#! /usr/bin/env python
import httplib2
import jamal_google_auth as gauth
from googleapiclient import discovery

def add_row(sheet_id, range, values):
    credentials = gauth.get_credentials()
    service = discovery.build('sheets', 'v4', credentials=credentials)
    rangeName = range
    body = {
        "range" : range,
        "values" :values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=sheet_id, range=rangeName, valueInputOption='RAW', body=body).execute()
