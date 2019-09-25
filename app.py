from flask import Flask
from mylib.mat import fib as f
app = Flask(__name__)

@app.route('/')
def home():
    return "Home page success."
@app.route('/fib/<int:n>')
def fib(n):
    return str(f(n))

if __name__ == '__main__':
    print('Hello heroku')