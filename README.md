# HubSpot FastAPI Backend

## Overview
This project is a FastAPI-based backend for automating contact and deal management in HubSpot CRM using the HubSpot API.

## Features
- Fetches all contacts created in January 2025.
- Uses the HubSpot API key for authentication.
- Caches processed contacts using Redis to avoid redundant API calls.
- Sends an admin email summary after processing contacts.
- Implements rate limiting to prevent exceeding API limits.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Redis (for caching)

## Setup Instructions
### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/hubspot-fastapi-backend.git
cd hubspot-fastapi-backend
```

### 2. Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with the following variables:
```sh
HUBSPOT_API_KEY=your_hubspot_api_key
ADMIN_EMAIL=your_admin_email@example.com
```

### 5. Start Redis (Required for Caching)
#### On macOS/Linux (Using Homebrew or APT)
```sh
redis-server
```
#### On Windows (Using Docker)
```sh
docker run --name redis -p 6379:6379 -d redis
```

### 6. Run the FastAPI Server
```sh
uvicorn main:app --reload
```

### 7. Access the API
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 8. Trigger Contact Processing
```sh
curl -X GET "http://127.0.0.1:8000/process-contacts"
```

## Testing
To run unit tests (if implemented):
```sh
pytest tests/
```

## Future Enhancements
- Implement email notifications for errors.
- Add more logging and monitoring.
- Expand API functionality for other HubSpot objects.

## License
This project is licensed under the MIT License.

