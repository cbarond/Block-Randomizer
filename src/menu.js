const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
})

// window.onload = function startup() {
//     alert("This project is a work in progress and may have bugs.\n\nInstructions:");
// }