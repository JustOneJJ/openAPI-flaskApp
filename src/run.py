import os

import connexion

import sys
sys.path.append("api")

from api.swagger_server import encoder

import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

def create_app():
    "start app"
    abs_file_path = os.path.abspath(os.path.dirname(__file__))
    #openapi_path = os.path.join(abs_file_path, "../", "../" "openapi")
    openapi_path = os.path.join(abs_file_path, "./api/swagger_server/swagger")
    app = connexion.FlaskApp(
        __name__, specification_dir=openapi_path, options={"swagger_ui": True, "serve_spec": True}
    )
    #app.add_api("spec.yml", strict_validation=True)
    app.add_api("swagger.yaml", strict_validation=True)
    flask_app = app.app
    flask_app.json_encoder = encoder.JSONEncoder

    return flask_app