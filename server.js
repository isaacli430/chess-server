var app = require('express')();
var express = require('express');
var server = require('http').Server(app);
var io = require('socket.io')(server);

app.use(express.static('public'));
app.listen(5000);
server.listen(8080);
// process.on('uncaughtException', function (exception) { });

io.on('connection', function (socket) {
  socket.emit("connected");
  let room = socket.handshake.query.room;
  // socket.on('autoLogin', function (data) {
  //   socket.emit('refreshedFriends', { friends: reply });
  // });
});