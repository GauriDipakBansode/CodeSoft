function getRecommendations() {
    const userId = document.getElementById("userIdInput").value;

    if (!userId) {
        alert("Please enter a user ID.");
        return;
    }

    fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: userId })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById("result");

        if (!data.recommendations || data.recommendations.length === 0) {
            resultDiv.innerHTML = "<p>No recommendations found for this user.</p>";
            return;
        }

        let output = "<h3>Recommended products:</h3><ul>";
        data.recommendations.forEach(item => {
            output += `<li>Product ID: ${item}</li>`;
        });
        output += "</ul>";
        resultDiv.innerHTML = output;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = `<p style="color:red;">Error: ${error.message || 'Something went wrong.'}</p>`;
    });
}
