import asyncio

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiopg.sa import create_engine

# from app.database.common import prepare_tables
from app.handlers.user.dashboard import UserDashboard
from app.handlers.user.entity import UserEntity
from config import Config


async def database_client(app):
    app['database'] = await create_engine(
        user=Config.db_user,
        database=Config.db_name,
        host=Config.db_host,
        port=Config.db_port,
        password=Config.db_pass
    )
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

    # Category handlers
    app.router.add_route(path='/', handler=UserDashboard, name='dashboard', method='get')

    # Entity handler
    app.router.add_route(path='/entity/{entity_id}', handler=UserEntity, name='entity', method='get')

    # Don't use this for production. Use nginx static (for example) instead.
    app.router.add_static(
        prefix=f'/static',
        path=f'{project_root}/static',

    )

    return app
