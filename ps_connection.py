#!/usr/bin/python
import psycopg2
import sys
import pprint
from datetime import date
 
class PsConnection:

    def connection(self):
        conn_string = "host='localhost' dbname='opdb_dev' user='postgres' password='postgres'"
        # print the connection string we will use to connect
        print "Connecting to database\n	->%s" % (conn_string)
    
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
    
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        return cursor
        '''
        # execute our Query
        cursor.execute("SELECT * FROM BinanceTRXPrices")
    
        # retrieve the records from the database
        records = cursor.fetchall()
    
        # print out the records using pretty print
        # note that the NAMES of the columns are not shown, instead just indexes.
        # for most people this isn't very useful so we'll show you how to return
        # columns as a dictionary (hash) in the next example.
        pprint.pprint(records)
        '''

    def insert(self, query):
        conn_string = "host='localhost' dbname='opdb_dev' user='postgres' password='postgres'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def insert_registry(self, last_price):
        today = date.today()
        query = "INSERT INTO public.binancetrxprices (trx_price, trx_minute_date) VALUES({}, {})".format(str(last_price), "'" + today.strftime("%d/%m/%y") + "'")
        self.insert(query)