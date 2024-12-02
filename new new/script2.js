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
      const data = e.target.result;
      displayData(parseCSV(data));
    };
    reader.readAsText(file);
  });
  
  // Parse CSV data
  function parseCSV(data) {
    const rows = data.split("\n").filter((row) => row.trim() !== "");
    return rows.map((row) => row.split(","));
  }
  
  // Display uploaded data in a table
  function displayData(data) {
    const tableBody = document.querySelector("#dataTable tbody");
    tableBody.innerHTML = ""; // Clear previous data
  
    data.forEach((row, index) => {
      if (index === 0) return; // Skip header
      const tr = document.createElement("tr");
      row.forEach((cell) => {
        const td = document.createElement("td");
        td.textContent = cell;
        tr.appendChild(td);
      });
      tableBody.appendChild(tr);
    });
  }
  
  // Handle real-time analysis
  document.getElementById("analyzeButton").addEventListener("click", () => {
    const resultsDiv = document.getElementById("analysisResults");
    resultsDiv.innerHTML = "<p>Performing analysis...</p>";
  
    // Simulate analysis with a timeout
    setTimeout(() => {
      resultsDiv.innerHTML = "<p><strong>Analysis complete:</strong> No threats detected!</p>";
    }, 2000);
  });