# doup

Doup is a simple script enabling to build and run a docker container from a Dockerfile using a single command.

## Install
Install using (specifying the desired version, eg. `version-4.0.0`):

```
sudo sh -c 'mkdir -p /tmp/doupinstall && curl -L 'https://github.com/SachCZ/doup/archive/refs/tags/version-4.0.0.tar.gz' | tar -xz -C /tmp/doupinstall/ --strip-components=1 && cp /tmp/doupinstall/doup-executable /usr/local/bin/doup && chmod +x /usr/local/bin/doup && cp /tmp/doupinstall/doup-completion /etc/bash_completion.d/doup && rm -rf /tmp/doupinstall/'
```

## Usage
You must set an `env` variable pointing to a dir containing directories with specified structure (`<searchdir>`). Put this into your
`.bashrc`:

```
export DOUP_SEARCHDIR=<searchdir>
```

The folders must obey this structure:
```
<searchdir>/myawsomedocker/context/Dockerfile
<searchdir>/myawsomedocker/workspace
```
The directories `workspace` and `context` will be mounted to the docker image. `context` is used during
build.

Use `doup myawsomedocker` to run, `doup myawsomedocker stop` to stop and `doup myawsomedocker
update` to rebuild the image.

