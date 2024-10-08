var firestore = null;

function RTEService() {}
RTEService.prototype.initFireStore = function () {
  const firebaseConfig = {
    apiKey: "AIzaSyBge9O5sGrb2j_l6ObY5agDOe-MZaTGlcQ",
    authDomain: "sample-f6d86.firebaseapp.com",
    databaseURL: "https://sample-f6d86-default-rtdb.firebaseio.com",
    projectId: "sample-f6d86",
    storageBucket: "sample-f6d86.appspot.com",
    messagingSenderId: "289813396319",
    appId: "1:289813396319:web:fd5d58a31b7c838e5254ea",
    measurementId: "G-JSY9T2SJDX",
  };
  firebase.initializeApp(firebaseConfig);
  return firebase.firestore();
};

RTEService.prototype.getFirestore = function () {
  //Prevent to initialize firestore each time/
  if (firestore == null) {
    firestore = RTEService.prototype.initFireStore();
  }
  return firestore;
};
const db = RTEService.prototype.getFirestore();
let today = new Date();
db.collection("chats")
  .where("sent_at", ">", today)
  .onSnapshot((snapshot) => {
    snapshot.docChanges().forEach((change) => {
      if (change.type === "added") {
        if (change.doc.data().sender != currentUser) {
          receiveMessage(change.doc.data().sender, change.doc.data().content);
        }
      }
      if (change.type === "modified") {
        console.log("Modified city: ", change.doc.data());
      }
      if (change.type === "removed") {
        console.log("Removed city: ", change.doc.data());
      }
    });
  });
