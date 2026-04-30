let currentScenario = "";

function selectScenario(scenario) {
    currentScenario = scenario;
    document.getElementById("chat").innerHTML += 
        `<p><b>System:</b> You selected ${scenario}</p>`;
}

async function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value;

    if (message === "") return;

    if (currentScenario === "") {
        alert("Please select a scenario first!");
        return;
    }

    document.getElementById("chat").innerHTML += 
        `<p><b>You:</b> ${message}</p>`;

    input.value = "";

    try {
        let response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                message: message,
                scenario: currentScenario
            })
        });

        let data = await response.json();

        document.getElementById("chat").innerHTML += 
            `<p><b>AI:</b> ${data.reply}</p>
             <p style="color: lightgreen;"><b>Feedback:</b> ${data.feedback}</p>`;

    } catch (error) {
        document.getElementById("chat").innerHTML += 
            `<p><b>Error:</b> Backend not connected</p>`;
    }
}