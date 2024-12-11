document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-links a');
    const homeLink = document.getElementById('home-link');
    const contentArea = document.getElementById('content-area');

    // Функция для прокрутки наверх
    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Плавная прокрутка
        });
    };

    // Обработчик для главной страницы
    const loadHomePage = () => {
        fetch('/main') // Путь, где хранится файл main.html
            .then(response => response.text())
            .then(html => {
                contentArea.innerHTML = html; // Вставляем новый контент
                scrollToTop(); // Прокручиваем наверх
            })
            .catch(error => {
                console.error('Ошибка при загрузке главной страницы:', error);
                contentArea.innerHTML = '<p>Ошибка при загрузке главной страницы. Попробуйте позже.</p>';
            });
    };

    // Очищаем контент и прокручиваем наверх при клике на логотип
    homeLink.addEventListener('click', (event) => {
        event.preventDefault();
        loadHomePage(); // Загружаем главную страницу через AJAX
    });

    // Обработчик для других ссылок навигации
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const url = link.getAttribute('data-url');

            fetch(url)
                .then(response => response.text())
                .then(html => {
                    contentArea.innerHTML = html; // Вставляем новый контент
                    scrollToTop(); // Прокручиваем наверх
                })
                .catch(error => {
                    console.error('Ошибка при загрузке контента:', error);
                    contentArea.innerHTML = '<p>Ошибка при загрузке контента. Попробуйте позже.</p>';
                });
        });
    });
});
