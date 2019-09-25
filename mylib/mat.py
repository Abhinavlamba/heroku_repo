from flask import Blueprint

api = Blueprint('api',__name__)

@api.route('/')
def home():
    return "api reached"
 
@api.route('/<int:n>')
def fib_(n):
    return str(fib(n))
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

