#! /usr/bin/env python
import sqlite3

def connection(db_name):
    return sqlite3.connect(db_name)

def select(db_name, query):
    conn = connection(db_name)
    cursor = conn.cursor()
    return cursor.execute(query)

def insert(db_name, query):
