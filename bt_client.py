#! /usr/bin/env python
import json
import sys
import requests

TICKER_BT_PATH='https://api.bitcointrade.com.br/v1/public/BTC/ticker'

def get_ticker():
    headers = {
        "content-type": "application/json"
    }
    req = requests.get(TICKER_BT_PATH,headers=headers)
    if req.status_code != 200:
        raise Exception("Error to get ticker")
    return req.json()
