from flask import Flask, render_template, request

app = Flask(__name__)

# ホームページのルート
@app.route('/')
def home():
    return render_template('index.html')

# 挨拶を返すルート
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"こんにちは、{name}さん！"

if __name__ == '__main__':
    app.run(debug=True)