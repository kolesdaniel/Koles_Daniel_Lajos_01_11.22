from os import system

def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Pakli Kiírása')
    print('2 - Útmutató')
    print('3 - Játék elindítása')
    return input('Kérem válasszon: ')