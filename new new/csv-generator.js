// Function to generate random CSV data
function generateRandomCSV() {
    const headers = [
        "Duration",
        "Protocol Type",
        "Service",
        "Flag",
        "Source Bytes",
        "Destination Bytes",
        "Class"
    ];

    const rows = [];
    const numRows = 20; // Generate 20 rows (can be adjusted)
    const protocolTypes = ["tcp", "udp", "icmp"];
    const services = ["http", "private", "ftp", "telnet"];
    const flags = ["SF", "REJ", "S0", "RSTO"];
    const classes = ["normal", "anomaly", "high threat", "low threat"];

    for (let i = 0; i < numRows; i++) {
        const duration = Math.floor(Math.random() * 100); // Random duration
        const protocolType = protocolTypes[Math.floor(Math.random() * protocolTypes.length)];
        const service = services[Math.floor(Math.random() * services.length)];
        const flag = flags[Math.floor(Math.random() * flags.length)];
        const sourceBytes = Math.floor(Math.random() * 10000);
        const destinationBytes = Math.floor(Math.random() * 10000);
        const threatClass = classes[Math.floor(Math.random() * classes.length)];

        rows.push([duration, protocolType, service, flag, sourceBytes, destinationBytes, threatClass]);
    }

    return [headers, ...rows];
}

// Function to convert data array into CSV format
function convertToCSV(data) {
    return data.map(row => row.join(",")).join("\n");
}

// Function to download the generated CSV file
function downloadCSV(filename, data) {
    const csvContent = convertToCSV(data);
    const blob = new Blob([csvContent], { type: "text/csv" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Generate and download CSV every 10 seconds
setInterval(() => {
    const csvData = generateRandomCSV();
    const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
    const filename = `dataset_${timestamp}.csv`;
    downloadCSV(filename, csvData);
    console.log(`Generated and downloaded: ${filename}`);
}, 10000); // Interval set to 10 seconds
