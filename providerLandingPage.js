document.querySelector('link[rel="icon"]').addEventListener('click', function() {
    window.location.href = "/";
});

const radios = document.querySelectorAll('input[type="radio"]');

radios.forEach(radio => {
    radio.addEventListener('click', function() {
        // Disable all radio buttons on click
        radios.forEach(radio => {
            radio.disabled = true;
        });

        // Enable the selected radio button
        this.disabled = false;
    });
});