#!/usr/bin/python3
from cgi import FieldStorage
from json import dumps, loads

args = FieldStorage()

error = 'Status: 400 Bad Request\n'
content = 'Content-Type: application/json\n\n'

if 'kerb' not in args:
    output = {"error": "kerb was not specified"}
    print(error + content)
    print(dumps(output))
else:
    output = {"access-key": "hunter2"}

print(error + content)
print(dumps(output))
