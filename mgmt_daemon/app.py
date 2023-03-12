from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main_redirect():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='20500')