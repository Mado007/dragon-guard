## Dragon Park Dashboard

Dragon Park Dashboard is a tool designed to enhance the safety and efficiency of Dragon Park operations by providing real-time information about the status of park zones.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Insights](#insights)
- [Frontend Dashboard](#frontend-dashboard)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Dragon Park Dashboard consists of a backend service built with Flask to process events from the New Unified DragonPark Logging System (NUDLS™) and expose the status of park zones through a RESTful API. The backend is complemented by a simple frontend dashboard that displays the grid of zones.

## Requirements

Ensure you have the following dependencies installed:

- Python 3
- Flask

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Mado007/dragon-guard
   cd dragon-guard
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python app.py --port 5000
   ```

## Usage

- Access the Dragon Park Dashboard at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
- NUDLS events can be sent to the `/nudls` endpoint for processing.

## API Documentation

### Endpoints

- **GET /zones**: Fetch a list of all zones and their statuses.
- **GET /zones/:zoneId**: Retrieve details for a specific zone.

### Example API Request

```bash
curl -X GET http://127.0.0.1:5000/zones
```

## Testing

1. Start your application according to the instructions in the readme file.
2. Run the provided Postman collection against your API.
3. Make requests (based on your documentation) to determine the status of each zone.

## Insights

### High Availability

Given the critical nature of the software, the backend ensures high availability with the following measures:

- Utilization of load balancing.
- Implementation of failover mechanisms.
- Regular monitoring and automated alerts for system health.

### Scalability

In anticipation of housing over 1 million dragons, potential areas of concern include:

- Database scalability for handling increased data.
- Optimized algorithms for processing large datasets efficiently.

## Frontend Dashboard

### Dashboard Features

- Displays a grid of zones in a tabular format.
- Color-coded indicators for zone status (green for safe, red for maintenance).
- Basic search functionality for finding specific zones.
- Details view for each zone, including the last maintenance date and carnivore presence.
- Manual refresh button to fetch the latest data from the backend.

### User Authentication

Basic user authentication is implemented to restrict access to authorized personnel.

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or provide feedback.

## License

This project is licensed under the [MIT License](https://rem.mit-license.org/).

Copyright © 2023 [Mahmoud Eid](https://github.com/Mado007).<br />
`https://github.com/Mado007/dragon-guard` with the actual URL of your GitHub repository. Adjust the content as needed, and make sure to update the instructions and documentation based on the specific details of your project.
_This README was generated with ❤️ by [Mahmoud Eid](https://github.com/Mado007)_
