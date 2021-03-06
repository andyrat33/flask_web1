from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<string:name>')
def hello(name: str):
    return f'Hello {name}'

@app.route('/goodbye/<string:name>')
def hello(name: str):
    return f'Goodbye {name}'

if __name__ == '__main__':
    app.run()
