menu = {'margarita':[20,30],'hawaii':[23,35],'salami':[22,34],'carbonara':[21,32]}
dash = '-'*20
print("Witaj w Pizzeri u Jarosława")
choice = 2
while choice != 0:
    print("""
    1. Zamów Pizzę
    2. Menu
    3. Kontakt
    0. Zakończ
    """)
    choice = int(input("Wybierasz: "))
    print("")
    #wyjdz z petli
    if(choice==0):
        print("Do zobaczenia :)")
    #zamow pizze
    if(choice==1):
        print("Jaką pizzę chciałbyś zamówić?")

    #pokaz menu
    if(choice==2):
        print(dash)
        print('{:^20}'.format('MENU'))
        print(dash)
        for i in range(len(menu)):
            print('{:<12}{:>4}{:>4}'.format(list(menu.keys())[i],list(menu.values())[i][0],list(menu.values())[i][1]))
        print(dash)

    #kontakt
    if(choice==3):
        print(dash)
        print('{:^20}'.format('KONTAKT'))
        print(dash)
        print("Pizzera u Jarosława \n01-641 Żoliborz \ntel. 696 696 696")
        print(dash)