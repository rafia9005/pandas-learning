from handler.users import search_users_def
from handler.users import users_all
import time 

def menu_handler():
    def menu_satu():
        search_users_def()
    def manu_dua():
        users_all()
    # membuat list menu
    menu_list = {
        1: menu_satu,
        2: users_all
    }
    
    print("1. Email Search")
    print("2. All Users")
    
    use = int(input("pilih menu : "))
    
    if use in menu_list:
        time.sleep(2)
        menu_list[use]()
    else:
        print("pilihan tidak valid")
    