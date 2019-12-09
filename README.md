# aiohttp-blog
python 3.7 aiohttp blog sample

## how create migration

- `alembic revision --autogenerate -m "init tables"`

## how make migration

- `alembic upgrade head`

## how downgrade migration

- `alembic downgrade $revision`

## how to add fixtures to db

- `cd ./tests/fixtures`
- `python database.py`

## problems:

### can't find app module

- `export PYTHONPATH=$PYTHONPATH:'$you_home_dir/$path_to_folder with project/aiohttp-blog/src'`

###  No config file 'alembic.ini' found

- make all operations with alembic from ./src/app/database/migrations/ folder