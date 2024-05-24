import pandas as pd
data = pd.read_csv("data/users.csv")

def users_all():
    print(data)    
    
def search_users_def():

    search_email = input("masukan email : ")

    result_search_email = data.loc[data["email"] == search_email]

    if not result_search_email.empty:
        print("Data dengan email : ", search_email)
        print(result_search_email)
    else:
        print("Data dengan email : ", search_email, "tidak di temukan")