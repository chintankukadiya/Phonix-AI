function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        // Add user message to chat content
        const chatContent = document.getElementById("chat-content");
        chatContent.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

        // Clear the input field
        document.getElementById("user-input").value = "";

        // Make a POST request to Flask backend (change the URL after deployment)
        fetch('https://phonix-ai-backend.onrender.com', {  // Replace with your Render backend URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            const assistantResponse = data.response;  // Get the AI response from the server
            chatContent.innerHTML += `<p><strong>AI Assistant:</strong> ${assistantResponse}</p>`;

            // Scroll to the bottom of the chat
            chatContent.scrollTop = chatContent.scrollHeight;
        })
        .catch(error => {
            console.error("Error:", error);
            chatContent.innerHTML += `<p><strong>AI Assistant:</strong> Oops, something went wrong!</p>`;
        });
    }
}
