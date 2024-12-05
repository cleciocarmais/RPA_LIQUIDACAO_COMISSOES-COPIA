import pyautogui as p
import logging
# from clickApi import click2 as c
from src.Model.global_clickApi import click2 as c

def anulacao_titulo_spf(lancamento_antigo = "2390304",lancameto_novo = None):
    print("ANULAÇAO DE TITULO")
    logging.info('ANULACAO DE TITIULO')
    img = 'C:/RPA/arquivos/images/'
  
    p.hotkey("alt", 'u')
    p.sleep(0.5)
    p.press('Enter')
    ancora_titulo = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)
    while ancora_titulo == None:
        p.sleep(1)
        print("aguarde")
        ancora_titulo = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)
    p.write(lancamento_antigo)
    p.sleep(1)
    p.press('Tab')
    p.sleep(1)
    creditos_debitos = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)
    while creditos_debitos == None:

        p.sleep(0.5)
        print('    carregando pagina titutos')
        creditos_debitos = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)

    else:
        logging.info('  Erro ao processa varivael creditos_debitos')

    creditos_debitos = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)
    if creditos_debitos != None:
        c(creditos_debitos.x, creditos_debitos.y)
    else:
        logging.info('  Erro ao processa o valor da variavel creditos_debitos')

    p.sleep(1)
    mensagem_saldo = p.locateCenterOnScreen(f'{img}erro_critico2.png', confidence=0.95)
    if mensagem_saldo != None:
        p.sleep(1)
        btn_bok_ok = p.locateCenterOnScreen(f'{img}ok100.png', confidence=0.90)
        if btn_bok_ok != None:
            c(btn_bok_ok.x, btn_bok_ok.y)
        else:
            print('    Erro ao processa variavel btn_bok_ok')
    else:
        logging.info('  Erro ao processa variavel erro_critico')
    p.sleep(2)
    incluir = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
    if incluir != None:
        c(incluir.x,incluir.y)
    else:
        print('  Erro ao processo variavel incluir')

    creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
    while creditos_debitos2 == None:
        p.sleep(0.5)
        print("  aguarade tela de anulacao aparace")
        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
    if creditos_debitos2 != None:
        c(creditos_debitos2.x+70, creditos_debitos2.y)

    else:
        logging.info('Erro ao processa variavel creditos_debitos2')  

    print("  Selecioando tipo de Credito/Debito")
    logging.info("  Selecioando tipo de Credito/Debito")
    p.write("ANULAÇÃO TÍTULO AVULSO (0)(-)(50)")
    p.press('ENTER')
    p.press("tab")
    p.sleep(0.5)
    p.press("tab")
    p.sleep(0.5)
    p.press("tab")
    p.sleep(1)
    p.write(f'ANULADO CONF LANC {lancameto_novo}')
 
    p.sleep(0.5)
    p.press("Tab")
    p.press("Tab")
    
    p.write('AV.LANCTO')
    p.sleep(1)
    btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
    if btn_ok02 !=None:

        c(btn_ok02.x, btn_ok02.y)
    p.sleep(3)

    # cancela = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
    # if cancela !=None:
    #     c(cancela.x, cancela.y)
    fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
    if fechar != None:
        print("aguarde")
        c(fechar.x, fechar.y)
    p.press("Esc")
    p.write(lancameto_novo)


    

if __name__=="__main__":
    p.countdown(4)
    anulacao_titulo_spf()