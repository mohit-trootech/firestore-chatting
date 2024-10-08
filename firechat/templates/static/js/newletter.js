/*Newsletter Subscribtion Handling Ajax */
$(document).ready(() => {
  /*Newsletter Subscribtion Handling Ajax */
  $("#newsletter-form").submit((event) => {
    event.preventDefault();
    email = event.target.querySelector('[name="subscribe"]').value;
    postRequest(newsletterUrl, {
      email: email,
    });
    event.target.querySelector('[name="subscribe"]').value = "";
  });
});
