from flask import Flask

from quiz.config import Config
from quiz.database import quizes
from quiz.mquiz.models import Quizes
from quiz.mquiz.routes import bp1
from quiz.users.routes import bp2
from quiz.auth_middleware import Middleware

def create_app():
    app = Flask(__name__)
    app.wsgi_app = Middleware(app.wsgi_app)

    app.config.from_object(Config)

    app.register_blueprint(bp1)
    app.register_blueprint(bp2)

    @app.route("/")
    def root():
        # quizes.drop()
        # qz1 = Quizes.find_quizes('quiz1')
        # Quizes.add_questions('quiz1',{'testq1':'testa1','testq2':'testa2'})
        # Quizes.add_solvers('quiz1',['me','you'])
        # Quizes.remove_questions('quiz1',['testq1=2',])
        # Quizes.remove_solvers('quiz1',['me',])
        return "app-root"

    return app
