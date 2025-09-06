function sendFeeling() {
    let feelingInput = document.getElementById("feeling");
    let feeling = feelingInput.value.trim();
    if (!feeling) return;

    // Show user message
    let chatLog = document.getElementById("chat-log");
    let userMsg = document.createElement("div");
    userMsg.textContent = "You: " + feeling;
    userMsg.style.color = "#6A0DAD";
    chatLog.appendChild(userMsg);

    feelingInput.value = "";

    // Send to server
    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ feeling: feeling })
    })
    .then(response => response.json())
    .then(data => {
        let aiMsg = document.createElement("div");
        aiMsg.textContent = "Baby AI: " + data.emotion;
        aiMsg.style.color = "#D269FF";
        chatLog.appendChild(aiMsg);
        chatLog.scrollTop = chatLog.scrollHeight;

        // Show reminder
        document.getElementById("reminder").textContent = "Remember, you are loved and cared for 💜";
    });
}

// Press Enter to send
function checkEnter(e) {
    if (e.key === "Enter") {
        sendFeeling();
    }
}