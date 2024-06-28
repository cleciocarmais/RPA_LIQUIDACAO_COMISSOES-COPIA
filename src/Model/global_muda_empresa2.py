from src.Model.global_clickApi import click2 as c
import pyautogui as p
import logging
                       
def muda_empresa(name):
     
    ########### COORDENADAS DO BOT�O MUDA EMPRESA PARA CADA M�DULO DO DEALER ###############
    # M�DULO OFICINA - p.click(454,53)
    # M�DULO ESTOQUE - p.click(159,53)
    # M�DULO CONTAS A RECEBER - p.click(164,53)
    # M�DULO CONTAS A PAGAR - p.click(189,53)
    # M�DULO CONTROLE BANCARIO - p.click(147,57)
    ########################################################################################

    p.click(147,57)# Clica em Mudar Empresa - VAI MUDAR COORDENADAS DEPENDENDO DO M�DULO DO DEALER
    p.click(706,378) # Clicar na select box
    p.scroll(2000) # Subir todas as op��es, para iniciar a busca do come�o da lista de empresas
    if name in ['NOVALUZ BS','NOVALUZ SD', 'NOVALUZ WS']:
        name = 'NOVALUZ BS'

    empresa = p.locateCenterOnScreen('C:/RPA/arquivos/images/muda_empresa/' + name + '.png', confidence = 0.95)
    while empresa == None:
        p.click(861,627)
        # seta = p.locateCenterOnScreen('C:/RPA/arquivos/images/muda_empresa/seta_me.png', confidence = 0.95)
        # c(seta.x , seta.y )
        empresa = p.locateCenterOnScreen('C:/RPA/arquivos/images/muda_empresa/' + name + '.png', confidence = 0.95)
    c(empresa.x,empresa.y)

    p.click(755,446)# Clica em OK
    p.sleep(0.5)
    p.press('Enter')
    p.sleep(0.5)

    bd_sem_backup = p.locateCenterOnScreen('C:/RPA/arquivos/images/bd_sem_backup.png', confidence = 0.95)
    if bd_sem_backup != None:
        print('achei bd sem backup')
        ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok3.png', confidence = 0.95)
        if ok != None:
            c(ok.x, ok.y )
        else:
            print('Nao achei botao ok')
    else:
        print('nao achei bd sem backup')
    p.sleep(0.5)
    
    print('Mudado para empresa: ' + name)
    logging.info('Mudado para empresa: ' + name)
    p.sleep(0.5)

    cancelar = p.locateCenterOnScreen('C:/RPA/arquivos/images/cancelar.png', confidence = 0.95)
    while cancelar != None:
        p.sleep(0.5)
        cancelar = p.locateCenterOnScreen('C:/RPA/arquivos/images/cancelar.png', confidence = 0.95)
    p.sleep(1)

def muda_empresa_contas_a_receber(name):
     
    ########### COORDENADAS DO BOT�O MUDA EMPRESA PARA CADA M�DULO DO DEALER ###############
    # M�DULO OFICINA - p.click(454,53)
    # M�DULO ESTOQUE - p.click(159,53)
    # M�DULO CONTAS A RECEBER - p.click(164,53)
    # M�DULO CONTAS A PAGAR - p.click(189,53)
    # M�DULO CONTROLE BANCARIO - p.click(147,57)
    ########################################################################################

    p.click(164,53)# Clica em Mudar Empresa - VAI MUDAR COORDENADAS DEPENDENDO DO M�DULO DO DEALER
    p.sleep(1)
    p.click(706,378) # Clicar na select box
    p.sleep(1)
    p.scroll(2000) # Subir todas as op��es, para iniciar a busca do come�o da lista de empresas
    p.sleep(1)
    empresa = p.locateCenterOnScreen('C:/RPA/arquivos/images/muda_empresa/' + name + '.png', confidence = 0.95)
    while empresa == None:
        p.click(861,629)
        # seta = p.locateCenterOnScreen('C:/RPA/arquivos/images/muda_empresa/seta_me.png', confidence = 0.95)
        # c(seta.x , seta.y )
        p.sleep(1)
        empresa = p.locateCenterOnScreen('C:/RPA/arquivos/images/muda_empresa/' + name + '.png', confidence = 0.95)
    c(empresa.x,empresa.y)
    p.sleep(1)
    p.click(755,446)# Clica em OK
    p.sleep(0.5)
    
    p.press("Enter")

    bd_sem_backup = p.locateCenterOnScreen('C:/RPA/arquivos/images/bd_sem_backup.png', confidence = 0.95)
    if bd_sem_backup != None:
        print('achei bd sem backup')
        ok = p.locateCenterOnScreen('C:/RPA/arquivos/images/ok3.png', confidence = 0.95)
        if ok != None:
            print('achei botao ok')
            c(ok.x, ok.y )
        else:
            print('Nao achei botao ok')
    else:
        print('nao achei bd sem backup')
    p.sleep(0.5)
    
    print('Mudado para empresa: ' + name)
    logging.info('Mudado para empresa: ' + name)
    p.sleep(0.5)

    cancelar = p.locateCenterOnScreen('C:/RPA/arquivos/images/cancelar.png', confidence = 0.95)
    while cancelar != None:
        p.sleep(0.5)
        cancelar = p.locateCenterOnScreen('C:/RPA/arquivos/images/cancelar.png', confidence = 0.95)
    p.sleep(1)
            
