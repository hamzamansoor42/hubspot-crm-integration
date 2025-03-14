import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HUBSPOT_API_URL = "https://api.hubapi.com"
HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

def get_headers():
    return {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }

def fetch_contacts():
    url = f"{HUBSPOT_API_URL}/crm/v3/objects/contacts?createdate__gte=2025-01-01"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        logger.error(f"Error fetching contacts: {response.text}")
        return []

def send_admin_email(summary):
    logger.info(f"Sending summary email to {ADMIN_EMAIL}: {summary}")
    # Implementation of email sending can be added here