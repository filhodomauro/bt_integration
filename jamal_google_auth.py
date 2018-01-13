#! /usr/bin/env python
import os
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'raspberry.home-central.googleapis.com.json'

def get_credentials():
    credentials = service_account.Credentials.from_service_account_file(
            get_credential_path(), scopes=SCOPES)
    return credentials

def get_credential_path():
    home_dir = os.path.expanduser('~')
    credentials_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credentials_dir):
        raise RuntimeError("Credentials not fount on path {}".format(credentials_dir))
    return os.path.join(credentials_dir, SERVICE_ACCOUNT_FILE)
