document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("issue-file");
    const fileListContainer = document.getElementById("file-list");

    fileInput.addEventListener("change", function () {
        fileListContainer.innerHTML = ""; // Clear previous files
        const files = fileInput.files;
        for (let i = 0; i < files.length; i++) {
            const listItem = document.createElement("li");
            listItem.textContent = files[i].name;
            fileListContainer.appendChild(listItem);
        }
    });
});


// In your dashboard.js file
document.addEventListener('DOMContentLoaded', function () {
    let currentResult = null;

    async function scanSource() {
        const virustotalResult = document.getElementById('virustotal-result');
        // Display the loading icon while scanning
        virustotalResult.innerHTML = '<p>Loading...</p>';

        try {
            // Make an asynchronous request to the server
            const sourceUrl = document.getElementById('issue-source').value;
            const response = await fetch('/scan-url', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: sourceUrl }),
            });

            // Handle the response from the server
            const result = await response.json();
            currentResult = result; // Save the current result
            virustotalResult.innerHTML = `<p>${result.message}</p>`;
        } catch (error) {
            console.error('Error during scanSource:', error);
            virustotalResult.innerHTML = '<p>An error occurred during the scan.</p>';
        }
    }

    // Function to display the current result without making a new request
    function showCurrentResult() {
        const virustotalResult = document.getElementById('virustotal-result');
        if (currentResult) {
            virustotalResult.innerHTML = `<p>${currentResult.message}</p>`;
        } else {
            virustotalResult.innerHTML = '<p>No result available</p>';
        }
    }
});
