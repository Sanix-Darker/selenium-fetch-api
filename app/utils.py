# coding: utf-8

from flask import jsonify
import requests
import json

from app.classes.SeleniumScrap import SeleniumScrap


def scrap_html_content(secret_key, selector, url):

    if secret_key is not None and url is not None and selector is not None:
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
                'message': 'some parameters are missing amount:{}, from:{}, to:{} '.format(amount, from_, to_) 
            }
        )

    return response
