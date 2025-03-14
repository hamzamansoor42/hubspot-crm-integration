from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import time
import redis
from services import *

load_dotenv()

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/process-contacts")
def process_contacts():
    try:
        contacts = fetch_contacts()
        total_processed = 0

        for contact in contacts:
            redis_client.set(contact['id'], 1) 
            total_processed += 1

        send_admin_email({"total_processed": total_processed})
        return {"message": "Process completed", "total": total_processed}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong!")