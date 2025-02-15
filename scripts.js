function fetchResponse() {
    const userInput = document.getElementById("userInput").value;
    if (!userInput.trim()) {
        document.getElementById("response").innerText = "Please enter a query.";
        return;
    }
    document.getElementById("response").innerText = "Fetching response...";
    fetch("https://landmark-backend-95jj4noqx-varshinimanes-projects.vercel.app/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.response || "No response received.";
    })
    .catch(error => {
        document.getElementById("response").innerText = "Error fetching response.";
        console.error("Error:", error);
    });
}
