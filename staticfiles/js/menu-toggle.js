function toggleMenu() {
  let menu = document.getElementById("nav");
  if (menu.children[1].style.display === "none") {
      menu.children[1].style.display = "block"; // Show the menu
      menu.parentElement.style.background = "#353634";
  } else {
      menu.children[1].style.display = "none"; // Hide the menu
      menu.parentElement.style.background = "none";
  }
}