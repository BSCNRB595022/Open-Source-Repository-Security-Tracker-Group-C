// Get filter and search elements
const severityFilter = document.getElementById('severity-filter');
const sortBy = document.getElementById('sort-by');
const searchBar = document.getElementById('search-bar');
const applyFilters = document.getElementById('apply-filters');

// Get the table body element
const tableBody = document.querySelector('table tbody');

applyFilters.addEventListener('click', () => {
    const severityValue = severityFilter.value;
    const sortByValue = sortBy.value;
    const searchValue = searchBar.value.toLowerCase();

    // Create a data object to send to the server
    const data = {
        severity: severityValue,
        sort: sortByValue,
        search: searchValue,
    };

    // Send a POST request to the server with the data
    fetch('/get_filtered_issues', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            // Clear the table
            tableBody.innerHTML = '';

            // Populate the table with filtered issues
            data.issues.forEach(issue => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${issue.title}</td>
                    <td>${issue.description}</td>
                    <td>${issue.severity}</td>
                    <td>${issue.source}</td>
                `;
                tableBody.appendChild(row);
            });
        });
});
