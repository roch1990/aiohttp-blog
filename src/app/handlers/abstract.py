from aiohttp import web
from aiopg.sa import Engine
from aioredis import Redis


class AbstractView(web.View):

    def __init__(self, request):
        super().__init__(request=request)

        self.database: Engine = request.app['database']
