#! /usr/bin/env python
import os
import datetime
import bt_client
import google_sheets_client
from bitcointrade_dao import BitcointradeDao

RANGE = 'data!A:D'
def main():
    print 'Getting Ticker'
    sheet_id = os.environ['BITCOINTRADE_SHEET_ID']
    db_path = os.environ['DB_PATH']
    today = datetime.datetime.now()
    dao = BitcointradeDao(db_path)
    registrate_bitcoin_data(dao, sheet_id, today)

def registrate_bitcoin_data(dao, sheet_id, today):
    str_date = today.strftime("%Y-%m-%d")
    ticker = bt_client.get_ticker()
    dao.add_transaction(str_date, today.hour, ticker)
    transactions_values = dao.get_transactions_hour(str_date, today.hour)
    google_sheets_client.add_row(sheet_id, RANGE,
        [[
            str_date,
            today.hour,
            transactions_values['min'],
            transactions_values['max']
        ]])
    dao.close()

if __name__ == '__main__':
    main()
