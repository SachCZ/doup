# syntax = docker/dockerfile:experimental
FROM debian:bookworm

RUN apt-get update

*essential
*user
*git
*misc
*starship
*tmux
*neovim
*rust
*cpp-bookworm

USER devuser
WORKDIR /home/devuser/
