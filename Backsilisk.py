#!/usr/bin/python3.7
from bottle import route, run, error, get, post, request, template
from Authent import *
from Safe import *

a = Authent()
s = Safe()

@route('/hello')
def hello():
    return "Hello World!"

@get('/login') # or @route('/login')
def login():
    return template('login.tpl')

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if a.checkLogin(username, password):
        return template('std.tpl', name=username)
    else:
        return "<p>Login failed.</p>"

@get('/safe/<user>/<table>')
def safe(user, table):
    s.connect(user)
    data = s.getTable(user, table)
    return template('safe.tpl', _data=data)

@error(404)
def error404(error):
    return "Nothing here, sorry"

run(host='localhost', port=8080, debug=True, reloader=True)