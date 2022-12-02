import random

lapok=[]
kozepen = []
utmutato=[]
jatekosok={}
jatekosok2 = []
pakliSzereploi = ['makk','piros','zöld','tök']

for i in range(0,31):
  lapok.append('')

from os import system

def menu():
    system('cls')
    print('----------MENÜ----------')
    print('0 - Kilépés')
    print('1 - Pakli Kiírása')
    print('2 - Útmutató')
    print('3 - Játék elindítása')
    valasztott = input('Kérem válasszon a menüpontok közül: ')
    return valasztott

def pakliKiir():
        system('cls')
        print('-32db lap van egy pakliban.')
        input('-Szerepelhet benne: piros, zöld, makk és tök is.\n-Ezeken bellül is vannak rangok Pl:(alsó,felső,király,ász). \n \n Enter lenyomásával léphet tovább....')

def utmutatoKiir():
      system('cls')
      print('-----Piros papucs-----')    
      for adatok in utmutato :
        print(f'{adatok}')
      input(f'\nA JÁTÉK CÉLJA:\nA kézlapok lerakása. \n\nJáték típusa: gyermek \n\nJátékosok: 3, 4, 5, 6 \n\n----A JÁTÉK MENETE---- \nAz osztó a kártyalapokat képükkel lefelé fordítva kör alakban helyezi el az asztalon. \nVégül egy kártyát a kör közepére helyez, képével felfelé fordítva. \nAz osztótól jobbra ülőnek, majd sorban minden játékosnak a kör közepén lévő kártyával azonos színű lapot kell tenni és egy tetszés szerinti lappal színt kérni. \nTehát ha piros lap lett felütve, a következő játékos addig húz a körbe rakott kártyákból, amíg piros színűt nem talál. \nEzt a kör közepére teszi és egy másik lappal színt kér a következő játékostól: pirosra makkot, makkra zöldet, stb. \nAki nem tud a kért színből tenni, a legfelső kártyával azonos színű lapot fel kell vennie. \nIlyenkor a tőle jobbra ülő játékos tehet le a felső lappal azonos színű kártyát és kérhet egy másikkal színt a szomszédjától. \nA játékot megnyeri az a játékos, aki utolsó lapját is a kör közepére tudta tenni. \n\nEnter lenyomásával léphet tovább....')

def jatekInditasa():
  system('cls')
  print('--Játék Indítása--')

  # jatekosok eltarolasa
  jatekosokSzama=input(f'\nAdja meg a játékosok neveit vesszővel elválasztva: ')
  jatekosokNevei = jatekosokSzama.strip().split(',')
  
  # jatekosok feallitasa
  for nev in jatekosokNevei:
    jatekosok2.append(nev)

  kozepen.clear()
  vege = 0
  

  while vege != 31:
    input(f'\nHúzás/rakás......\n')

    vege += 1
    

    for nev in jatekosokNevei:
      jatekosok[nev] =  pakliSzereploi[random.randint(0,3)]

    for index,value in zip(jatekosok.keys(),jatekosok.values()):
      print(f'\t|--{index}--| \t ||Kártyák||: \t  [{value}] \n')


    

      
    lerakas1 = input(f'\n(első játékos)Lerakás:  ')
    lerakas2 = input(f'\n(másik játékos)Lerakás:  \n')  
    lerakasok = [lerakas1,lerakas2]

    kozepen.append(jatekosok[jatekosok2[0]])
    kozepen.append(jatekosok[jatekosok2[1]])
     
    print(kozepen)

    if vege == 31:
      print('\n','-'*25,f'  {jatekosok2[0]} nyert, GRATULA! 💪','-'*25)

  input(f'\n \t Enter lenyomásával léphet tovább....')


 





