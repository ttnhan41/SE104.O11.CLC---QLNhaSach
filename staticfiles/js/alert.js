let alertWrapper = document.querySelectorAll('.alert');
let alertClose = document.querySelectorAll('.alert__close');

for (let i = 0; i < alertWrapper.length; i++) {
  let button = alertClose[i]
  button.onclick = function(event) {
      let buttonClicked = event.target;
      buttonClicked.parentElement.remove();
      return false;
  }
}