// Variables
const colorSelect = document.querySelectorAll(".colorSelect")
const quantityInput = document.querySelectorAll(".quantityInput")
const nameInput = document.querySelectorAll(".nameInput")
const rows = document.getElementById("rows")
const columns = document.getElementById("columns")
const corners = document.getElementById("corners")
const generateButton = document.querySelector("[data-generate]")

var canvas = document.getElementById("mainCanvas")
var context = canvas.getContext("2d")

let colors = []
let names = []
let currentQuantity = []
let numOfItems = 0
let blockSizeByCol
let blockSizeByRow
let blockSize
let grid = []
let viable = true

// Functions
function containsOnlyNumbers(str) {
  return /^[0-9]+$/.test(str)
}

function checkForDuplicates(array) {
  return new Set(array).size !== array.length
}

function setup() {
  // Reset variables
  colors = []
  names = []
  currentQuantity = []
  numOfItems = 0
  grid = []
  viable = true

  for (i = 0; i < quantityInput.length; i += 1) {
    console.log(
      containsOnlyNumbers(quantityInput[i].value),
      quantityInput[i].value
    ) // Console.log
    if (quantityInput[i].value != "") {
      if (containsOnlyNumbers(quantityInput[i].value)) {
        currentQuantity[numOfItems] = parseFloat(quantityInput[i].value)
      } else {
        currentQuantity[numOfItems] = NaN
      }
      colors[numOfItems] = colorSelect[i].value
      names[numOfItems] = nameInput[i].value
      numOfItems += 1
    }
  }
  console.log(numOfItems, colors, currentQuantity, names) // Console.log
}

function computeSize() {
  width = 400
  height = 850
  blockSizeByCol = Math.floor(width / columns.value)
  blockSizeByRow = Math.floor(height / rows.value)
  blockSize = Math.min(blockSizeByCol, blockSizeByRow)
  console.log(`Block Size: ${blockSize}px`) // Console.log
}

function checkViability() {
  // Check Numbers
  if (currentQuantity.includes(NaN)) {
    alert("Please make sure quantities are only positive numbers.")
    viable = false
  }

  // Check if there are enough options
  if (
    (corners.checked && numOfItems < 2) ||
    (!corners.checked && numOfItems < 5)
  ) {
    alert("Please add more options.")
    viable = false
  }

  // Check if colors are unique
  if (checkForDuplicates(colors)) {
    alert("Please make sure all colors are unique.")
    viable = false
  }

  // Check block size
  if (blockSize == 0) {
    alert("Please reduce the number of rows and/or columns.")
    viable = false
  }
}

function createGrid() {
  for (i = 0; i < rows.value; i++) {
    grid[i] = new Array(parseFloat(columns.value))
  }
  console.log(`Rows: ${grid.length} \nCols: ${grid[0].length}`) // Console.log
  canvas.width = blockSize * columns.value
  canvas.height = blockSize * rows.value

  console.log(`Corners: ${corners.checked} \nViable: ${viable}`) // Console.log
  if (viable) {
    for (i = 0; i < grid.length; i++) {
      for (j = 0; j < grid[0].length; j++) {
        let above = -1
        let left = -1
        let topLeft = -1
        let topRight = -1
        if (i - 1 >= 0) {
          above = grid[i - 1][j]
        }
        if (j - 1 >= 0) {
          left = grid[i][j - 1]
        }
        if (i - 1 >= 0 && j - 1 >= 0) {
          topLeft = grid[i - 1][j - 1]
        }
        if (i - 1 >= 0 && j + 1 >= 0) {
          topRight = grid[i - 1][j + 1]
        }
        let neighbors = [above, left, -1]
        if (!corners.checked) {
          neighbors = [above, left, topLeft, topRight, -1]
        }
        index = getRandomInt(0, numOfItems)
        grid[i][j] = colors[index]
        while (neighbors.includes(grid[i][j]) == true && viable) {
          index = getRandomInt(0, numOfItems)
          grid[i][j] = colors[index]
        }
      }
    }
  }
}

function drawGrid() {
  for (i = 0; i < grid.length; i++) {
    for (j = 0; j < grid[0].length; j++) {
      var x = j * blockSize
      var y = i * blockSize
      context.fillStyle = `${grid[i][j]}`
      context.fillRect(x, y, blockSize, blockSize)
    }
  }
}

function getRandomInt(min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min) + min) // The maximum is exclusive and the minimum is inclusive
}

// Event Listeners
generateButton.addEventListener("click", () => {
  setup()
  computeSize()
  checkViability()
  createGrid()
  context.clearRect(0, 0, canvas.width, canvas.height)
  drawGrid()

  //   context.fillRect(0, 0, canvas.width, canvas.height)

  //   var x = 0
  //   var y = 0
  //   console.log(rows.value, columns.value)
  //   for (i = 0; i < colors.length; i += 1) {
  //     console.log(colors[i], currentQuantity[i], names[i])
  //     console.log(`X1: ${x}    Y1: ${y}`)
  //     if (x < 450) {
  //       context.fillStyle = `${colors[i]}`
  //       context.fillRect(x, y, 150, 150)
  //       x += 150
  //     } else {
  //       x = 0
  //       y += 150
  //       context.fillStyle = `${colors[i]}`
  //       context.fillRect(x, y, 150, 150)
  //       x += 150
  //     }
  //   }
})
