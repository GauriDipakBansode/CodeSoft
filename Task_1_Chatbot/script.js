function sendMessage(){
    let inputBox = document.getElementById("user-input");
    let message = inputBox.ariaValueMax;

    if(message === ""){
        return;
    }

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user">You: ${message}</div>`;


    let botReply = "This is a rule-based chatbot UI";

    chatBox.innerHTML += `<div class="bot">Bot: ${botReply}</div>`;


    inputBox.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

   
}