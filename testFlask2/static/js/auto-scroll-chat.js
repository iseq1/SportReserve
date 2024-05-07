function scrollChatToBottom() {
    var chatbox = document.getElementById("chatbox");
    chatbox.scrollTop = chatbox.scrollHeight - chatbox.clientHeight;
}


document.addEventListener("DOMContentLoaded", function() {
    scrollChatToBottom();
});
