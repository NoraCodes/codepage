from flask import Flask
from database import getdb

app = Flask(__name__)

@app.route("/")
def hello():
    with getdb() as db:
        return "Hello, world"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

