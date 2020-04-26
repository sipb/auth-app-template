#!/usr/bin/python3
from cgi import FieldStorage
from json import dumps, loads
import os

args = FieldStorage()

error = 'Status: 200 OK\n'
content = 'Content-Type: text/html\n\n'

output = None
if 'SSL_CLIENT_S_DN_Email' in os.environ:
  output = { "kerb" : os.environ['SSL_CLIENT_S_DN_Email'] }
  # add to database or something more fancy, probably create a password, do fancy checks and stuff
else:
  error = 'Status: 401 Unauthorized\n'
  # click this link -- whatever you're at now plus https and :444
  # e.g. res.send("no certificate, please visit https://minecraft.scripts.mit.edu:444");

print(error + content)
print(dumps(output))
