#!/usr/bin/env bash
set -e
USER_HOME=$(getent passwd $SUDO_USER | cut -d: -f6)
cp -r workspace "${USER_HOME}/.doupworkspace"
cp doup.py /usr/local/bin/doup
chmod +x /usr/local/bin/doup
cp doup-completion /etc/bash_completion.d/doup
echo "Done."

