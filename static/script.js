
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

// Display messages in the chat window
function addMessage(message, className) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add(className);

    messageDiv.textContent = message;

    chatBox.appendChild(messageDiv);

    // Automatically scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}


// Send message to Flask backend
async function sendMessage() {

    const message = userInput.value.trim();

    // Don't send empty messages
    if (message === "") {
        return;
    }

    // Display user's message
    addMessage(message, "user-message");

    userInput.value = "";

    sendBtn.disabled = true;

    try {

        // Send message to Flask
        const response = await fetch("/get", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                msg: message
            })

        });

        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }

        const data = await response.json();

        // Display chatbot response
        addMessage(data.response, "bot-message");

    }

    catch (error) {

        console.error("Error:", error);

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot-message"
        );

    }

    finally {

        sendBtn.disabled = false;

        userInput.focus();

    }

}


// Send message when Enter is pressed
userInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});
