from aiopg.sa import Engine
from sqlalchemy import Table

from app.database.common import resultproxy_to_dict
from app.database.models.category import Category
from app.database.models.entity import Entity


async def get_all_categories(
        engine: Engine,
):

    table: Table = Category.__table__

    async with engine.acquire() as conn:
        async with conn.begin():

            result = await conn.execute(table.select())
            output = resultproxy_to_dict(result)
    return output


async def get_all_entities(
        engine: Engine,
):

    table: Table = Entity.__table__

    async with engine.acquire() as conn:
        async with conn.begin():

            result = await conn.execute(table.select())
            output = resultproxy_to_dict(result)
    return output


async def get_entity_by_category(
        engine: Engine,
        category_id: int
):

    table: Table = Entity.__table__

    async with engine.acquire() as conn:
        async with conn.begin():

            result = await conn.execute(table.select().where(table.c.category_id == category_id))
            output = resultproxy_to_dict(result)

    return output


async def get_entity_by_id(
        engine: Engine,
        entity_id: int
):

    table: Table = Entity.__table__

    async with engine.acquire() as conn:
        async with conn.begin():

            result = await conn.execute(table.select().where(table.c.id == entity_id))
            output = resultproxy_to_dict(result)

    if len(output) == 0:
        return None

    return output[0]
