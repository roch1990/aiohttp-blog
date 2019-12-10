import datetime

import aiohttp_jinja2
from babel.dates import format_datetime

from app.database.methods.select import get_all_entities, get_all_categories
from app.handlers.abstract import AbstractView
from app.log import get_logger
from config import Config

log = get_logger()


class UserDashboard(AbstractView):

    @aiohttp_jinja2.template('dashboard.jinja2')
    async def get(self):

        entities: list = await get_all_entities(
            engine=self.database,
        )
        categories: list = await get_all_categories(
            engine=self.database
        )

        for entity in entities:
            for categorie in categories:
                if entity.get('category_id') != categorie.get('id'):
                    continue
                entity['category'] = categorie.get('title')
                break

            entity['text'] = f'{entity.get("text")[0:360]}...'
            entity['creation_date'] = format_datetime(
                datetime.datetime.strptime(
                    entity.get('creation_date'),
                    '%Y-%m-%d %H:%M:%S.%f',
                ),
                locale=Config.babel_locale,
            )

        entities = sorted(entities, key=lambda entity: entity.get('creation_date'), reverse=True)

        return {'payload': entities}

    async def post(self):
        return {}
