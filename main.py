from functions import*
from os import system

választott=''
while választott!='0':
    választott=menu()
    if választott=='1':
       pakliKiir()
    elif választott=='2':
        utmutatoKiir()
    elif választott=='3':
        pass