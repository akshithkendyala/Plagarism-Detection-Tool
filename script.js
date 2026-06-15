async function checkSimilarity() {

    let file1 = document.getElementById("file1").files[0];
    let file2 = document.getElementById("file2").files[0];

    if (!file1 || !file2) {
        alert("Please select both files.");
        return;
    }

    let formData = new FormData();

    formData.append("file1", file1);
    formData.append("file2", file2);

    try {

        let response = await fetch(
            "http://127.0.0.1:5000/check",
            {
                method: "POST",
                body: formData
            }
        );

        let data = await response.json();

        // Show Result
        document.getElementById("result").innerHTML =
            `Similarity: ${data.similarity}% | Risk: ${data.risk}`;

        // Save latest score for dashboard
        localStorage.setItem(
            "lastScore",
            data.similarity
        );

        // Save history
        let history =
            JSON.parse(
                localStorage.getItem("history")
            ) || [];

        history.push({
            similarity: data.similarity,
            risk: data.risk,
            date: new Date().toLocaleString()
        });

        localStorage.setItem(
            "history",
            JSON.stringify(history)
        );

    } catch (error) {

        console.error(error);

        alert(
            "Error connecting to backend. Make sure Flask server is running."
        );
    }
}


// Download Report
function downloadReport() {

    let result =
        document.getElementById("result").innerText;

    if (result === "") {
        alert("Please run plagiarism check first.");
        return;
    }

    let report =
        "PLAGIARISM DETECTION REPORT\n";
    report += "===========================\n\n";
    report += result + "\n\n";
    report +=
        "Generated On: " +
        new Date().toLocaleString();

    let blob =
        new Blob(
            [report],
            { type: "text/plain" }
        );

    let link =
        document.createElement("a");

    link.href =
        URL.createObjectURL(blob);

    link.download =
        "plagiarism_report.txt";

    link.click();
}