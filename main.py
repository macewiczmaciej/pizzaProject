menu = {'własna':[15,20],'margarita':[20,30],'hawaii':[23,35],'salami':[22,34],'carbonara':[21,32]}
skladniki = {'szynka':4,'ser':3,'salami':4,'bekon':3,'kurczak':5,'pieczarki':2,'ananas':3,'cebula':2}
sosy = ['bez sosu','czosnkowy','pomidorowy','miodowo-musztardowy','majonezowy']
zamowienie = []
cena = 0
sos = None

def showMenu():
    print(dash)
    print('{:^24}'.format('MENU'))
    print(dash)
    for i in range(len(menu)):
        print('{:<1}{:<2}{:<12}{:>4}{:>4}'.format(i + 1, '.', list(menu.keys())[i].capitalize(), list(menu.values())[i][0],list(menu.values())[i][1]))
    print(dash)

def showSkladniki():
    print(dash)
    print('{:^24}'.format('SKŁADNIKI'))
    print(dash)
    for i in range(len(skladniki)):
        print('{:<1}{:<2}{:<12}{:>4}'.format(i + 1, '.', list(skladniki.keys())[i].capitalize(), list(skladniki.values())[i]),'PLN')
    print(dash)

def wyborSosu():
    print(dash)
    print('{:^24}'.format('SOSY'))
    print(dash)
    for i in range(len(sosy)):
        print('{:<1}{:<2}{:<1}'.format(i, '.', sosy[i]))
    print(dash)
    print("Jaki sos do pizzy? ")
    choiceSos = int(input("Wybieram: "))
    sos = sosy[choiceSos]
    print("Wybrany sos:", sos)

def sumujZamowienie():
    suma = cena
    if sos != 0 and sos != None:
        suma+=3
    print('Wartość zamówienia wynosi: ',suma,'PLN')

def szczegolyZamowienia():

    print(dash)
    print('{:^24}'.format("MOJE ZAMÓWIENIE"))
    print(dash)
    if len(zamowienie)==0:
        print("Jeszcze nic nie wybrałeś :)")
    else:
        print("Twoje zamówienie: ")
        print(zamowienie)
        sumujZamowienie()

dash = '-'*24
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

    #wyjdz z menu
    if(choiceMenu==0):
        print("Do zobaczenia :)")

    #zamow pizze
    if(choiceMenu==1):
        showMenu()
        print("Podaj numer pizzy którą chcesz zamówić")
        choicePizza = input("Wybieram: ")

        #wlasna
        if choicePizza == "1":
            wybraneSkladniki = []
            choiceSkladnik = None;
            showSkladniki()
            while(choiceSkladnik != 'dalej'):
                print("Podaj numer składnika który chcesz dodać do pizzy")
                print("Wpisz 'dalej', jeśli chcesz przejść do kolejnego kroku lub 'anuluj', żeby powrócić do MENU")
                choiceSkladnik = input("Wybieram: ")
                if choiceSkladnik == 'anuluj':
                    break
                elif choiceSkladnik == 'dalej':
                    print("Jaki rozmiar pizzy? Podaj 'mala' lub 'duza'")
                    choiceRozmiar = input("Wybieram: ")
                    if choiceRozmiar == 'mala':
                        zamowienie.append(list(menu.keys())[int(choicePizza)-1])
                        cena += list(menu.values())[int(choicePizza)-1][0]
                    elif choiceRozmiar == 'duza':
                        zamowienie.append(list(menu.keys())[int(choicePizza)-1])
                        cena += list(menu.values())[int(choicePizza)-1][1]
                    wyborSosu()

                else:
                    wybraneSkladniki.append(list(skladniki.keys())[int(choiceSkladnik)-1])
                    cena += list(skladniki.values())[int(choiceSkladnik)-1
                    ]
                    print("Wybrane składniki: ",wybraneSkladniki)
        else:
            print("Jaki rozmiar pizzy? Podaj 'mala' lub 'duza'")
            choiceRozmiar = input("Wybieram: ")
            if choiceRozmiar == 'mala':
                zamowienie.append(list(menu.keys())[int(choicePizza)-1])
                cena += list(menu.values())[int(choicePizza)-1][0]
            elif choiceRozmiar == 'duza':
                zamowienie.append(list(menu.keys())[int(choicePizza)-1])
                cena += list(menu.values())[int(choicePizza)-1][1]
            wyborSosu()
        szczegolyZamowienia()

    #pokaz menu
    if(choiceMenu==2):
        showMenu()

    #moje zamowienie
    if(choiceMenu==3):
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
            print(dash)
            print("SUKCES! Zamówiono wybrane pizze :)")
            print(dash)
            zamowienie.clear()
        elif choiceZamowienie == 2:
            zamowienie.clear()
            print(dash)
            print("Zamówienie zostało anulowane.")
            print(dash)

    #kontakt
    if(choiceMenu==4):
        print(dash)
        print('{:^22}'.format('KONTAKT'))
        print(dash)
        print("Pizzera u Jarosława \n01-641 Żoliborz \ntel. 696 696 696")
        print(dash)