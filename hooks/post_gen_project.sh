#!/bin/bash
## This post project generation script only runs if uv is on the machine
command -v uv >/dev/null 2>&1 || { echo >&2 "uv not found.  Aborting startup script."; exit 1; }

## Init uv & virtualenv
uv init
uv venv
git add .
git commit -m "Initial commit"