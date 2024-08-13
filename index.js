const cur_date = Date();

// Will add current date to message
function updateHtml() {
  document.getElementById("message").innerHTML = cur_date;
  document.getElementById("hello").innerHTML = "who?";
}


window.addEventListener("load", updateHtml());

function addUser() {
  console.log("User added");
}
