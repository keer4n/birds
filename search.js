document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const resultsContainer = document.getElementById('results');

    searchButton.addEventListener('click', function() {
        const query = searchInput.value.toLowerCase();
        resultsContainer.innerHTML = '';

        // Example search logic
        const birds = [
            { name: 'Himalayan Monal', scientificName: 'Lophophorus impejanus', status: 'I' },
            { name: 'Satyr Tragopan', scientificName: 'Tragopan satyra', status: 'VU' },
            // Add more birds here
        ];

        const filteredBirds = birds.filter(bird =>
            bird.name.toLowerCase().includes(query) ||
            bird.scientificName.toLowerCase().includes(query) ||
            bird.status.toLowerCase().includes(query)
        );

        filteredBirds.forEach(bird => {
            const birdElement = document.createElement('div');
            birdElement.classList.add('bird');
            birdElement.innerHTML = `<h3>${bird.name}</h3><p><strong>Scientific Name:</strong> ${bird.scientificName}</p><p><strong>Status:</strong> ${bird.status}</p>`;
            resultsContainer.appendChild(birdElement);
        });

        if (filteredBirds.length === 0) {
            resultsContainer.innerHTML = '<p>No results found.</p>';
        }
    });
});
