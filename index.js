const cur_date = Date();

// Will add current date to message
function updateHtml() {
  document.getElementById("message").innerHTML = cur_date;

  console.log("Hello world");
  document.getElementById("hello").innerHTML = "who?";
}

updateHtml();

function addUser() {
  console.log("User added");
}

function getUserLastName() {
  return "LAST NAME";
}
