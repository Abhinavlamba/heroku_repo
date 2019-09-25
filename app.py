from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Home page success."
def f(n):
    if n <= 1:
        return 1
    else:
        return f(n-1) + f(n-2)

@app.route('/fib/<int:n>')
def fib(n):
    return str(f(n))

if __name__ == '__main__':
    print('Hello heroku')