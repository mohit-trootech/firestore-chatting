//Gets the text from the input box and processes it
function getResponse(userText) {
  const mainChatElem = document.getElementById("main-chat-container");

  userText = userText != null ? userText : $("#textInput").val();
  if (userText != "") {
    let userHtml = `
<div class="chat chat-end userText">
  <div class="chat-image avatar">
      <div class="w-10 rounded-full">
          <img alt="" src="${currentUserProfilePicture}" />
      </div>
    </div>
  <div class="chat-header capitalize">
      <a href="/accounts/${currentUser}">${currentUser}</a>
      <time class="text-xs opacity-50">${getTime()}</time>
  </div>
  <div class="chat-bubble">${userText}</div>
  <div class="chat-footer opacity-50">Delivered</div>
</div>
`;
    postRequest(chatAjaxUrl, {
      userText: userText,
    });
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
  }
}

function sendButton() {
  getResponse(null);
}

function heartButton() {
  getResponse("Heart clicked!");
}
function chatSend(event) {
  if (event.code == "Enter") {
    getResponse(null);
  }
}
$(document).ready(function () {
  /*Update User Online Status */
  $("#updateStatus").change(() => {
    getRequest(chatAjaxUrl, {
      requestType: "updateStatus",
    });
    updateOnlineUsers();
  });
  function updateOnlineUsers() {
    /*Update User Online List */
    if (userOnlineList) {
      getRequest(
        chatAjaxUrl,
        {
          requestType: "onlineUsers",
        },
        updateOnlineUsersContent
      );
    }
  }
  setInterval(() => {
    updateOnlineUsers();
  }, 120000);
});
