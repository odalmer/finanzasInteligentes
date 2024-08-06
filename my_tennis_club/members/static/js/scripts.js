// scripts.js

// Cambia el color de fondo de los botones al pasar el mouse
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".btn");

    buttons.forEach(function(button) {
        button.addEventListener("mouseenter", function() {
            button.style.backgroundColor = "#0056b3";
        });

        button.addEventListener("mouseleave", function() {
            button.style.backgroundColor = "#007bff";
        });
    });
});

// Mostrar alerta al enviar un formulario de contacto
const contactForm = document.querySelector("form");
if (contactForm) {
    contactForm.addEventListener("submit", function(event) {
        event.preventDefault();
        alert("Gracias por tu mensaje. Nos pondremos en contacto contigo pronto.");
        contactForm.submit();
    });
}

document.querySelector('form').addEventListener('submit', function(event) {
    console.log('Form submitted');
});
