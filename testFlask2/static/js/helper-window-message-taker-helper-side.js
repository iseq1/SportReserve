
function sendMessage() {
    var message = document.getElementById("user-message").value;
    var branchId = document.getElementById("branch-id").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit_message_helper", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            updateChatbox(); // После успешной отправки сообщения обновляем чат
        }
    };
    xhr.send(JSON.stringify({message: message, branchId: branchId}));
}

function updateChatbox() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_messages_helper", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            document.getElementById("chatbox").innerHTML = xhr.responseText;
        }
    };
    xhr.send();
}

document.getElementById("send-btn").addEventListener("click", function() {
    sendMessage();
});

// Обновляем чат при загрузке страницы
window.onload = function() {
    updateChatbox();
};


// Обновляем чат каждые 5 секунд
setInterval(updateChatbox, 5000);