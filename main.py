from functions import *
from os import system

valasztott=''
while valasztott!='0':
    valasztott=menu()
    if valasztott=='1':
       pakliKiir()
    elif valasztott=='2':
        utmutatoKiir()
    elif valasztott=='3':
        jatekInditasa()