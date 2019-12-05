import os


__all__ = [
    'Config',
]


env = os.environ.get


class Config:

    app_name = 'aiohttp-blog'
    app_env = 'stage'

    app_log_level = env('LOG_LEVEL', 'DEBUG')
    app_address = env('LISTEN_ADDR', '0.0.0.0')
    app_port = int(env('LISTEN_PORT', 8080))

    db_host = env('DB_HOST', '0.0.0.0')
    db_port = env('DB_PORT', 5432)
    db_name = env('DB_NAME', 'test')
    db_pass = env('DB_PASS', 'test')
    db_user = env('DB_USER', 'test')

    migrations = int(env('MIGRATIONS', 0))
