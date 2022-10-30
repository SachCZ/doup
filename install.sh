#!/usr/bin/env bash
set -e
WORKSPACE_DIR=${HOME}/.doupworkspace
echo "Installing templates to ${WORKSPACE_DIR}"
mkdir -p ${WORKSPACE_DIR}
cp -r workspace/* ${WORKSPACE_DIR}
echo "Installing exe to /usr/local/bin/doup"
sudo cp doup.py /usr/local/bin/doup
sudo chmod +x /usr/local/bin/doup
echo "Installing completion to /etc/bash_completion.d/doup"
sudo cp doup-completion /etc/bash_completion.d/doup
echo "Done."
