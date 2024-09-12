# app.py
from flask import Flask
import pandas as pd


app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, OpenShift with Docker!'

@app.route('/')
def hello_world():
    df = pd.DataFrame({'Data': [1, 2, 3]})
    return df, 'Hello, OpenShift with Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)