const cur_date = Date()

function updateHtml() {
    document.getElementById("message").innerHTML = cur_date;

    console.log("Hello world");
    document.getElementById("hello").innerHTML = "who?";
}

updateHtml();


function addUser() {
    console.log("User added");
}