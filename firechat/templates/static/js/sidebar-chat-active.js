$(document).ready(() => {
  $(".chat-navigation").click((elem) => {
    const liElem = elem.target.closest("li");
    removeSidebarActiveClass();
    liElem.classList.add("active");
  });
});

function removeSidebarActiveClass() {
  const charBarElems = document.getElementsByClassName("chat-navigation");
  Array.from(charBarElems).forEach((elem) => {
    elem.classList.remove("active");
  });
}
