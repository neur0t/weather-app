# app/auth.py
from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
import os

API_TOKEN = os.getenv("TOKEN")
api_key_header = APIKeyHeader(name="x-token", auto_error=True)

def verify_token(api_key: str = Security(api_key_header)):
    if api_key != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
    return api_key
