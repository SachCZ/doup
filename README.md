# doup

Doup is a simple script enabling to build and run a docker container from a Dockerfile using a single command.

## Install
Install using (specifying the desired version, eg. `version-1.1.1`):

```
sudo sh -c 'mkdir -p /tmp/doupinstall && curl -L 'https://github.com/SachCZ/doup/archive/refs/tags/version-1.1.1.tar.gz' | tar -xz -C /tmp/doupinstall/ --strip-components=1 && cp /tmp/doupinstall/doup-executable /usr/local/bin/doup && chmod +x /usr/local/bin/doup && cp /tmp/doupinstall/doup-completion /etc/bash_completion.d/doup && rm -rf /tmp/doupinstall/'
```

You must set an `env` variable pointing to a dir containing your dockerfiles (`<searchdir>`). Put this into your
`.bashrc`:

```
export DOUP_SEARCHDIR=<searchdir>
```

## Usage
Put a valid docker file named `Docker.myawsomedocker` into `<searchdir>`. The run:

```
doup myawsomedocker
```
