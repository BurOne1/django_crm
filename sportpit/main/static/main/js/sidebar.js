document.addEventListener('DOMContentLoaded', function() {
    // Получаем текущий путь URL
    var currentPath = window.location.pathname;

    // Находим все ссылки в боковой панели
    var sidebarLinks = document.querySelectorAll('.nav-link');

    // Проходимся по каждой ссылке
    sidebarLinks.forEach(function(link) {
        // Получаем путь URL из атрибута href
        var linkPath = link.querySelector('a').getAttribute('href');

        // Сравниваем текущий путь с путем ссылки
        if (currentPath === linkPath) {
            // Если совпадает, добавляем класс для подсветки текста и иконки
            link.classList.add('active-link');
        }
    });
});