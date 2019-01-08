import mysql.connector

def connect():
    conn = mysql.connector.connect(user = 'fVb9YnCgUU', password = '########',
                                   host = 'remotemysql.com', database = 'fVb9YnCgUU',
                                   port = 3306)
    cursor = conn.cursor()
    return cursor, conn
    
