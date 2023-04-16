
const accordionHeaders = document.querySelectorAll('.accordion-header');
accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
        header.classList.toggle('active');
        const accordionBody = header.nextElementSibling;
        if (header.classList.contains('active')) {
            accordionBody.style.display = 'block';
        } else {
            accordionBody.style.display = 'none';
        }
    });
});

