// Function to display the dropdown content when the input box is clicked
document.getElementById("inputBox").addEventListener("click", function() {
  document.getElementById("dropdownContent").style.display = "block";
});

// Function to select an option and fill the input box with the selected value
function selectOption(option) {
  document.getElementById("inputBox").value = option;
  document.getElementById("dropdownContent").style.display = "none";
}
