// Image upload & model prediction
document.getElementById('file-input').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            const img = document.getElementById('preview');
            img.src = e.target.result;
            img.style.display = 'block';

            const predictionText = document.getElementById('prediction-text');
            const confidenceText = document.getElementById('confidence-text');
            const relatedLinksList = document.getElementById('related-links');

            predictionText.innerText = "Processing...";
            confidenceText.innerText = "Processing...";
            relatedLinksList.innerHTML = "";

            // Hide or reset map
            const mapContainer = document.getElementById('map');
            mapContainer.innerHTML = "";
            mapContainer.style.display = "none";

            document.querySelector('.prediction').style.display = 'block';

            const formData = new FormData();
            formData.append('file', file);

            fetch('/predict', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                predictionText.innerText = data.prediction;
                confidenceText.innerText = `${(data.confidence * 100).toFixed(2)}%`;

                if (data.related_links && data.related_links.length > 0) {
                    data.related_links.forEach(link => {
                        const li = document.createElement('li');
                        const a = document.createElement('a');
                        a.href = link;
                        a.innerText = link;
                        a.target = "_blank";
                        a.style.textDecoration = "underline";
                        li.appendChild(a);
                        relatedLinksList.appendChild(li);
                    });
                }

                // Show map if coordinates exist
                if (data.latitude && data.longitude) {
                    mapContainer.style.display = "block";

                    const map = L.map('map').setView([data.latitude, data.longitude], 13);

                    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        attribution: '© OpenStreetMap contributors'
                    }).addTo(map);

                    L.marker([data.latitude, data.longitude])
                        .addTo(map)
                        .bindPopup("Location of this image")
                        .openPopup();
                }
            })
            .catch(error => {
                console.error('Error:', error);
                predictionText.innerText = "Error in prediction.";
                confidenceText.innerText = "--";
            });
        };

        reader.readAsDataURL(file);
    }
});

