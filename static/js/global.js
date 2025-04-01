// Функция для закрытия всех открытых выпадающих меню
function closeAllDropdowns() {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
        dropdowns[i].classList.remove('show');
    }
}

// Обработчик клика для выпадающих меню
document.querySelectorAll('.dropbtn').forEach(function(btn) {
    btn.addEventListener('click', function(event) {
        event.preventDefault();
        var dropdownContent = this.nextElementSibling;

        // Закрываем все открытые меню
        closeAllDropdowns();

        // Открываем текущее меню
        dropdownContent.classList.toggle('show');
    });
});

// Закрытие выпадающих меню при клике вне их области
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        closeAllDropdowns();
    }
}

// JavaScript для модальных окон (логин и выход)
document.getElementById('loginBtn').addEventListener('click', function(event) {
    event.preventDefault();
    alert('Login modal will appear here.');
    // Реализуйте модальное окно для входа
});

document.getElementById('logoutBtn').addEventListener('click', function(event) {
    event.preventDefault();
    if (confirm('Are you sure you want to logout?')) {
        alert('User logged out.');
        // Реализуйте функциональность выхода
    }
});