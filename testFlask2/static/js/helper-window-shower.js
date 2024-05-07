let currentBranchId = null; // Глобальная переменная для хранения текущего branch_id

document.addEventListener('DOMContentLoaded', function() {
    const listInfoItems = document.querySelectorAll('.listInfo li .list-info-item');

    listInfoItems.forEach(function(item) {
        item.addEventListener('click', function(event) {
            event.preventDefault(); // Предотвращаем переход по ссылке по умолчанию
            const branchId = this.parentElement.dataset.branchId; // Получаем branchId из родительского элемента <li>
            loadChat(branchId);
            currentBranchId = branchId; // Сохраняем текущий branch_id
        });
    });

    function loadChat(branchId) {
        fetch(`/get_messages_helper?branch_id=${branchId}`)
            .then(response => response.text())
            .then(html => {
                const chatbox = document.getElementById('chatbox');
                chatbox.innerHTML = html;
            })
            .catch(error => console.error('Ошибка при загрузке сообщений:', error));
    }
});

function updateChatbox(branchId) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", `/get_messages_helper?branch_id=${branchId}`, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            document.getElementById("chatbox").innerHTML = xhr.responseText;
        }
    };
    xhr.send();
}


// Обновляем чат при загрузке страницы
window.onload = function() {
    // Предположим, что у вас есть начальное значение branchId
    const initialBranchId = "1"; // Замените это на ваше начальное значение branchId
    updateChatbox(initialBranchId);
    currentBranchId = initialBranchId; // Сохраняем начальное значение branch_id
};

// Обновляем чат каждые 5 секунд с использованием сохраненного branch_id
setInterval(function() {
    if (currentBranchId) {
        updateChatbox(currentBranchId);
    }
}, 5000);
