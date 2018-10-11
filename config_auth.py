from oauth2client import file, client, tools
from googleapiclient.discovery import build
from httplib2 import Http

SCOPES = "https://www.googleapis.com/auth/drive"


def oauth():
    store = file.Storage('./credentials.json')
    creds = store.get()
    if not creds or creds.access_token_expired:
        creds = refresh_token(store=store)
    return build('drive', 'v3', http=creds.authorize(Http()))


def refresh_token(store):
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
    return creds


DRIVE = oauth()
