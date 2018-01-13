#! /usr/bin/env python
import sqlite3

class BitcointradeDao:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)

    def add_transaction(self, transaction_date, transaction_hour, ticker):
        query = """INSERT INTO transactions
         VALUES (:transaction_date, :transaction_hour,
         :transaction_value, datetime('now'))"""
        self.insert(query, {
                "transaction_date" : transaction_date,
                "transaction_hour" : transaction_hour,
                "transaction_value" : float(ticker['data']['last'])
            })

    def get_transactions_hour(self, transaction_date, transaction_hour):
        query = """SELECT MIN(transaction_value),MAX(transaction_value)
         FROM transactions
         WHERE transaction_date = :t_date AND transaction_hour = :hour """
        args = { "t_date": transaction_date, "hour" : transaction_hour}
        transaction = self.select_one(query, args)
        return {
            "min" : transaction[0],
            "max" : transaction[1]
        }


    def select_one(self, query, args):
        cursor = self.conn.cursor()
        return cursor.execute(query,args).fetchone()

    def insert(self, query, args):
        cursor = self.conn.cursor()
        cursor.execute(query, args)
        self.conn.commit()

    def close(self):
        self.conn.close()
