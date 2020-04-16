#!/usr/bin/python3
from cgi import FieldStorage
from json import dumps, loads
import os

args = FieldStorage()

error = 'Status: 400 Bad Request\n'
content = 'Content-Type: application/json\n\n'

if 'SSL_CLIENT_S_DN_Email' in os.environ:
  print(os.environ['SSL_CLIENT_S_DN_Email'])
  # add to database or something more fancy, probably create a password, do fancy checks and stuff
else:
  # click this link -- whatever you're at now plus https and :444
  # res.send("no certificate, please visit https://minecraft.scripts.mit.edu:444");
  pass

output = {}
# if 'kerb' not in args:
#     output = {"error": "kerb was not specified"}
#     print(error + content)
#     print(dumps(output))
# else:
#     output = {"access-key": "hunter2"}

print(error + content)
print(dumps(output))
