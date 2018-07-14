#!/usr/bin/env python

import jsonschema
import json


data = ''
schema = ''

with open('../LongExample_forVerification.txt', 'r') as f:
    data = json.load(f)

print(data)

with open('schema_customized.json', 'r') as f:
    schema = json.load(f)

print(schema)

try:
    jsonschema.validate(data, schema)
except jsonschema.ValidationError as e:
    print('Invalid JSON - {0}'.format(e.message))
