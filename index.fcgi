#!/usr/bin/node

var fcgi = require('node-fastcgi');

const express = require('express'),
      app = express(),
      http = fcgi.createServer(app),
      sql = require('mysql');

app.get('/', function (req, res) {

//socket.getPeerCertificate()
    if ('SSL_CLIENT_S_DN_Email' in req.socket.params) {
        res.send(req.socket.params.SSL_CLIENT_S_DN_Email);
    } else {
        res.send("no certificate, please visit <a href=\"\">https://minecraft.scripts.mit.edu:444</a>");
    }
//   res.send(JSON.stringify(req.socket.params));//'Hello World');
});

http.listen();

//https.listen(config.HTTPS_PORT);
