async function loginUser(){

    let username =
        document.getElementById("username").value;

    let password =
        document.getElementById("password").value;

    let formData = new FormData();

    formData.append("username", username);
    formData.append("password", password);

    let response = await fetch(
        "http://127.0.0.1:5000/login",
        {
            method: "POST",
            body: formData
        }
    );

    let data = await response.json();

    if(data.success){

        alert("Login Successful");

        window.location.href = "upload.html";

    } else {

        alert("Invalid Username or Password");
    }
}