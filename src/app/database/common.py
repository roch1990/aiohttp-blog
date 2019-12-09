import datetime

import psycopg2
from sqlalchemy.engine import ResultProxy
from sqlalchemy.schema import CreateTable

from app.database.models.category import Category
from app.database.models.entity import Entity
from app.log import get_logger

log = get_logger()


# async def prepare_tables(engine):
#
#     tables = [
#         Entity.__table__,
#         Category.__table__
#     ]
#
#     async with engine.acquire() as conn:
#         for table in tables:
#             try:
#                 create_expr = CreateTable(table)
#                 await conn.execute(create_expr)
#             except psycopg2.ProgrammingError:
#                 pass


def resultproxy_to_dict(result: ResultProxy) -> dict:

    d, a = {}, []
    for rowproxy in result:
        for column, value in rowproxy.items():
            if isinstance(value, datetime.datetime):
                value = str(value)
            d = {**d, **{column: value}}
        a.append(d)
    return a
