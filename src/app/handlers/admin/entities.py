import aiohttp_jinja2

from app.handlers.abstract import AbstractView
from app.log import get_logger

log = get_logger()


class AdminEntities(AbstractView):

    @aiohttp_jinja2.template('admin_entities.jinja2')
    async def get(self):
        return {}

    async def post(self):
        return {}
