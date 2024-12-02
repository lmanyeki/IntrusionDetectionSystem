
  // Handle file upload
document.getElementById("uploadButton").addEventListener("click", () => {
    const fileInput = document.getElementById("fileInput");
    if (fileInput.files.length === 0) {
        alert("Please select a file!");
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = (e) => {
        try {
            const data = e.target.result;
            const parsedData = parseCSV(data);
            displayData(parsedData);
        } catch (error) {
            alert("Error parsing the CSV file. Please check the file format.");
            console.error("CSV Parsing Error:", error);
        }
    };

    reader.onerror = () => {
        alert("Error reading the file. Please try again.");
        console.error("File Read Error:", reader.error);
    };

    reader.readAsText(file);
});

// Parse CSV data
function parseCSV(data) {
    const rows = data.split("\n").filter((row) => row.trim() !== ""); // Remove empty rows
    return rows.map((row) => row.split(",")); // Split rows into cells
}


// Display uploaded data in a table
function displayData(data) {
    const tableBody = document.querySelector("#dataTable tbody");
    tableBody.innerHTML = ""; // Clear previous data

    data.forEach((row, index) => {
        if (index === 0) return; // Skip header

        const tr = document.createElement("tr");

        row.forEach((cell, cellIndex) => {
            const td = document.createElement("td");
            td.textContent = cell;

            // Assuming the last column represents the threat level
            if (cellIndex === row.length - 1) {
                td.classList.add(getThreatClass(cell.trim()));
            }

            tr.appendChild(td);
        });

        tableBody.appendChild(tr);
    });
}

// Add color-coding classes based on threat level
function getThreatClass(threat) {
    switch (threat.toLowerCase()) {
        case "high":
            return "threat-high";
        case "medium":
            return "threat-medium";
        case "low":
            return "threat-low";
        default:
            return ""; // No class for unknown threats
    }
}

// Handle real-time analysis
document.getElementById("analyzeButton").addEventListener("click", () => {
    const resultsDiv = document.getElementById("analysisResults");
    resultsDiv.innerHTML = "<p>Performing analysis...</p>";

    // Simulate analysis with a timeout
    setTimeout(() => {
        // Simulate random threat levels
        const threatLevels = ["Low", "Medium", "High"];
        const randomThreat = threatLevels[Math.floor(Math.random() * threatLevels.length)];

        resultsDiv.innerHTML = `<p class="${getThreatClass(randomThreat)}"><strong>Analysis complete:</strong> Threat level detected: ${randomThreat}</p>`;
    }, 2000);
});
// Handle Generate Report button click
document.getElementById("generateReportButton").addEventListener("click", () => {
    fetch("http://127.0.0.1:5000/generate_report")
        .then((response) => {
            if (response.ok) {
                return response.blob();
            } else {
                throw new Error("Failed to generate report.");
            }
        })
        .then((blob) => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.style.display = "none";
            a.href = url;
            a.download = "threat_report.csv";
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            alert("Report downloaded successfully!");
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("Failed to download the report.");
        });
});
