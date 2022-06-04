#!/usr/bin/python3

import sys
import os
import subprocess
import tempfile
from distutils.dir_util import copy_tree
import shutil, errno


def is_image(tag):
    output = subprocess.check_output(["docker", "image", "list"])
    lines = output.split(b"\n")[:-1]
    repositories = [line.split()[0].decode() for line in lines][1:]
    return tag in repositories


def get_base_dir(tag):
    return os.path.join(os.environ["DOUP_SEARCHDIR"], tag)


snippets_dir = os.path.join(os.environ["DOUP_SEARCHDIR"], "snippets")


def get_parent_tag(context):
    with open(os.path.join(context, "Dockerfile")) as f:
        for line in f:
            if line[:4] == "FROM":
                return line.split()[1]
    raise RuntimeError("There seems to be no FROM statement in the Dockerfile.")


def is_existing(tag):
    output = subprocess.check_output(["docker", "ps", "-a"])
    lines = output.split(b"\n")[:-1]
    tags = [line.split()[-1].decode() for line in lines][1:]
    return tag in tags


def stop(tag):
    subprocess.check_output(["docker", "stop", tag])
    subprocess.check_output(["docker", "rm", tag])


def get_snippet_name(line):
    striped_line = line.strip()
    if len(striped_line) > 0 and striped_line[0] == "*":
        return striped_line[1:]
    return None


def copy_file(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else:
            raise OSError("Failed to copy {} to {}.".format(src, dst))


def get_file_name(line):
    striped_line = line.strip()
    if len(striped_line) > 6 and striped_line[:6] == "*file=":
        return striped_line[6:]
    return None


def copy_snippet_files(snippet_name, destionation):
    with open(os.path.join(snippets_dir, snippet_name)) as snippet:
        for snippet_line in snippet:
            file_name = get_file_name(snippet_line)
            if file_name:
                src = os.path.join(snippets_dir, file_name)
                dst = os.path.join(destionation, file_name)
                copy_file(src, dst)


def get_snippet_lines(snippet_name):
    with open(os.path.join(snippets_dir, snippet_name)) as snippet:
        for snippet_line in snippet:
            if not get_file_name(snippet_line):
                yield snippet_line


def generate_dockerfile_lines(dockerfile, temp_context_dir):
    # Has pretty nasty side effect.
    with open(dockerfile) as f:
        for line in f:
            snippet_name = get_snippet_name()
            if snippet_name:
                copy_snippet_files(snippet_name, temp_context_dir)
                for snippet_line in get_snippet_lines(snippet_name):
                    yield snippet_line
            yield line


def build(tag):
    if is_existing(tag):
        stop(tag)
    context = os.path.join(get_base_dir(tag), "context")
    parent_tag = get_parent_tag(context)
    parent_context = os.path.join(get_base_dir(parent_tag), "context")
    if not is_image(parent_tag) and os.path.exists(parent_context):
        build(parent_tag)

    temp_context_dir = tempfile.mkdtemp()
    copy_tree(context, temp_context_dir)
    dockerfile_lines = []
    temp_dockerfile = os.path.join(temp_context_dir, "Dockerfile")
    dockerfile_lines = list(generate_dockerfile_lines(temp_dockerfile, temp_context_dir))
    with open(os.path.join(temp_context_dir, "Dockerfile"), "w") as f:
        f.writelines(dockerfile_lines)

    build_command = "tar -czh . | DOCKER_BUILDKIT=1 docker build --no-cache -t {} -".format(tag)
    subprocess.check_output(build_command, shell=True, cwd=temp_context_dir)


def run(tag):
    if is_existing(tag):
        stop(tag)

    user_mounts = []
    user_mounts_file_path = os.path.join(os.environ["DOUP_SEARCHDIR"], "mounts")
    if os.path.exists(user_mounts_file_path):
        with open(user_mounts_file_path) as f:
            user_mounts = [mount.strip() for mount in f.readlines()]

    mounts = [
        (os.path.join(get_base_dir(tag), "context"), "/home/devuser/context"),
        (os.path.join(get_base_dir(tag), "workspace"), "/home/devuser/workspace")
    ]
    for local_path, _ in mounts:
        if not os.path.exists(local_path):
            raise RuntimeError("Cant mount {} it is not a dir/file!".format(local_path))

    run_command = "docker run {} {} --network host -td --name {} {}".format(
        " ".join("-v {}".format(mount) for mount in user_mounts),
        " ".join("-v {}:{}".format(local_path, docker_path) for local_path, docker_path in mounts), tag, tag)
    subprocess.check_output(run_command, shell=True)


def is_running(tag):
    output = subprocess.check_output(["docker", "ps"])
    lines = output.split(b"\n")[:-1]
    tags = [line.split()[-1].decode() for line in lines][1:]
    return tag in tags


def connect(tag):
    os.system("docker exec -it {} /usr/bin/env bash".format(tag))


def remove_image(tag):
    if is_existing(tag):
        stop(tag)
    subprocess.check_output(["docker", "rmi", tag])


def main():
    if len(sys.argv) == 1:
        print("At least one argument is required.")
        exit(1)
    tag = sys.argv[1]
    command = sys.argv[2] if len(sys.argv) == 3 else "run"
    if command not in ["run", "update", "stop"]:
        print("Invalid command: {}".format(command))
        exit(1)

    if command == "stop":
        if not is_running(tag):
            print("No container stoped nor removed. {} is not running.".format(tag))
            sys.exit(1)
        else:
            stop(tag)
            sys.exit(0)

    valid_image = is_image(tag)
    if valid_image and command == "update":
        remove_image(tag)
        valid_image = False
    if not valid_image:
        build(tag)
    if not is_running(tag):
        run(tag)
        os.system("clear")
    connect(tag)


if __name__ == "__main__":
    main()
