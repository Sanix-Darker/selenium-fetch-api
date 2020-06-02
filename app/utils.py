# coding: utf-8

import base64

from app.classes.SeleniumScrap import SeleniumScrap
from app.settings import SECRET_KEY

import sys, traceback


def get_trace():
    print("-"*60)
    traceback.print_exc(file=sys.stdout)
    print("-"*60)


def scrap_html_content(secret_key, selector, url):
    """
    This method will take as parameters a secret confidential key, a selector 
    and a url as parameters and give back the html content from the url -> selector

    :secret_key a specific secret_key
    :selector a specific The base_64 selector to scrap in the whole web-page
    :url the target url of the webpage, we want to scrap
    """

    if secret_key is not None and url is not None and selector is not None:
        secret_key = b64_decode(secret_key)
        url = b64_decode(url)
        selector = b64_decode(selector)

        if secret_key == SECRET_KEY:
            try:
                s = SeleniumScrap(selector) # //span[@class='converterresult-toAmount']
                result = s.get(url)

                response = {
                    'status':'success',
                    'code': 200,
                    'result': result
                }
            except Exception:
                get_trace()
                response = {
                    'status':'error',
                    'code': 500,
                    'message': 'Something went wrong in the server, check logs !' 
                }
        else:
            response = {
                'status':'error',
                'code': 400,
                'message': 'There is an error with the secret-key, check it again!' 
            }
    else:
        response = {
            'status':'error',
            'code': 400,
            'message': 'some parameters are missing secret_key:{}, url:{}, selector:{} '.format(secret_key, url, selector) 
        }

    return response


def b64_encode(data):
    """
    A simple base64 encoder
    
    """
    encodedBytes = base64.b64encode(data.encode('utf-8'))
    return encodedBytes.decode('utf-8')

def b64_decode(data):
    """
    A simple base64 decoder

    """
    message_bytes = base64.b64decode(data)
    return  message_bytes.decode('utf-8')
