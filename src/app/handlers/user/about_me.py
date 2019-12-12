import datetime

import aiohttp_jinja2
from babel.dates import format_datetime

from app.database.methods.select import get_all_entities, get_all_categories, get_entity_by_category_name
from app.handlers.abstract import AbstractView
from app.log import get_logger
from config import Config

log = get_logger()


class UserAbout(AbstractView):

    @aiohttp_jinja2.template('about_me.jinja2')
    async def get(self):
        return {'name': 'Andrew', 'surname': 'Svetlov'}

    async def post(self):
        return {}
