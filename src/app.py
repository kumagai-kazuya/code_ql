import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 1. 任意のコード実行の脆弱性 (Arbitrary Code Execution)
@app.route('/execute')
def execute():
    user_input = request.args.get('code')  # ユーザー入力
    eval(user_input)  # この行が脆弱です
    return 'Code executed!'

# 2. SQL インジェクションの脆弱性 (SQL Injection)
@app.route('/login')
def login():
    username = request.args.get('username')  # ユーザー入力
    password = request.args.get('password')  # ユーザー入力

    # SQLクエリを直接文字列結合しているため、SQLインジェクションの脆弱性あり
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = sqlite3.connect('test.db')
    cursor = conn.execute(query)  # この行が脆弱です
    user = cursor.fetchone()

    if user:
        return 'Login successful'
    else:
        return 'Login failed'

if __name__ == '__main__':
    app.run(port=3000)
