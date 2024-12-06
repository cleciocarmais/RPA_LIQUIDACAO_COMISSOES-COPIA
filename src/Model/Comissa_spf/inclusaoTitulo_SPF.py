import pyautogui as p
import logging
# from clickApi import click2 as c
import sys
sys.path.append(r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_COMISSOES')
from src.Model.global_clickApi import click2 as c
import pyperclip as pyp

def incluir_titulo_spf(id_cliente):
    img = 'C:/RPA/arquivos/images/'
    print('INICIANDO PROCESSO DE INCLUSÃO DE TITULO')
    logging.info('INICIANDO PROCESSO DE INCLUSÃO DE TITULO')
    print("aguarde!!!")
    p.hotkey('ctrl','c')
    id_lancamento_antigo = pyp.paste()
    print(f'lancemento antigo {id_lancamento_antigo}')
    p.press('Tab')
    p.sleep(0.5)
    p.press('esc')
    p.sleep(0.5)
    incluir_tituto = p.locateCenterOnScreen(f'{img}incluir_titulo.png', confidence=0.95)
    if incluir_tituto != None:
        c(incluir_tituto.x, incluir_tituto.y)
    p.sleep(1)
    tipo_titulo = p.locateCenterOnScreen(f'{img}tipo_titulo.png', confidence=0.95)
    if tipo_titulo != None:
        c(tipo_titulo.x+50, tipo_titulo.y)
        p.sleep(0.5)
        p.write('SPF')
        p.sleep(0.5)
        p.press('Enter')
    contra_apresentacao = p.locateCenterOnScreen(f'{img}contra_apresentacao.png', confidence=0.95)
   

    if contra_apresentacao != None:
        c(contra_apresentacao.x, contra_apresentacao.y)
    
    p.sleep(0.5)
    vencimento = p.locateCenterOnScreen(f'{img}vencimento.png', confidence=0.95)
    if vencimento != None:
        c(vencimento.x, vencimento.y)
    p.sleep(2)
    agente_cobrador = p.locateCenterOnScreen(f'{img}agente_cobrador.png', confidence=0.90)
    if agente_cobrador != None:
        c(agente_cobrador.x+80,agente_cobrador.y)
        p.write('VEÍCULOS (03)')
        p.sleep(0.5)
        p.press('Enter')
        p.sleep(0.5)
        p.press("Tab")
        p.sleep(0.5)
        p.press('down')
    else:
        p.alert('erro')
    # p.alert('passou')
    
    vendodor = p.locateCenterOnScreen(f'{img}vendedor_incluir_titulo.png', confidence=0.95)
    if vendodor != None:
        c(vendodor.x+76, vendodor.y)
        p.sleep(0.5)
        p.press('down')
        p.sleep(0.5)
        p.press('up')
        p.press('Enter')
    p.sleep(1)
    p.press('tab')
    p.hotkey('ctrl','c')
    valor_S = pyp.paste()
    p.hotkey("ctrl",'shift','right')
    p.press('backspace', presses=30)
    p.sleep(0.5)
    p.write(valor_S.replace('.',','))


    p.press("tab")
    p.sleep(1)
    pasta = p.locateCenterOnScreen(f'{img}pasta_titulo_incluir.png', confidence=0.95)
    if pasta != None:
        c(pasta.x, pasta.y)
    while pasta != None:
        p.sleep(1)
        pasta = p.locateCenterOnScreen(f'{img}pasta_titulo_incluir.png', confidence=0.95)
    codigo = p.locateCenterOnScreen(f'{img}observacao_codigo.png', confidence=0.95)
    if codigo != None:
        c(codigo.x+75, codigo.y)
        p.write(id_cliente)
        p.sleep(1)
        p.press('tab')
    p.sleep(1)
    voltar = p.locateCenterOnScreen(f'{img}volta_observacao.png', confidence=0.95)
    if voltar != None:
        c(voltar.x, voltar.y)
    p.sleep(1)
    confirma = p.locateCenterOnScreen(f'{img}confirma_incluir_titulo.png', confidence=0.95)
    if confirma != None:
        c(confirma.x, confirma.y)
    else:
        p.alert('olaaaaaaaaaaaaa')
    p.sleep(2)
    # fechar = p.locateCenterOnScreen(f'{img}fechar.png', confidence=0.95)
    # if fechar != None:
    #     c(fechar.x, fechar.y)
    p.hotkey('ctrl','c')
    id_lancamento_novo = pyp.paste()
      # id_lancamento_novo = '2636241'
    # id_lancamento_antigo = '454545'
    p.sleep(1)
    fechar = p.locateCenterOnScreen(f'{img}fechar.png', confidence=0.95)
    if fechar != None:
        c(fechar.x, fechar.y)

    # id_lancamento_novo = '2636668'
    # id_lancamento_antigo = '2636668'
    
    return id_lancamento_antigo, id_lancamento_novo
    

    


    


# if __name__=='__main__':
#     p.sleep(2)
# cliente = {'datas' : '01/02/2024 09:28:27','nome' : 'CLAUDINEUDA DA SILVA SOUSA','Valor total nf' : '1944.31', 'valor_pessoal' : '1944,31', 'empresa' : 'NOVALUZ WS','id_cliente' : '0478551'}
# print(cliente)
# incluir_titulo_spf(cliente['id_cliente'])

# print(__name__)
    
    


# 1894222