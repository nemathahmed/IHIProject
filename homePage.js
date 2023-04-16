const icon = document.getElementById('icon');
icon.src = 'static/diapredict/icon.png';

const button = document.getElementById('get-started-button');
const buttonsContainer = document.getElementById('category-button-container');
button.addEventListener('click', () => {
    buttonsContainer.style.display = 'block';
    button.style.display = 'none';
});

const patientButton = document.getElementById('patient-button');
patientButton.addEventListener('click', () => {
    console.log('patient button is clicked');
})
const providerButton = document.getElementById('provider-button');
providerButton.addEventListener('click', () => {
    console.log('provider button is clicked');
})