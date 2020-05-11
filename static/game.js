window.socket = io.connect('http://localhost:8080/game?room=' + $("#room").content);
socket.on("connected", function () {
    alert("ok");
});