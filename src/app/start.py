import asyncio

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiopg.sa import create_engine

# from app.database.common import prepare_tables
from app.handlers.admin.categories import AdminCategories
from app.handlers.admin.create_entity import AdminCreateEntity
from app.handlers.user.about_me import UserAbout
from app.handlers.user.categories import UserCategories
from app.handlers.user.category import UserCategory
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

    aiohttp_jinja2.setup(
        app=app,
        loader=jinja2.FileSystemLoader('./templates'),
    )
    app.cleanup_ctx.append(database_client)

    # For user
    # Category handlers
    app.router.add_route(path='/', handler=UserDashboard, name='dashboard', method='get')
    app.router.add_route(path='/categories', handler=UserCategories, name='categories', method='get')
    app.router.add_route(path='/category/{category_title}', handler=UserCategory, name='category', method='get')
    # Entity handler
    app.router.add_route(path='/entity/{entity_id}', handler=UserEntity, name='entity', method='get')
    # About me handler
    app.router.add_route(path='/about_me', handler=UserAbout, name='about_me', method='get')

    # For admin
    # Categories
    app.router.add_route(path='/admin/categories', handler=AdminCategories, name='admin_categories', method='get')
    # Entities
    app.router.add_route(path='/admin/entity/create', handler=AdminCreateEntity, name='admin_create_entity', method='get')
    app.router.add_route(path='/admin/entity/create', handler=AdminCreateEntity, name='admin_create_entity', method='post')

    # Don't use this for production. Use nginx static (for example) instead.
    app.router.add_static(
        prefix=f'/static',
        path=f'{project_root}/static',

    )

    return app
