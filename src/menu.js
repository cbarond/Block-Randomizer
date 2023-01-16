const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
})

let instructions = `This project is a work in progress and may have bugs.\n
Instructions:
- Insert how many rows and columns you want
- Select whether you want corners of the same color to touch
- For each item you want, fill in a color, quantity, and name
- Press the "Generate" button to create the grid\n
Notes:
- You don't need to fill in all the slots for items, only what you need.
- It may not create a proper grid the first time. Check your quantities and try running it a few more times.`

window.onload = function startup() {
    alert(instructions);
}