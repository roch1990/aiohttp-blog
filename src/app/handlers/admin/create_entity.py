import aiohttp_jinja2

from app.database.methods.select import get_all_categories
from app.handlers.abstract import AbstractView
from app.log import get_logger

log = get_logger()


class AdminCreateEntity(AbstractView):

    @aiohttp_jinja2.template('admin_create_entity.jinja2')
    async def get(self):

        categories = await get_all_categories(
            engine=self.database
        )

        return {'payload': categories}

    async def post(self):
        log.debug()
        return {}
