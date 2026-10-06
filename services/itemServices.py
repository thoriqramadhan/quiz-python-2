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

def itemSeed():
    try:
        data = [('mobil' , 100000) , ('motor', 10000023) , ('sepeda' , 5000) , ('bola', 100) , ('handphone' , 2000)]
        query = "insert into item (name, price) values(%s, %s)"
        cursor.executemany(query , data)
        db_con.commit()
        return True
    except: 
        db_con.rollback()
        return False

def handleViewItem() -> bool:
    try:
        query = 'select id , name , price from item'
        cursor.execute(query)
        result = cursor.fetchall()
        WelcomeTemplate('VIEW ITEM')
        for item in result:
            print(f'ID : {item.get('id')} , NAME : {item.get('name')} , PRICE : {item.get('price')}')
    except:
        print('FAILED')

def handleAddItem(name, price) -> bool:
    try:
        query = 'insert into item (name , price) values (%s , %s)'
        cursor.execute(query , (name, price))
        db_con.commit()
        WelcomeTemplate(f'BERHASIL MENAMBAHKAN {name}')
        return True
    except:
        db_con.rollback()
        print('FAILED')
        return False
    
def handleEditItem(id , name, price) -> bool:
    try:
        query = 'update item set name = %s , price = %s where id = %s'
        cursor.execute(query , (name, price , id))
        db_con.commit()
        WelcomeTemplate(f'BERHASIL Mengubah ID : {id}')
        return True
    except:
        db_con.rollback()
        print('FAILED')
        return False
    
def handleDeleteItem(id ) -> bool:
    try:
        query = 'delete from item where id = %s'
        cursor.execute(query , (id ,))
        db_con.commit()
        WelcomeTemplate(f'BERHASIL Menghapus ID : {id}')
        return True
    except:
        db_con.rollback()
        print('FAILED')
        return False
# itemSeed()