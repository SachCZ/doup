# doup

Doup is a simple script enabling to build and run a docker container from a Dockerfile using a single command.

## Install
From version 5 onward simply download the release or clone this repo. Then run

```bash
sudo ./install.sh
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
build. Other files you wish to mount to the docker can be specified in `<searchdir>/mounts`, eg.:
```
$HOME/.ssh:/home/devuser/.ssh
```

Use `doup myawsomedocker` to run, `doup myawsomedocker stop` to stop and `doup myawsomedocker
update` to rebuild the image.

