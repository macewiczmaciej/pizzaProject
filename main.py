import datetime

import obliczenia
import random

menu = {'własna': [15, 20], 'margarita': [20, 30], 'hawaii': [23, 35], 'salami': [22, 34], 'carbonara': [21, 32]}
skladniki = {'szynka': 4, 'ser': 3, 'salami': 4, 'bekon': 3, 'kurczak': 5, 'pieczarki': 2, 'ananas': 3, 'cebula': 2}
zamowienie = []
cena = []

def showMenu():
    print(dash)
    print('{:^24}'.format('MENU'))
    print(dash)
    for i in range(len(menu)):
        print('{:<1}{:<2}{:<12}{:>4}{:>4}'.format(i + 1, '.', list(menu.keys())[i].capitalize(),list(menu.values())[i][0], list(menu.values())[i][1]))
    print(dash)

def zamowPizze():
    print("Podaj numer pizzy którą chcesz zamówić")
    choicePizza = input("Wybieram pizzę: ")

    # wlasna
    if choicePizza == "1":
        wybraneSkladniki = []
        choiceSkladnik = ""
        wartoscSkladnikow = 0
        showSkladniki()
        while (choiceSkladnik != 'gotowe'):
            print("Podaj numer składnika który chcesz dodać do pizzy")
            print("Wpisz 'gotowe' żeby przejść dalej")
            choiceSkladnik = input("Wybieram składnik: ")
            if choiceSkladnik == 'gotowe':
                break
            else:
                wybraneSkladniki.append(list(skladniki.keys())[int(choiceSkladnik) - 1])
                wartoscSkladnikow += list(skladniki.values())[int(choiceSkladnik) - 1]
                print("Wybrane składniki: ", wybraneSkladniki)
        sumujZamowienie(choicePizza, wyborRozmiaru(choicePizza),wartoscSkladnikow)
    else:
        sumujZamowienie(choicePizza, wyborRozmiaru(choicePizza))

def wyborRozmiaru(choicePizza):
    print("Jaki rozmiar pizzy? Podaj 'mala' lub 'duza'")
    choiceRozmiar = input("Wybieram rozmiar: ")
    if choiceRozmiar == 'mala':
        zamowienie.append(list(menu.keys())[int(choicePizza) - 1])
    elif choiceRozmiar == 'duza':
        zamowienie.append(list(menu.keys())[int(choicePizza) - 1])
    return choiceRozmiar


def showSkladniki():
    print(dash)
    print('{:^24}'.format('SKŁADNIKI'))
    print(dash)
    for i in range(len(skladniki)):
        print('{:<1}{:<2}{:<12}{:>4}'.format(i + 1, '.', list(skladniki.keys())[i].capitalize(),
                                            list(skladniki.values())[i]), 'PLN')
    print(dash)


def sumujZamowienie(choicePizza, choiceRozmiar, wartoscSkladnikow = 0):
    if (choiceRozmiar == 'mala'):
        cena.append(list(menu.values())[int(choicePizza) - 1][0] + wartoscSkladnikow)
    elif (choiceRozmiar == 'duza'):
        cena.append(list(menu.values())[int(choicePizza) - 1][1] + wartoscSkladnikow)

def szczegolyZamowienia():
    print(dash)
    print('{:^24}'.format("MOJE ZAMÓWIENIE"))
    print(dash)
    if len(zamowienie) == 0:
        print("Jeszcze nic nie wybrałeś :)")
    else:
        for i in range(len(zamowienie)):
            print('{:<1}{:<2}{:<12}{:<4}'.format(i + 1, '.', zamowienie[i], cena[i]))
        print()
        print("Łączna wartość zamówienia to:", sum(cena))
dash = '-' * 24
print("Witaj w Pizzeri u Jarosława")
choiceMenu = 2
while choiceMenu != 0:
    print("""
    1. Zamów Pizzę
    2. Menu
    3. Moje zamowienie
    4. Kontakt
    0. Zakończ
    """)
    choiceMenu = int(input("Wybieram: "))

    # wyjdz z menu
    if (choiceMenu == 0):
        print("Do zobaczenia :)")

    # zamow pizze
    if (choiceMenu == 1):
        showMenu()
        zamowPizze()
        szczegolyZamowienia()

    # pokaz menu
    if (choiceMenu == 2):
        showMenu()

    # moje zamowienie
    if (choiceMenu == 3):
        szczegolyZamowienia()
        print()
        print("1. Zamów")
        print("2. Anuluj")
        print("0. Cofnij")
        print()
        choiceZamowienie = int(input('Wybieram: '))
        if choiceZamowienie == 0:
            continue
        elif choiceZamowienie == 1:
            with open("zamowienia.txt","a") as file:
                file.write(str(datetime.datetime.now()))
                file.write("\n")
                file.write(str(zamowienie))
                file.write("\n")

            print(dash)
            print("SUKCES! Zamówiono wybrane pizze :)")
            print(dash)
            cena.clear()
            zamowienie.clear()
        elif choiceZamowienie == 2:
            print(dash)
            print("Zamówienie zostało anulowane.")
            print(dash)
            zamowienie.clear()
            cena.clear()

    # kontakt
    if (choiceMenu == 4):
        print(dash)
        print('{:^22}'.format('KONTAKT'))
        print(dash)
        print("Pizzera u Jarosława \n01-641 Żoliborz \ntel. 696 696 696")
        print(dash)
