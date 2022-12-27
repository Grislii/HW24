import os

from flask import Flask, request, jsonify
from flask_restx import Resource, Api, Namespace
from werkzeug.exceptions import BadRequest

from utils import do_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

perform_query_ns = Namespace("perform_query")

api = Api(app)
api.add_namespace(perform_query_ns)


@perform_query_ns.route("/")
class PerformQuery(Resource):
    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py
    def post(self):
        rq_json = request.json

        filename = rq_json["file_name"]

        if not os.path.exists(os.path.join(DATA_DIR, filename)):
            raise BadRequest

        return jsonify(do_query(rq_json, DATA_DIR))
    # return app.response_class('', content_type="text/plain")

if __name__ == "__main__":
    app.run()
