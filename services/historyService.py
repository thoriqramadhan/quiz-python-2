import os , sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir in sys.path:
    sys.path.remove(script_dir)

from database.connection import db_con
from utils.interface import WelcomeTemplate

cursor = db_con.cursor(dictionary=True)


def handleViewTransaction() -> bool:
    try:
        query = 'select trx.id as trx_id , cs.name as customer_name, cs.id as customer_id , itm.name as item_name , itm.id as item_id from transaction as trx left join customer as cs on cs.id = trx.customer_id left join item as itm on itm.id = trx.item_id '
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        WelcomeTemplate('VIEW TRANSACTION')
        for item in result:
            print(f'trx_id : {item.get('trx_id')} , customer_name : {item.get('customer_name')} , customer_id : {item.get('customer_id')} , item_name : {item.get('item_name')} , item_id : {item.get('item_id')} ')
    except:
        print('FAILED')

def handleCreateTransaction(item_id) -> bool:
    try:
        query = 'insert into transaction (item_id , customer_id) values(%s , %s)'
        cursor.execute(query , (item_id, 1))
        db_con.commit()
        WelcomeTemplate(f'BERHASIL MENAMBAHKAN TRANSAKSI')
        return True
    except:
        db_con.rollback()
        print('FAILED')
        return False

handleViewTransaction()
    

# itemSeed()