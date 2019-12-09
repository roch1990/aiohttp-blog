import json

import aiohttp_jinja2

from app.database.methods.select import get_all_categories
from app.handlers.abstract import AbstractView
from app.log import get_logger

log = get_logger()


class UserCategory(AbstractView):

    @aiohttp_jinja2.template('user_categories.jinja2')
    async def get(self):

        records = await get_all_categories(
            engine=self.database,
        )

        log.debug(records)

        return {'payload': records}

    async def post(self):
        return {}
