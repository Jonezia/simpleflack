function changedisplayname() {
  var displayname = prompt("Choose a display name: ");
  if (displayname == "") {
    alert("Your display name cannot be blank");
    changedisplayname();
  } else {
  localStorage.setItem("displayname",displayname);
  document.getElementById("displayname").innerHTML = localStorage.getItem("displayname");
};
}

document.addEventListener('DOMContentLoaded', () => {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  if (localStorage.getItem("displayname") == null ||
  localStorage.getItem("displayname") == "") {
    changedisplayname();
  } else {
    document.getElementById("displayname").innerHTML = localStorage.getItem("displayname");
  };

  socket.on('connect', () => {

    document.getElementById("channelsplus").onclick = () => {
      var channelname = prompt("Choose a channel name: ");
      socket.emit('new channel', channelname);
    };
  });

  socket.on('update channels', () => {
    location.reload();
  });

});
