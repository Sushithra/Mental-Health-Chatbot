const chatBody = document.getElementById("chatBody");
const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");

function addMessage(message, isBot = false) {
  const messageDiv = document.createElement("div");
  messageDiv.className = isBot ? "bot-message" : "user-message";
  messageDiv.textContent = message;
  chatBody.appendChild(messageDiv);
  chatBody.scrollTop = chatBody.scrollHeight;
}

function handleUserMessage() {
  const userMessage = userInput.value.trim();
  if (userMessage) {
    addMessage(userMessage, false);
    userInput.value = "";

    // Fetch bot response
    fetch("/get-response", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userMessage }),
    })
      .then((response) => response.json())
      .then((data) => {
        addMessage(data.bot_message, true);
      })
      .catch((error) => {
        addMessage("Oops! Something went wrong. Please try again later.", true);
      });
  }
}

sendButton.addEventListener("click", handleUserMessage);
userInput.addEventListener("keypress", (event) => {
  if (event.key === "Enter") handleUserMessage();
});
