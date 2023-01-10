// Variables
const colorSelect = document.querySelectorAll(".colorSelect")
const quantityInput = document.querySelectorAll(".quantityInput")
const nameInput = document.querySelectorAll(".nameInput")
const rows = document.getElementById("rows")
const columns = document.getElementById("columns")
const printButton = document.querySelector("[data-print]")

var canvas = document.getElementById("mainCanvas")
var context = canvas.getContext("2d")

let colors = []
let names = []
let currentQuantity = []
let numOfItems = 0

// Functions
function setup() {
    colors = []
    names = []
    currentQuantity = []
    numOfItems = 0
  for (i = 0; i < quantityInput.length; i += 1) {
    if (quantityInput[i].value > 0) {
      currentQuantity[numOfItems] = quantityInput[i].value
      colors[numOfItems] = colorSelect[i].value
      names[numOfItems] = nameInput[i].value
      numOfItems += 1
    }
  }
  console.log(numOfItems, colors, currentQuantity, names)
  return numOfItems
}

// Event Listeners
printButton.addEventListener("click", () => {
    setup()
    context.clearRect(0, 0, canvas.width, canvas.height);
  var x = 0
  var y = 0
  console.log(rows.value, columns.value)
  for (i = 0; i < colors.length; i += 1) {
    console.log(
      colors[i],
      currentQuantity[i],
      names[i]
    )
    console.log(`X1: ${x}    Y1: ${y}`)
    if (x < 450) {
      context.fillStyle = `${colors[i]}`
      context.fillRect(x, y, 150, 150)
      x += 150
    } else {
      x = 0
      y += 150
      context.fillStyle = `${colors[i]}`
      context.fillRect(x, y, 150, 150)
      x += 150
    }
  }
})
