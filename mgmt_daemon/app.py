from flask import Flask, render_template, redirect, request
import hashlib
import json

app = Flask(__name__)

@app.route('/')
def main_redirect():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login/check', methods=['GET', 'POST'])
def login_check():
    f = open('static/config/mgmt_config.json', 'r', encoding='utf-8')# 读取config
    json_res = json.load(f)
    json_username = json_res['username']
    json_password = json_res['password']
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        str_md5 = md5.hexdigest()
        if username == json_username and str_md5 == json_password:
            return redirect('/board')
        else:
            return render_template('login_error.html')
    else:
        print('请求必须为POST类型')
        pass

@app.route('/board')
def board():
    return render_template('board.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='20500')