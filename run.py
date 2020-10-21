from aiohttp import web
from aiohttp_rest_framework import setup_rest_framework
from app.load_conf import load_config
from app.utils import create_app


config = load_config()
app = create_app(config)
setup_rest_framework(app)

if __name__ == '__main__':
    web.run_app(app)
