# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:16:26 2018

@author: antony.s.pavlenko
"""

from eve import Eve
from flask import send_from_directory

app = Eve(__name__, static_folder="")

@app.after_request
def after(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':   
    app.run(host='0.0.0.0', threaded=True)