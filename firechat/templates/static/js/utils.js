/*Utility Scripts */
function loadJs(content) {
  eval(content);
}
/*Get Chat Time in Required Format */
function getTime() {
  let today = new Date();
  hours = today.getHours();
  minutes = today.getMinutes();

  if (hours < 10) {
    hours = "0" + hours;
  }

  if (minutes < 10) {
    minutes = "0" + minutes;
  }

  let time = hours + ":" + minutes;
  return time;
}

function toggleFollowingFollower(event) {
  event.preventDefault();
  const elem = event.target;
  const user = elem.id.split("-")[1];
  elem.innerText = elem.innerText == "Following" ? "Follow" : "Following";
  getRequest(chatAjaxUrl, {
    user: user,
    requestType: "updateFriendsList",
  });
}

function updateOnlineUsersContent(content) {
  userOnlineList.innerHTML = content.page;
}
/*Gets the Chat Messages */
function receiveMessage(sender, responseText) {
  let responseHTML = `
  <div class="chat chat-start botText">
                        <div class="chat-header capitalize">
                           <a href="/accounts/${sender}"> ${sender}</a>
                            <time class="text-xs opacity-50">${getTime()}</time>
                        </div>
                        <div class="chat-bubble">${responseText}</div>
                    </div>`;
  $("#chatbox").append(responseHTML);
  document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

$(document).ready(() => {
  /*Scroll to Bottom of Chat Application */
  const elems = $(".chat");
  if (elems.length > 1) {
    elems[elems.length - 1].scrollIntoView(true);
  }
});
