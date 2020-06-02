# coding: utf-8

from flask import jsonify
import requests
import json

import base64

from app.classes.SeleniumScrap import SeleniumScrap
from app.settings import SECRET_KEY



def scrap_html_content(secret_key, selector, url):
    """
    This method will take as parameters a secret confidential key, a selector 
    and a url as parameters and give back the html content from the url -> selector

    :secret_key a specific secret_key
    :selector a specific The base_64 selector to scrap in the whole web-page
    :url the target url of the webpage, we want to scrap
    """

    if secret_key is not None and url is not None and selector is not None:

        if secret_key == SECRET_KEY:

            s = SeleniumScrap(selector) # //span[@class='converterresult-toAmount']
            result = s.fetch(url)

            response = jsonify(
                {
                    'status':'success',
                    'result': result
                }
            )
        else:
            response = jsonify(
                {
                    'status':'error',
                    'message': 'there is an error with the secret-key, check it again!' 
                }
            )   
    else:
        response = jsonify(
            {
                'status':'error',
                'message': 'some parameters are missing amount:{}, from:{}, to:{} '.format(amount, from_, to_) 
            }
        )

    return response


def b64_encode(data):
    """
    A simple base64 encoder
    
    """
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    return str(encodedBytes, "utf-8")

def b64_decode(data):
    """
    A simple base64 decoder

    """
    message_bytes = base64.b64decode(data.encode('ascii'))
    return message_bytes.decode('ascii')
