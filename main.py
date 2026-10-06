from utils.interface import WelcomeTemplate
from utils.menus import itemMenuPrint , transactionMenuPrint
main_menus = ('Item' , 'Transaction' )


WelcomeTemplate('WELCOME TO ONLINE SHOP')

selectedMainMenu: int | None = None
while True :
    for index , item in enumerate(main_menus, start=1):
        print(f'{index}. {item}')

    selectedMain = int(input(f'Silahkan pilih menu : {1} - {len(main_menus)} \n'))
    # check is validc
    match selectedMain:
        case 1:
            itemMenuPrint()
        case 2:
            transactionMenuPrint()


print('SELAMAT TINGGAL')
    
