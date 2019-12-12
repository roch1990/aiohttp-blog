import json

import aiohttp_jinja2

from app.database.methods.select import get_all_categories
from app.handlers.abstract import AbstractView
from app.log import get_logger

log = get_logger()


class UserCategories(AbstractView):

    @aiohttp_jinja2.template('categories.jinja2')
    async def get(self):

        categories = await get_all_categories(
            engine=self.database
        )

        return {'payload': categories}

    async def post(self):
        return {}
