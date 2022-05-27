import subprocess
import pathlib
import random
import string
import shutil

from create_proj.models import BackEndChoices, FrontEndChoices


#Variables
# parent_dir
# custom_file dir
# db variables

def create_django_angular_project(database):
    """."""

    proj_name = ''.join(random.choices(string.ascii_lowercase, k=10)) #-- we can make it like this--> angular_djangodijfm 
    parent_dir = pathlib.Path.cwd().parent.parent / proj_name
    db_name = ''.join(random.choices(string.ascii_lowercase, k=10)) # we can choose give name  ateamdb
    DATABASES = "{opening_brace}'default': {opening_brace}'ENGINE': 'django.db.backends.{database}','OPTIONS': {opening_brace}'read_default_file': '/path/to/{database}.cnf',{closing_brace},{closing_brace}{closing_brace}"
    DATABASES = DATABASES.format(database=database, opening_brace='{', closing_brace='}')
    #db_name=kglpcnqhhc db_type=mysql
    cmd = f"""
    mkdir -p {parent_dir}
    cd {parent_dir}
    echo "db_name={db_name} db_type={database}" > README.md
    . ../venv/bin/activate           
    pip3 freeze > requirements.txt
    django-admin startproject backend
    ng new frontend --defaults --skip-install=true
    """               # for activating virual env first we need to create one
    subprocess.check_output(cmd, shell=True)
    with open(parent_dir / 'backend' / 'backend' / 'settings.py', 'a') as f:
        f.write(f"DATABASES = {DATABASES}")
    zip = shutil.make_archive(proj_name, 'zip', f'{parent_dir}')
    shutil.rmtree(f'{parent_dir}')
    return pathlib.Path(zip)

def getnerateDbUri(database):
    user = 'ateam'              ## should save creds in some file
    password = 'adminateam'
    host = '127.0.0.1'
    dbName = 'NameList'
    port_dic = {"mysql":3306,"postgres":5432,"mssql":1433,"oracle":1521}
    db = database  # mysql/oracle/...
    dbUri = "{0}://{1}:{2}@{3}:{4}/{5}".format(db,user, password, host, port_dic[db], database)


def create_flask_angular_project(database):
    proj_name = "flask_angular"+''.join(random.choices(string.ascii_lowercase, k=4))
    parent_dir = pathlib.Path.cwd().parent.parent / proj_name
    custom_path = str(pathlib.Path.cwd()) + "/custom"
    db_name = "ateamdb"
    dbURI = getnerateDbUri(database)
    cmd = f"""
    mkdir -p {parent_dir}
    cd {parent_dir}
    echo "db_name={db_name},db_type={database},db_uri={dbURI}" > README.md
    . ../venv/bin/activate  
    pip3 install -r {custom_path}/flask/requirements.txt
    mkdir backend
    cp {custom_path}/flask/main.py ./backend
    ng new frontend --defaults --skip-install=true
    rm -rf ./frontend/src/app
    cp -R {custom_path}/angular/app ./frontend/src
    """
    subprocess.check_output(cmd, shell=True)
    zip = shutil.make_archive(proj_name, 'zip', f'{parent_dir}')
    shutil.rmtree(f'{parent_dir}')
    return pathlib.Path(zip) 


def create_project_archive(backend, frontend, database):
    """."""

    if backend == BackEndChoices.DJANGO.value and frontend == FrontEndChoices.ANGULAR.value:
        return create_django_angular_project(database)

    elif backend == BackEndChoices.FLASK.value and frontend == FrontEndChoices.ANGULAR.value:
        return create_flask_angular_project(database)
