const cur_date = Date();

// Will add current date to message
function updateHtml() {
  document.getElementById("message").innerHTML = cur_date;
  document.getElementById("hello").innerHTML = "who?";
}

function addUser() {
  console.log("User added");
  return "OK"
}


module.exports = { addUser, updateHtml }