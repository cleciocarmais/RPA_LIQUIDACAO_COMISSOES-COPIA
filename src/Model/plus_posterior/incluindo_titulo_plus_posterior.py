import pyautogui as p
import traceback
import sys
sys.path.append('C:/RPA_O_MAIS_LINDO_DA_EQUIPE/RPA_LIQUIDACAO_COMISSOES')
from src.Model.global_clickApi import click2 as c
import pyperclip as pyp
import logging
from datetime import date
from src.Model.global_calculo_imposto import glob_calculo_valor
def incluir_titulo_plus_posterio(valor_notal_fiscal,numero_ns):
    data_vencimento = date.today().strftime("%d/%m/%y")
    p.sleep(3)
    img = 'C:/RPA/arquivos/images/'
    print('INICIANDO PROCESSO DE INCLUSAO DE TITULO PLUS POSTERIOR')
    logging.info(f'*INICIANDO DE INCLUSAO DE TITULO PLUS POSTERIOR ')   
    
    p.sleep(0.5)
    p.hotkey('alt','u') #acessando titulos
    p.sleep(0.5)
    p.press('Enter')

    ancora_lancemento = p.locateCenterOnScreen(f'{img}lancamentos1.png', confidence=0.95)
    while ancora_lancemento == None:
        p.sleep(1)
        ancora_lancemento = p.locateCenterOnScreen(f'{img}lancamentos1.png', confidence=0.95)
    p.sleep(1)
    incluir_tituto = p.locateCenterOnScreen(f'{img}incluir_titulo.png', confidence=0.95)
    if incluir_tituto != None:
       c(incluir_tituto.x, incluir_tituto.y)
  
    p.sleep(1)
    p.sleep(0.5)
    p.write('48438') #Nº SACADOR
    p.sleep(0.5)
    p.press("Tab")
    p.sleep(0.5)
    p.write(numero_ns)
    p.press('Tab')
    p.press("Tab")
    p.write('001')

    tipo_titulo = p.locateCenterOnScreen(f'{img}tipo_titulo.png', confidence=0.95)
    if tipo_titulo != None:
        c(tipo_titulo.x+50, tipo_titulo.y)
        p.sleep(0.5)
        p.write('PLUS POSTERIOR')
        p.sleep(0.5)
        p.press('Enter')
    
    
    p.sleep(0.5)
    vencimento = p.locateCenterOnScreen(f'{img}vencimento.png', confidence=0.95)
    if vencimento != None:
        c(vencimento.x, vencimento.y)
        p.press('Tab')
        p.sleep(1)
        p.write(data_vencimento)
        p.press('tab')
    else:
        p.press('Tab')
        p.press('Tab')
        p.press('Tab')
        p.write(data_vencimento)
        p.press('Tab')


    p.sleep(1)

    natOperacao = p.locateCenterOnScreen(f'{img}nat_operacao.png', confidence=0.85)
    if natOperacao != None:
        c(natOperacao.x+75, natOperacao.y)
        p.hotkey('ctrl','shift','right')
        p.press('backspace', presses=300)
        p.write('OC02') #campo nat opecação
        p.sleep(0.5)
        p.press('Tab')
        p.sleep(1)
    
        p.hotkey('ctrl','shift','right')
        p.press('backspace', presses=300)
        p.write("71310") #CONTA GERENCIAL
        p.sleep(1)
        p.press('Tab')
        p.write('VEICULOS NOVOS') # DEPARTAMENTOS
        p.sleep(0.5)
        p.press("tab")
        p.write('COBRANCA SIMPLES') #TIPO DE COBRANÇA

    inserir_valor = p.locateCenterOnScreen(f'{img}valor_titulo.png', confidence=0.95)
    if inserir_valor != None:
        c(inserir_valor.x+45, inserir_valor.y)
        p.sleep(0.5)
        valor_notal_fiscal = str(valor_notal_fiscal)
        p.write(valor_notal_fiscal.replace(".",","))
    else:
        print('ERRO AO INSERIR VALOR')
     
    
    
    pasta = p.locateCenterOnScreen(f'{img}pasta_titulo_incluir2.png', confidence=0.95)
    if pasta != None:
        c(pasta.x, pasta.y)
        while pasta != None:
            p.sleep(1)
            pasta = p.locateCenterOnScreen(f'{img}pasta_titulo_incluir2.png', confidence=0.95)
            print('Aguarde')

        p.sleep(1)
        p.write(f'PLUS POSTERIOR - BANCO HONDA SA {data_vencimento} \n \n N° NOTA FISCAL {numero_ns}')
        p.hotkey("alt","v")
    
    # fechar = p.locateCenterOnScreen(f'{img}fechar.png', confidence=0.95)
    # if fechar != None:
    #      c(fechar.x, fechar.y)
    p.sleep(1)
    confirma = p.locateCenterOnScreen(f'{img}confirma_incluir_titulo.png', confidence=0.95)
    if confirma != None:
        c(confirma.x, confirma.y)
    p.sleep(2)
    # fechar = p.locateCenterOnScreen(f'{img}fechar.png', confidence=0.95)
    # if fechar != None:
    #     c(fechar.x, fechar.y)
    p.hotkey('ctrl','c')
    numeoro_lancamento_plus_posterior = pyp.paste()
    p.sleep(1.5)
    fechar = p.locateCenterOnScreen(f'{img}fechar.png', confidence=0.95)
    if fechar != None:
        c(fechar.x, fechar.y)
    
    return numeoro_lancamento_plus_posterior
    
    

# incluir_titulo_plus_posterio(10242.28)

    


    