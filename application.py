# from flask import Flask, render_template, request

# import logging
# from news import menus_blueprint

# from rest_server.resource import TemperatureResource, TemperatureCreationResource
# from rest_server.resource_check import resource_blueprint
# from flask_restful import Api
#
#
# application = Flask(__name__)
# application.register_blueprint(menus_blueprint, url_perfix='/news')
# application.register_blueprint(resource_blueprint, url_perfix="/resource")
#
# api= Api(application)
# api.add_resource(TemperatureResource, "/resource/<sensor_id>")
# api.add_resource(TemperatureCreationResource, "/resource_creation")
#
# logging.basicConfig(filename='test.log', level=logging.DEBUG)
#
#
# # @app.route("/")
# # def hello_world():
# #     print("!!!!!")
# #     return "hellow123456798"
#
#
# @application.route("/")
# def hello_html():
#     value = 27
#     value_list = ['Mina', 'Momo', 'Sana']
#     return render_template(
#         'index.html',
#         name='Twice',
#         value_list=value_list,
#         value=value
#     )
#
#
# if __name__ == "__main__":
#
#     application.debug = True
#     application.run(host="localhost", port="8080")
import os

from flask import Flask, render_template
from flask_restful import Api
import logging

from database import base
from database.base import User
from views.menus import menus_blueprint
from views.auth import auth_blueprint
from rest_server.resource_check import resource_blueprint
from rest_server.resource import TemperatureResource, TemperatureCreationResource, TemperatureByLocationResource


from flask_login import current_user, LoginManager


application = Flask(__name__)
application.register_blueprint(menus_blueprint, url_prefix='/menus')
application.register_blueprint(auth_blueprint, url_prefix='/auth')
application.register_blueprint(resource_blueprint, url_prefix='/resource')

application.config['WTF_CSRF_SECRET_KEY'] = os.urandom(24)
application.config['SECRET_KEY'] = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(application)

@login_manager.user_loader
def load_user(user_id):
    q = base.db_session.query(User).filter(User.id == user_id)
    user = q.first()

    if user is not None:
        user._authenticated = True
    return user

api = Api(application)
api.add_resource(TemperatureResource, "/resource/<sensor_id>")
api.add_resource(TemperatureCreationResource, "/resource_creation")
api.add_resource(TemperatureByLocationResource, "/resource_location/<location>")

logging.basicConfig(
    filename='test.log',
    level=logging.DEBUG
)


@application.route('/')
def hello_html():
    value = 50
    value_list = ['파이썬', '자바', '스위프트']
    return render_template(
        'index.html',
        name="yhhan",
        value_list=value_list,
        value=value,
        nav_menu="home",
        current_user=current_user
    )


if __name__ == "__main__":
    logging.info("Flask Web Server Started!!!")

    application.debug = True
    application.config['DEBUG'] = True

    application.run(host="0.0.0.0", port="8080")