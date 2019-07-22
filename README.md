# Restaurant API

## Requirements

Install a postgres database and virtualenv library to test this api.

## Setup

- Configure the config file in `app/main/config.py`, change the development database with your database information.
- Create your virtualenv and activate it:
```
virtualenv venv
. venv/bin/activate
```
- Install your application with the command `pip install --editable .` in the root directory.
- Run the following commands to create your restaurant model:
```
python3 manage.py db init
python3 manage.py db migrate --message 'initial database migration'
python3 manage.py db upgrade
```
- Launch your restaurant api server with `python3 manage.py run`.

## Tests

Run the test in using pytest library with the command `pytest`.