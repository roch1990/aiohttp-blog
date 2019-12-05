import os

from aiohttp import web

from app.start import make_app
from config import Config

project_root = os.path.dirname(os.path.abspath(__file__))

# Входная точка приложения
web.run_app(
    make_app(
        project_root=project_root),
        host=Config.app_address,
        port=Config.app_port,
)
