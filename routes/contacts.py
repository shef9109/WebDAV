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
        scopes=['https://www.googleapis.com/auth/contacts.readonly'],
        redirect_uri='http://localhost:8000/contacts/auth/callback'
    )
    authorization_url, state = flow.authorization_url()
    return {"authorization_url": authorization_url}

@router.get("/auth/callback")
async def google_auth_callback(code: str):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=['https://www.googleapis.com/auth/contacts.readonly'],
        redirect_uri='http://localhost:8000/contacts/auth/callback'
    )
    flow.fetch_token(code=code)
    credentials = flow.credentials
    service = build('people', 'v1', credentials=credentials)
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=10,
        personFields='names,emailAddresses').execute()
    connections = results.get('connections', [])
    return connections