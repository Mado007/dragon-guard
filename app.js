document.addEventListener('DOMContentLoaded', function () {
    // Fetch data from the backend API
    fetch('/nudls', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "kind": "dragon_added",
            "name": "McGroggity",
            "species": "deadly nadder",
            "gender": "male",
            "id": 1032,
            "digestion_period_hours": 48,
            "herbivore": false,
            "time": "2018-04-20T11:50:53.4601",
            "park_id": 1
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error sending data:', error));
});
