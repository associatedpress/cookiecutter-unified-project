#!/bin/bash
## This post project generation script only runs if uv is on the machine
command -v uv >/dev/null 2>&1 || { echo >&2 "uv not found.  Aborting startup script."; exit 1; }

## Write out project properties
echo '{
  "kernel_name": "{{cookiecutter.project_slug}}"
}' > kernel_config.json

## Init uv & virtualenv
uv init
uv venv
uv add jupyterlab ipykernel ipython jupytext jupyterlab_templates
uv run set_jupyter_kernel.py
git add .
git commit -m "Initial commit"