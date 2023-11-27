document.addEventListener('DOMContentLoaded', function () {
    const reportIssueForm = document.getElementById('report-issue-form');

    if (reportIssueForm) {
        reportIssueForm.addEventListener('submit', function (event) {
            event.preventDefault();
            scanSource();
        });
    }
});

function scanSource() {
    const urlInput = document.getElementById('issue-source');
    const resultContainer = document.getElementById('virustotal-result');

    // Get the URL from the input field
    const url = urlInput.value;

    // Check if the URL is valid
    if (!url) {
        resultContainer.innerHTML = '<p>Please enter a valid URL</p>';
        return;
    }

    // Make a POST request to the /scan-url route
    fetch('/scan-url', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url }),
    })
        .then(response => response.json())
        .then(data => {
            resultContainer.innerHTML = `<p>${data.message}</p>`;
        })
        .catch(error => {
            resultContainer.innerHTML = '<p>Error scanning URL</p>';
            console.error('Error scanning URL:', error);
        });
}
