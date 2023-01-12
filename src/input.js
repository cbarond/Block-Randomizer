// var color_picker = document.getElementById("color");
// var color_picker_wrapper = document.getElementById("color-picker-wrapper");

// color_picker.onchange = function() {
// 	color_picker_wrapper.style.backgroundColor = color_picker.value;
// }
// color_picker_wrapper.style.backgroundColor = color_picker.value;
// color_picker_wrapper.style.borderRadius = "10px";

let color_picker = document.querySelectorAll(".colorSelect")
let color_picker_wrapper = document.querySelectorAll(".color-picker-wrapper")

// for (i = 0; i < color_picker_wrapper.length; i++) {
//   console.log(color_picker[i])
//   color_picker.addEventListener("input", () => {
//     color_picker_wrapper[i].style.backgroundColor = color_picker[i].value
//     console.log(color_picker[i].value)
//   })
//   color_picker_wrapper[i].style.backgroundColor = color_picker[i].value
//   color_picker_wrapper[i].style.borderRadius = "10px"
// }

color_picker.forEach((color, index) => {
  let wrapper = color_picker_wrapper[index]
  color.addEventListener("input", () => {
    wrapper.style.backgroundColor = color.value
    wrapper.style.border = "none"
  })
})

// TODO Add configurable number of options