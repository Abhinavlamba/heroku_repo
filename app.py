from flask import Flask
from mylib.nest.mat import api

app = Flask(__name__)
app.register_blueprint(api,url_prefix='/a')

@app.route('/')
def home():
    return "Home page success."

if __name__ == '__main__':
    print('Hello heroku')
    #Comments
