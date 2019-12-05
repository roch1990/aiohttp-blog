import asyncio

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiopg.sa import create_engine

from app.database.common import prepare_tables
from app.handlers.admin import Admin
from app.handlers.dashboard import Dashboard
from config import Config


async def database_client(app):
    app['database'] = await create_engine(
        user=Config.db_user,
        database=Config.db_name,
        host=Config.db_host,
        port=Config.db_port,
        password=Config.db_pass
    )
    if Config.migrations:
        await prepare_tables(app['database'])
    yield

    await app['database'].wait_close()
    await asyncio.sleep(0.250)


async def make_app(project_root: str) -> web.Application:

    app = web.Application()

    path_prefix = 'awesome_blog'

    aiohttp_jinja2.setup(
        app=app,
        loader=jinja2.FileSystemLoader('./templates'),
    )
    app.cleanup_ctx.append(database_client)

    # Admin handlers
    app.router.add_route(path=f'/{path_prefix}/admin', handler=Admin, name='admin', method='get')
    app.router.add_route(path=f'/{path_prefix}/admin', handler=Admin, name='admin', method='post')

    # Dashboard handlers
    app.router.add_route(path=f'/{path_prefix}/dashboard', handler=Dashboard, name='dashboard', method='get')
    app.router.add_route(path=f'/{path_prefix}/dashboard', handler=Dashboard, name='dashboard', method='post')

    # Don't use this for production. Use nginx static (for example) instead.
    app.router.add_static(
        prefix=f'/static',
        path=f'{project_root}/static',

    )

    return app
