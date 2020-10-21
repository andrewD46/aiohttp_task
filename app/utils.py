from aiohttp import web
from app.urls import add_urls
from aiopg.sa import create_engine


def create_app(config_file):
    app = web.Application()
    add_urls(app)
    config_file.pop('sqlalchemy')
    app['config.yaml'] = config_file
    app.on_startup.append(go)
    app.on_cleanup.append(close_db)
    return app


async def go(app):
    app['db'] = await create_engine(**app['config.yaml'])


async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()
