import mysql.connector
import os
import dotenv

dotenv.load_dotenv()

passwd= os.getenv('DB_PASSWD')



db_con = mysql.connector.connect(
    user='root',
    host='localhost',
    passwd=passwd,
    database='online_shop'
)

if db_con.is_connected :
    print('CONNECTED')

