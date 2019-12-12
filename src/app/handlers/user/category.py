import datetime

import aiohttp_jinja2
from babel.dates import format_datetime

from app.database.methods.select import get_all_entities, get_all_categories, get_entity_by_category_name
from app.handlers.abstract import AbstractView
from app.log import get_logger
from config import Config

log = get_logger()


class UserCategory(AbstractView):

    @aiohttp_jinja2.template('dashboard.jinja2')
    async def get(self):

        entities: list = await get_entity_by_category_name(
            engine=self.database,
            category_title=self.request.match_info['category_title']
        )

        for entity in entities:
            entity['creation_date'] = format_datetime(
                datetime.datetime.strptime(
                    entity.get('creation_date'),
                    '%Y-%m-%d %H:%M:%S.%f',
                ),
                locale=Config.babel_locale,
            )

        return {'payload': entities}

    async def post(self):
        return {}
