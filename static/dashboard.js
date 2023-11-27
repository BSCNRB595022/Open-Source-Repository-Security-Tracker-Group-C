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


// Mock data for testing
const issues = [
    { title: 'Issue 1', description: 'Description 1', source: 'Source 1' },
    { title: 'Issue 2', description: 'Description 2', source: 'Source 2' },
    // Add more issues as needed
];

// Function to render issues in the table
function renderIssues() {
    const issueTableBody = document.getElementById('issue-table-body');
    issueTableBody.innerHTML = '';

    issues.forEach((issue, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${issue.title}</td>
            <td>${issue.description}</td>
            <td>${issue.source}</td>
            <td><button onclick="deleteIssue(${index})" class="btn btn-danger">Delete</button></td>
        `;
        issueTableBody.appendChild(row);
    });
}

// Function to submit a new issue
function submitIssue() {
    const title = document.getElementById('issue-title').value;
    const description = document.getElementById('issue-description').value;
    const source = document.getElementById('issue-source').value;

    if (title && description && source) {
        const newIssue = { title, description, source };
        issues.push(newIssue);
        renderIssues();
    } else {
        alert('Please fill in all fields.');
    }
}

// Function to delete an issue
function deleteIssue(index) {
    issues.splice(index, 1);
    renderIssues();
}

// Initial rendering
document.addEventListener('DOMContentLoaded', function () {
    renderIssues();
});


// Function to update an existing issue
function updateIssue(index) {
    const title = prompt('Update Title:', issues[index].title);
    const description = prompt('Update Description:', issues[index].description);
    const source = prompt('Update Source:', issues[index].source);

    if (title !== null && description !== null && source !== null) {
        issues[index] = { title, description, source };
        renderIssues();
    }
}

// Function to view details of an issue
function viewDetails(index) {
    const issue = issues[index];
    alert(`Title: ${issue.title}\nDescription: ${issue.description}\nSource: ${issue.source}`);
}

// Update the renderIssues function
function renderIssues() {
    const issueTableBody = document.getElementById('issue-table-body');
    issueTableBody.innerHTML = '';

    issues.forEach((issue, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${issue.title}</td>
            <td>${issue.description}</td>
            <td>${issue.source}</td>
            <td>
                <button onclick="updateIssue(${index})" class="btn btn-warning">Update</button>
                <button onclick="viewDetails(${index})" class="btn btn-info">Details</button>
                <button onclick="deleteIssue(${index})" class="btn btn-danger">Delete</button>
            </td>
        `;
        issueTableBody.appendChild(row);
    });
}


function logout() {
    // You can add any client-side logout logic here
    // For now, let's redirect to the logout route
    window.location.href = '/logout';
}