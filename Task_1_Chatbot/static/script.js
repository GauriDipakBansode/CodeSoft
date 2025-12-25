function sendMessage(){
    let inputBox = document.getElementById("user-input");
    let message = inputBox.value;

    if(message === ""){
        return;
    }

    fetch("/chat", {
        method: "Post",
        headers: {
            "Content-Type": "application/json"
        }, 
        body: JSON.stringify({ message: message })
    })

    .then(response => response.json())
    .then(data => {
        let chatBox = document.getElementById("chat-box");
        chatBox.innerHTML += "<p><b>You:</b>" + message +"</p";
        chatBox.innerHTML += "<p><b>Bot:</b>" + data.reply + "</p>";

    });


    inputBox.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

   
}