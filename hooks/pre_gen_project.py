import os
import sys

project_slug = "{{ cookiecutter.project_slug}}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\xb1[0m"

if project.slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {project_slug} is not a valid name for this project.")

    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create somethin aweaksome.")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")
