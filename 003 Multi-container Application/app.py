# using flask to build a simple app that uses mysql db

from flask import Flask
import mysql.connector
import time
import os

app = Flask(__name__)

def get_db_connection(retries=5, delay=5):
    for attempt in range(retries):
        try:
            connection = mysql.connector.connect(
                host='db',
                user='root',
                password=os.getenv("MYSQL_ROOT_PASSWORD", "example"),
                database=os.getenv("MYSQL_DATABASE", "test_db")
            )
            print("Connected to MySQL")
            return connection 
        except mysql.connector.Error as err:
            print(f"DB Not ready ({attempt+1}/{retries}): {err}")
            time.sleep(delay)
    raise Exception("Could not connect to MYSQL")

@app.route('/')
def hello_world():
    try:
        connection = get_db_connection()
        cursor= connection.cursor()
        cursor.execute("SELECT 'Hello, Docker Compose! Flask + MySQL is working' ")
        result = cursor.fetchone()
        connection.close()
        return f"<h1>{result[0]}</h1>"
    except Exception as e:
        return f"<h1 style='color:red'>Database Error: {str(e)} </h1>"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)