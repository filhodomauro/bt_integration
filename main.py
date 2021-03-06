#! /usr/bin/env python
import os
import datetime
import bt_client
import google_sheets_client
from bitcointrade_dao import BitcointradeDao

RANGE = 'data!A:D'
def main():
    try:
        print 'Getting Ticker'
        sheet_id = os.environ['BITCOINTRADE_SHEET_ID']
        db_path = os.environ['DB_PATH']
        today = datetime.datetime.now()
        dao = BitcointradeDao(db_path)
        registrate_bitcoin_data(dao, sheet_id, today)
        print 'Done'
    except Exception as e:
        print "Unexpected error on bitcointrade check"
        print e
        raise

def registrate_bitcoin_data(dao, sheet_id, today):
    str_date = today.strftime("%Y-%m-%d")
    ticker = bt_client.get_ticker()
    dao.add_transaction(str_date, today.hour, ticker)
    if today.minute == 59:
        transactions_values = dao.get_transactions_hour(str_date, today.hour)
        update_sheet(sheet_id, str_date, today.hour, transactions_values)
    dao.close()

def update_sheet(sheet_id, str_date, hour, transactions_values):
    google_sheets_client.add_row(sheet_id, RANGE,
        [[
            str_date,
            hour,
            transactions_values['min'],
            transactions_values['max']
        ]])

if __name__ == '__main__':
    main()
