"""Post-generation bootstrap.

Written in Python (rather than a shell script) so it runs identically on
Windows, macOS and Linux: Cookiecutter always executes ``*.py`` hooks with the
Python interpreter, whereas ``*.sh`` hooks are handed to the OS shell -- on
Windows that opens the file in an editor instead of running it.

Only runs if ``uv`` is on the machine.
"""

import json
import shutil
import subprocess
import sys

KERNEL_NAME = "{{ cookiecutter.project_slug }}"


def run(*args):
    """Run a command, aborting the hook if it fails."""
    subprocess.run(list(args), check=True)


def main():
    if shutil.which("uv") is None:
        print("uv not found.  Aborting startup script.", file=sys.stderr)
        sys.exit(1)

    # Write out project properties
    with open("kernel_config.json", "w") as f:
        json.dump({"kernel_name": KERNEL_NAME}, f)

    # Init uv & virtualenv
    run("uv", "init", "--bare", "--vcs", "none")
    run("uv", "venv")
    run("uv", "add", "jupyterlab", "ipykernel", "ipython", "jupytext",
        "jupyterlab_templates")
    run("uv", "run", "set_jupyter_kernel.py")

    run("git", "init")
    run("git", "add", ".")
    run("git", "commit", "-m", "Initial commit")


if __name__ == "__main__":
    main()
