lapok=[]
utmutato=[]
jatek=[]
pakli=['piros ász','piros király','piros felső','piros alsó','zöld ász','zöld király','zöld felső','zöld alsó','makk ász','makk király','makk felső','makk alsó','tök ász','tök király','tök felső','tök alsó']
from os import system

def menu():
    system('cls')
    print('----------MENÜ----------')
    print('0 - Kilépés')
    print('1 - Pakli Kiírása')
    print('2 - Útmutató')
    print('3 - Játék elindítása')
    valasztott = input('Kérem válasszon: ')
    return valasztott

def pakliKiir():
        system('cls')
        print('-32db lap van egy pakliban.')
        for lap in lapok :
            print(f'{lap}')
        input('-Szerepelhet benne: piros, zöld, makk és tök is.\n-Ezeken bellül is vannak rangok Pl:(alsó,felső,király,ász). \n \n Enter lenyomásával léphet tovább....')

def utmutatoKiir():
      system('cls')
      print('A JÁTÉK CÉLJA:')    
      for adatok in utmutato :
        print(f'{adatok}')
      input(f'A kézlapok lerakása.\n\n----A JÁTÉK MENETE---- \nAz osztó a kártyalapokat képükkel lefelé fordítva kör alakban helyezi el az asztalon. \nVégül egy kártyát a kör közepére helyez, képével felfelé fordítva. \nAz osztótól jobbra ülőnek, majd sorban minden játékosnak a kör közepén lévő kártyával azonos színű lapot kell tenni és egy tetszés szerinti lappal színt kérni. \nTehát ha piros lap lett felütve, a következő játékos addig húz a körbe rakott kártyákból, amíg piros színűt nem talál. \nEzt a kör közepére teszi és egy másik lappal színt kér a következő játékostól: pirosra makkot, makkra zöldet, stb. \nAki nem tud a kért színből tenni, a legfelső kártyával azonos színű lapot fel kell vennie. \nIlyenkor a tőle jobbra ülő játékos tehet le a felső lappal azonos színű kártyát és kérhet egy másikkal színt a szomszédjától. \nA játékot megnyeri az a játékos, aki utolsó lapját is a kör közepére tudta tenni.\n \n Enter lenyomásával léphet tovább....')

def jatekInditasa():
  system('cls')
  print('--Játék Indítása--')
  for elemek in jatek :
    print(f'{elemek}')
  input()