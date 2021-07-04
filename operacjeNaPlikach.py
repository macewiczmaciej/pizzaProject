
import datetime

def addToOrders(zamowienie):
    with open("zamowienia1.txt", "w") as file:
        datenow = datetime.datetime.now()
        file.write(datenow.strftime("%Y-%m-%d %H:%M"+":"))
        file.write("\n")
        file.write(str(zamowienie))
        file.write("\n")


def printFromOrders():
    with open("zamowienia1.txt", "a") as file:
        for i in file.readlines():
            print(i)
