import subprocess
import pathlib
import random
import string
import shutil

from create_proj.models import BackEndChoices, FrontEndChoices


def create_django_angular_project(database):
    """."""

    proj_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    parent_dir = pathlib.Path.cwd().parent.parent / proj_name
    db_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    cmd = f"""
    mkdir -p {parent_dir}
    cd {parent_dir}
    echo "db_name={db_name} db_type={database}" > README.md
    python3 -m venv venv
    . venv/bin/activate
    pip install django djangorestframework
    django-admin startproject backend
    ng new frontend --defaults --skip-install=true
    """
    subprocess.check_output(cmd, shell=True)
    venv_path = parent_dir / 'venv'
    shutil.rmtree(venv_path)
    zip = shutil.make_archive(proj_name, 'zip', f'{parent_dir}')
    shutil.rmtree(f'{parent_dir}')
    return pathlib.Path(zip)


def create_project_archive(backend, frontend, database):
    """."""

    if backend == BackEndChoices.DJANGO.value and frontend == FrontEndChoices.ANGULAR.value:
        return create_django_angular_project(database)
