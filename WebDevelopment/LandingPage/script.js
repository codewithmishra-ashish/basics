


document.addEventListener("DOMContentLoaded", function() {
    const icon = document.querySelector('.open');
    const navMenu = document.querySelector('.nav-link');

    icon.addEventListener('click', function() {
        navMenu.classList.toggle('open');
    });

    window.addEventListener('scroll', function() {
        const nav = document.querySelector('nav');
        nav.classList.toggle('sticky', window.scrollY > 0);
    });
});