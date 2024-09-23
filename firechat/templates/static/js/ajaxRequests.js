/*Post Request */
function postRequest(url, data, callback) {
  ajaxCall("POST", url, data, callback);
}

/*Get Request */
function getRequest(url, data, callback) {
  ajaxCall("GET", url, data, callback);
}

/*Ajax Call */
function ajaxCall(type, url, data, callback) {
  $.ajax({
    url: url,
    type: type,
    data: data,
    headers: {
      "X-CSRFToken": csrfToken,
    },
    success: function (response, status, xhr) {
      // console.log(response);
      // console.log(xhr);
      if (xhr.status != 204) {
        if (callback) {
          callback(response);
        }
      }
    },
    error: function (xhr, status, error) {
      console.error("Error occurred:", xhr.responseText, status, error);
    },
  });
}
