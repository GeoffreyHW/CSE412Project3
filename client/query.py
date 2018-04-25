from flask import Flask
import psycopg2

APP=Flask(__name__)

@APP.route('/querydb', methods=['GET'])
def get_data():
    """ query data from the vendors table """
    conn = None
    try:
        conn = psycopg2.connect(database="outfile", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute ("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        rows = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows