import subprocess
import pathlib
import random
import string
import shutil

from create_proj.models import BackEndChoices


def create_django_project(database):
    """."""

    dj_parent_dir = pathlib.Path.cwd().parent.parent
    proj_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    db_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    dj_dir = dj_parent_dir / proj_name
    cmd = f"""
    mkdir {dj_dir}
    cd {dj_dir}
    echo "db_name={db_name} db_type={database}" > README.md
    python3 -m venv venv
    . venv/bin/activate
    pip install django djangorestframework
    django-admin startproject {proj_name}
    mv {proj_name} src
    """
    subprocess.check_output(cmd, shell=True)
    venv_path = dj_dir / 'venv'
    shutil.rmtree(venv_path)
    zip = shutil.make_archive(proj_name, 'zip', f'{dj_dir}')
    shutil.rmtree(f'{dj_dir}')
    return pathlib.Path(zip)


def create_project_archive(backend, frontend, database):
    """."""

    if backend == BackEndChoices.DJANGO.value:
        return create_django_project(database)
