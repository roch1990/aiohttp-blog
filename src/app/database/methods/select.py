import sqlalchemy as sa
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


async def get_entity_by_category_name(
        engine: Engine,
        category_title: str
):

    entity_table: Table = Entity.__table__
    category_table: Table = Category.__table__

    join = sa.join(entity_table, category_table, entity_table.c.category_id == category_table.c.id)
    query = (sa.select([entity_table], use_labels=False)
             .select_from(join).where(category_table.c.title == category_title))

    async with engine.acquire() as conn:
        async with conn.begin():

            result = await conn.execute(query)
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
