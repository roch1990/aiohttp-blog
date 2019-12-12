import datetime

import aiohttp_jinja2
import markdown2
from aiohttp import web
from babel.dates import format_datetime

from app.database.methods.select import get_entity_by_id
from app.handlers.abstract import AbstractView
from app.log import get_logger
from config import Config

log = get_logger()


class UserEntity(AbstractView):

    @aiohttp_jinja2.template('user_entity.jinja2')
    async def get(self):

        entity = await get_entity_by_id(
            engine=self.database,
            entity_id=self.request.match_info['entity_id']
        )

        if not entity:
            raise web.HTTPNotFound()

        # convert datetime to pretty view
        entity['creation_date'] = format_datetime(
            datetime.datetime.strptime(
                entity.get('creation_date'),
                '%Y-%m-%d %H:%M:%S.%f',
            ),
            locale=Config.babel_locale,
        )
        entity['text'] = markdown2.markdown(
            entity.get('text')
        )
        return {'payload': entity}

    async def post(self):
        return {}
