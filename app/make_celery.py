from .factory import create_app

flask_app = create_app(create_app=True)
celery_app = flask_app.extensions["celery"]
