# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 19:21:15 2018

@author: antony.s.pavlenko
"""

import json
from os import listdir

schemas = {}
endpoints = {}
PATH_TO_SCHEMAS = "./schemas"
EXTENSION = 'json'

def addSchema(name):
    plural_name = name + "s"
    
    json1_file = open(PATH_TO_SCHEMAS + '/' + name + '.' + EXTENSION)
    json1_str = json1_file.read()
    schema = json.loads(json1_str)
    
    schemas[plural_name] = schema
    endpoints[plural_name] = {
            'item_title': name,
            'schema' : schemas[plural_name]
            }
    
def getDomainSetting():
    result = {}
    for i, ep in enumerate(endpoints):
        result[ep] = endpoints[ep]
    return result

def loadAllSchemas():
    for f in listdir(PATH_TO_SCHEMAS):
        name = f.split(".")[0]
        addSchema(name)