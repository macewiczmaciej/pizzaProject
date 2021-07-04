
import datetime

def addToOrders(zamowienie):
    with open("zamowienia.txt", "a") as file:
        datenow = datetime.datetime.now()
        file.write(datenow.strftime("%Y-%m-%d %H:%M"+":"))
        file.write("\n")
        file.write(str(zamowienie))
        file.write("\n")


def printFromOrders():
    with open("zamowienia.txt", "r") as file:
        for i in file.readlines():
            print(i)
