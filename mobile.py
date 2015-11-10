import flask, flask.views
from flask import url_for, request, session, redirect, jsonify, Response, make_response, current_app
from jinja2 import environment, FileSystemLoader
from flask import render_template, request
from flask import session, redirect

app = flask.Flask(__name__)
app.secret_key = '234234rfascasascqweqscasefsdvqwefe2323234dvsv'


@app.route('/', methods=['GET', 'POST'])
def index_route():
    return flask.render_template('index.html')


@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
    return '',200


if __name__ == '__main__':
    app.debug = True
    app.run(port=int(os.environ['PORT']), host='0.0.0.0',threaded=True)