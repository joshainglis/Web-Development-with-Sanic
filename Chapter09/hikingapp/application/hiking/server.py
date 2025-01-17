from sanic import Sanic
from hiking.common.log import setup_logging


def create_app():
    app = Sanic(__name__)
    setup_logging(app)

    from hiking.middleware import request_context  # noqa
    from hiking.blueprints.view import bp  # noqa
    from hiking.worker import postgres  # noqa
    from hiking.worker import redis  # noqa

    app.blueprint(bp)

    return app
