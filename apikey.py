import time
from datetime import date, datetime

import pymysql

class ApiKey:
    def __init__(self) -> None:
        while True:
            print("1.Create A API")
            print("2.Active A API")
            print("3.Use A API")
            print("4.Exit")

            inp = int(input("Enter Your Choise :- "))

            if inp == 1:
                self.create_api()

            elif inp == 2:
                self.active_api()

            elif inp == 3:
                self.use_api()

            elif inp == 4:
                quit()

            else:
                print("Your Choise is not Clear")

    def create_api(self):
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='myapp')

        cursor = connection.cursor()

        



        t = time.time()
        api = str(date.today())
        change = api.replace("-", "278")
        a = str(datetime.now())

        b = a.replace("-", "29")
        c = b.replace(":", "1.2")
        d = c.replace(" ", "1")

        
        apikeyvar = f"23644901uhshad728.{t}{change}7271jhsdha{d}dgfw72.212sxyz"
        print("Your API Key is :- " + apikeyvar)
        cursor.execute("INSERT INTO `api` (`id`, `akey`, `action`) VALUES(NULL, %s, 'off')", (apikeyvar))
        #23644901uhshad728.1706530572.2362483202427801278297271jhsdha2024290129291171.2461.212.236248dgfw72.212sxyz

        
        cursor.close()
        connection.commit()

        connection.close()

    def active_api(self):
        useapi = input("API Key On Active :- ")
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='myapp')

        cursor = connection.cursor()

        cursor.execute("UPDATE `api` SET `action` = 'active' WHERE `akey` = %s;", (useapi))

        cursor.close()
        connection.commit()

        connection.close()

    def use_api(self):
        pass #off no on calcutor display and key drop to calculator


obj = ApiKey()