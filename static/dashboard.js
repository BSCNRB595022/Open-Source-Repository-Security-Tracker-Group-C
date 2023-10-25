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

    console.log("Severity:", severityValue);
    console.log("Sort By:", sortByValue);
    console.log("Search:", searchValue);

    const data = {
        severity: severityValue,
        sort: sortByValue,
        search: searchValue,
    };

    console.log("Data to Send:", data);

    fetch('/get_filtered_issues', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            console.log("Data Received:", data);

            tableBody.innerHTML = '';

            data.issues.forEach(issue => {
                const row = document.createElement('tr');

                const titleCell = document.createElement('td');
                titleCell.innerText = issue[1]; // Access the title by index
                row.appendChild(titleCell);

                const descriptionCell = document.createElement('td');
                descriptionCell.innerText = issue[2]; // Access the description by index
                row.appendChild(descriptionCell);

                const severityCell = document.createElement('td');
                severityCell.innerText = issue[3]; // Access the severity by index
                row.appendChild(severityCell);

                const sourceCell = document.createElement('td');
                sourceCell.innerText = issue[4]; // Access the source by index
                row.appendChild(sourceCell);

                tableBody.appendChild(row);
            });


        });
});
