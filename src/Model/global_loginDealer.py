from src.Model.global_clickApi import click2 as c

import os
import logging
import pyautogui as p

def login_dealer_controle_bancario():
    print('Logando no Dealer Controle Bancario')
    logging.info('Logando no Dealer Controle Bancario')

    # Buscar as credenciais de acesso ao Dealernet
    # os.chdir('C:\RPA\credenciais')
    credenciais = open('C:\RPA\credenciais\login_dealer.txt','r')
    chaves = credenciais.readlines()
    credenciais.close()

    login = chaves[0][:-1]
    password = chaves[1]
    p.PAUSE=1
    os.startfile("C:\Conces\scb\scb.exe")
    p.sleep(3)
    usuario = p.locateCenterOnScreen('C:/RPA/arquivos/images/usuario.png', confidence = 0.95)

    if usuario != None:
        c(usuario.x+70 , usuario.y )
        p.press('delete', presses=200)
        p.sleep(1)
        p.write(login)



    senha = p.locateCenterOnScreen('C:/RPA/arquivos/images/senha.png', confidence = 0.95)
    if senha != None:
        c(senha.x+80 , senha.y )
        p.write(password)


    ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok.png', confidence = 0.95)
    if ok != None:
        c(ok.x, ok.y )

    p.sleep(2)

    ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok.png', confidence = 0.95)
    while ok != None:
        p.sleep(0.5)
        ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok.png', confidence = 0.95)
    # p.press(0.5)
    p.press("Enter")
    p.sleep(1)

    bd_sem_backup = p.locateCenterOnScreen('C:/RPA/arquivos/images/bd_sem_backup.png', confidence = 0.95)
    if bd_sem_backup != None:
        print('Achei bd sem backup')
        ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok3.png', confidence = 0.95)
        if ok != None:
            c(ok.x, ok.y )
        else:
            print('nao achei botao ok')
    else:
        print('Nao achei bd sem backup')
    p.sleep(1)
    
    cancelar = p.locateCenterOnScreen('C:/RPA/arquivos/images/cancelar.png', confidence = 0.95)
    while cancelar != None:
        p.sleep(0.5)
        cancelar = p.locateCenterOnScreen('C:/RPA/arquivos/images/cancelar.png', confidence = 0.95)
    p.sleep(1)
    
def login_dealer_contas_receber():

    logging.info('Logando Contar_receber')

    # Buscar as credenciais de acesso ao Dealernet
    # os.chdir('C:\RPA\credenciais')
    credenciais = open('C:\RPA\credenciais\login_dealer.txt','r')
    chaves = credenciais.readlines()
    credenciais.close()

    login = chaves[0][:-1]
    password = chaves[1]
    p.PAUSE=1
    os.startfile("C:\Conces\scr\scr.exe")
    p.sleep(3)
    usuario = p.locateCenterOnScreen('C:/RPA/arquivos/images/usuario.png', confidence = 0.95)

    if usuario != None:
        print('processo 01')
        c(usuario.x+70 , usuario.y )
        p.press('delete', presses=200)
        
        p.sleep(1)

        p.write(login)



    senha = p.locateCenterOnScreen('C:/RPA/arquivos/images/senha.png', confidence = 0.95)
    if senha != None:
        c(senha.x+80 , senha.y )
        p.write(password)


    ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok.png', confidence = 0.95)
    if ok != None:
        c(ok.x, ok.y )

    p.sleep(2)

    ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok.png', confidence = 0.95)
    while ok != None:
        p.sleep(0.5)
        ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok.png', confidence = 0.95)
    p.sleep(0.5)
    p.press("Enter")
    p.sleep(1)

    bd_sem_backup = p.locateCenterOnScreen('C:/RPA/arquivos/images/bd_sem_backup.png', confidence = 0.95)
    if bd_sem_backup != None:
        print('Achei bd sem backup')
        ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok3.png', confidence = 0.95)
        if ok != None:
            print('Achei botao ok')
            c(ok.x, ok.y )
        else:
            print('nao achei botao ok')
    else:
        print('Nao achei bd sem backup')
    p.sleep(1)
    
    cancelar = p.locateCenterOnScreen('C:/RPA/arquivos/images/cancelar.png', confidence = 0.95)
    while cancelar != None:
        p.sleep(0.5)
        cancelar = p.locateCenterOnScreen('C:/RPA/arquivos/images/cancelar.png', confidence = 0.95)
    p.sleep(1)



