lapok=[]
from os import system

def menu():
    system('cls')
    print('----------MENÜ----------')
    print('0 - Kilépés')
    print('1 - Pakli Kiírása')
    print('2 - Útmutató')
    print('3 - Játék elindítása')
    return input('Kérem válasszon: ')

def pakliKiir():
        system('cls')
        print('-7db lap van egy pakliban.')
        for lap in lapok :
            print(f'{lap}')
        input('-Szerepelhet benne: piros, zöld, makk és tök is.\n-Ezeken bellül is vannak dolgok Pl:(alsó,felső,király,ász).')

      

      

  