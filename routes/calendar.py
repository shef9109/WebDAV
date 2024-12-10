from fastapi import APIRouter, Depends
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

router = APIRouter()

CLIENT_SECRETS_FILE = 'client_secret.json'  # Путь к вашему файлу client_secret.json

@router.get("/auth")
async def google_auth():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        redirect_uri='http://localhost:8000/calendar/auth/callback'
    )
    authorization_url, state = flow.authorization_url()
    return {"authorization_url": authorization_url}

@router.get("/auth/callback")
async def google_auth_callback(code: str):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        redirect_uri='http://localhost:8000/calendar/auth/callback'
    )
    flow.fetch_token(code=code)
    credentials = flow.credentials
    service = build('calendar', 'v3', credentials=credentials)
    events_result = service.events().list(calendarId='primary', maxResults=10).execute()
    events = events_result.get('items', [])
    return events