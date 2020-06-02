# coding: utf-8
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from app.utils import *

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config['Secret'] = "Secret"


@app.route('/', methods=['GET']) # To prevent Cors issues
@cross_origin(supports_credentials=True)
def index():
    response = jsonify(
                {
                    'status':'success',
                    'message': 'Welcome to Selenium-fetch-api mabe by sanix-darker, please check the documentation of the API here : https://documenter.getpostman.com/view/2696027/SztG46Bv?version=latest'
                }
            )
    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return response


@app.route('/get', methods=['GET']) # To prevent Cors issues
@cross_origin(supports_credentials=True)
def get_method():
    result = scrap_html_content(
            request.args.get('secret_key'),
            request.args.get('selector'),
            request.args.get('url')
        )
    response = jsonify(result)
    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return response, result["code"]

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=9001)
