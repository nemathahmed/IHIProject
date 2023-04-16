
const accordionHeaders = document.querySelectorAll('.accordion-header');
accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
        header.classList.toggle('active');
        const accordionBody = header.nextElementSibling;
        if (header.classList.contains('active')) {
            accordionBody.style.display = 'block';
            accordionBody.style.border = '15px solid #9296F3';
        } else {
            accordionBody.style.display = 'none';
            accordionBody.style.border = '15px solid #9296F3';
        }
    });
});

const button = document.querySelector('.rounded-button');
button.addEventListener('click', function() {
    //TODO: integration
});


