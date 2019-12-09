import aiohttp_jinja2

from app.handlers.abstract import AbstractView
from app.log import get_logger

log = get_logger()


class AdminEntity(AbstractView):

    @aiohttp_jinja2.template('admin.jinja2')
    async def get(self):

        return {}

    async def post(self):
        return {}
