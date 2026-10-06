from utils.utils import loopMenu
from services.itemServices import handleViewItem , handleAddItem ,handleDeleteItem ,handleEditItem
from services.historyService import handleCreateTransaction , handleViewTransaction

def itemMenuPrint():
    menus = ['add', 'edit' , 'delete' , 'view' , 'back to menu']
    while True:
        loopMenu(menus)
        selectedMenu = int(input(f'Silahkan pilih menu : {1} - {len(menus)} \n'))
        if selectedMenu == 1 :
            name = input('Masukan nama \n')
            price = int(input('Masukan harga \n'))
            handleAddItem(name , price)
        elif selectedMenu == 2 :
            handleViewItem()
            id = int(input('Masukan ID : \n'))
            name = input('Masukan nama baru \n')
            price = int(input('Masukan harga baru \n'))
            handleEditItem()
        elif selectedMenu == 3:
            handleViewItem()
            id = int(input('Masukan ID : \n'))
            handleDeleteItem(id)
        elif selectedMenu == 4:
            handleViewItem()
        elif selectedMenu == 5:
            break
        else : 
            print('Menu tidak ada')

def transactionMenuPrint():
    menus = ['create transaction', 'history', 'back to menu' ]
    while True:
        loopMenu(menus)
        selectedMenu = int(input(f'Silahkan pilih menu : {1} - {len(menus)} \n'))
        if selectedMenu == 1 :
            handleViewItem()
            item_id = int(input('Masukan id barang \n'))
            handleCreateTransaction(item_id)
            
        elif selectedMenu == 2 :
            handleViewTransaction()
        elif selectedMenu == 3:
            break
        else : 
            print('Menu tidak ada')