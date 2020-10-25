//variables
const button = document.getElementById("button");
const content = document.getElementById("content");
const close = document.getElementById("close");

//Funcion
const showModal = () => {
    if (content.classList.contains("active")) {
        content.classList.remove("active");
    }else {
        content.classList.add("active");
    }
}

//Evento
button.addEventListener('click', showModal);
close.addEventListener('click', showModal);