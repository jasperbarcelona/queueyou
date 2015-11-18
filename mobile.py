import flask, flask.views
from flask import url_for, request, session, redirect, jsonify, Response, make_response, current_app
from jinja2 import environment, FileSystemLoader
from flask import render_template, request
from flask import session, redirect, jsonify
import requests
import os

app = flask.Flask(__name__)
app.secret_key = '234234rfascasascqweqscasefsdvqwefe2323234dvsv'
QUEUE_URL = 'http://appyourserver.herokuapp.com/api/queue/fetch/'
SVC_URL = 'http://appyourserver.herokuapp.com/api/user/svc/generate/'
LOGIN_URL = 'http://appyourserver.herokuapp.com/api/user/login/'


@app.route('/', methods=['GET', 'POST'])
def index_route():
    if not session:
        return redirect('/signin')

    return flask.render_template('index.html')


@app.route('/data/update', methods=['GET', 'POST'])
def update_data():
    get_queue = requests.get(
        QUEUE_URL,
        params = {'api_key':session['api_key']}
        )
    queue = get_queue.json()

    return jsonify(
        client_name=queue['client_name'],
        queue_no=queue['queue_no'],
        now_serving=queue['current'],
        hours=queue['estimated_hours'],
        minutes=queue['estimated_minutes']
        )
    

@app.route('/signin/', methods=['GET', 'POST'])
def user_sign_in():
    if session:
        return redirect('/')
    error_message=flask.request.args.get('message')
    error_code=flask.request.args.get('error')
    if error_code == '401':
        return flask.render_template('login.html', error=error_message)
    return flask.render_template('login.html', error='')


@app.route('/user/authenticate', methods=['GET', 'POST'])
def get_svc():
    generate_svc = requests.post(
        SVC_URL,
        {'msisdn':flask.request.form.get('msisdn')}
        )
    resp = generate_svc.json()
    if resp['status'] == 'failed':
        return jsonify(error=generate_svc.status_code,message=resp['error'])
    return flask.render_template('svc.html')


@app.route('/user/login', methods=['GET', 'POST'])
def user_login():
    data = flask.request.form.to_dict()
    login = requests.post(
        LOGIN_URL,
        {
        'msisdn':data['msisdn'],
        'svc':data['svc']
        }
        )
    login_resp = login.json()
    if login_resp['status'] == 'failed':
        return jsonify(error=login.status_code,message=login_resp['error'])
    session['api_key'] = login_resp['api_key']
    return jsonify(status=login.status_code)


@app.route('/logout', methods=['GET', 'POST'])
def user_log_out():
    session.clear()
    return redirect('/signin')


@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
    return '',200


if __name__ == '__main__':
    app.debug = True
    app.run(port=int(os.environ['PORT']),host='0.0.0.0',threaded=True)