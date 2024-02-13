from flask import Flask, redirect, request, session, url_for, render_template_string
from bokeh.embed import server_document
from bokeh.server.server import Server
from threading import Thread
from tornado.ioloop import IOLoop

# Import the modify_doc function from main.py
from main import modify_doc

app = Flask(__name__)
app.secret_key = 'qwerty'  # Change this to a random secret key

LOGIN_PAGE = '''
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form action="" method="post">
    <p><input type=text name=username placeholder=Username>
    <p><input type=password name=password placeholder=Password>
    <p><input type=submit value=Login>
</form>
'''

# Simple user database
users = {'admin': 'secret'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('bokeh_app'))
    return render_template_string(LOGIN_PAGE)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/bokeh_app')
def bokeh_app():
    if 'username' not in session:
        return redirect(url_for('login'))
    script = server_document('http://localhost:5006/bokeh_app')
    return render_template_string('<html><body>{{ script|safe }}</body></html>', script=script)

def bk_worker():
    server = Server({'/bokeh_app': modify_doc}, 
                    io_loop=IOLoop(), 
                    allow_websocket_origin=["10.0.4.103:5006"])
    server.start()
    server.io_loop.start()

Thread(target=bk_worker).start()

if __name__ == '__main__':
    app.run(port=8000, debug=True, host='0.0.0.0')
