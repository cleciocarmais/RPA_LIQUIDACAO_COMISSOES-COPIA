import logging
import pyautogui as p
# from clickApi import click2 as c
from src.Model.global_clickApi import click2 as c
import traceback
from src.Model.global_calculo_imposto import glob_imposto_irrf
# from calculo_imposto import imposto_irrf
# from muda_empresa2 import muda_empresa_contas_a_receber
from datetime import timedelta, datetime, date
import traceback
import pyperclip as pyp
numeroDocumentoControlado = 0

def liquidacao_plus_posterior(info_plus_posterior,numero_lancamento_gerado):
    """
        REALIZADA LIQUIDACAO DO TITULO GERANDO ANTERIOMENTE\n

        ---------------- ARGUMENTOS ------------------------\n
        DICIONARIO DE INFORMAÇOES CONTENDO SEGUINTES CHAVES:\n
        NUMERO GERADO PELO LANCAMENTO\n

        ------------------ RETORNO --------------------------\n

        RETORNA UM BOOLANG, TRUE DE LIQUIDACAO REALIZADA OU  \n
        FALSE DE LIQUIDACAO N REALIZADA 


        -+--+---+---+---+----+----+---+--+--+-----+--+-----+---

    
    """
    try :
        # SALVANDO NUMERO_LANCAMENTO 
        p.hotkey('alt','u')
        p.sleep(1)
        p.press('Enter')
        p.sleep(2)
        valor_plus_posterior = info_plus_posterior['Valor total nf']
        valor_nf = info_plus_posterior['Valor total nf']
        
        img = 'C:/RPA/arquivos/images/'
        # p.press('Tab')
        p.sleep(1)
        p.press('Esc')
        p.sleep(1)
       
        p.sleep(0.5)
        p.write(numero_lancamento_gerado)

        p.press('tab')
        p.sleep(1)
     
        p.sleep(0.5)

        creditos_debitos = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)
        while creditos_debitos == None:
            p.sleep(0.5)
            print('carregando pagina titutos')
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

        print('INICIALIZANDO PROCESSO DE INCLUSÃO IRRF PLUS POSTERIOR')
        logging.info('INICIALIZANDO PROCESSO DE INCLUSÃO IRRF PLUS POSTERIOR')
        incluir = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if incluir != None:
            c(incluir.x,incluir.y)
        else:
            print('  Erro ao processo variavel incluir')

        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while creditos_debitos2 == None:
            p.sleep(0.5)
            print("  aguarade tela de inclusão aparace")
            creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)

        if creditos_debitos2 != None:
            c(creditos_debitos2.x+70, creditos_debitos2.y)
        else:
            logging.info('Erro ao processa variavel creditos_debitos2')  

        p.write("IRRF RETIDO (-)(-)(31)")
        p.press('Enter')
        p.sleep(2)
        p.press("Tab")
        p.sleep(1)
        p.press("Tab")
        p.sleep(1)
        p.press("Tab")
        p.sleep(1)
   
        p.sleep(0.5)
 
        p.hotkey('ctrl','shift','right')
        p.press('backspace', presses=300)
        
        valor_finals = glob_imposto_irrf(valor_plus_posterior)

        p.write(valor_finals)
        p.press("Tab")
        p.sleep(1)
        p.write('IRRF')
        p.press("Tab")
        p.sleep(0.5)

        documento_tipo = p.locateCenterOnScreen(f'{img}documento_tipo.png', confidence=0.95)
        if documento_tipo != None:
            c(documento_tipo.x+50, documento_tipo.y)
        else:
            p.alert('Erro durante execucao')

        p.sleep(0.5)
        p.write('AV.LANCTO')
        p.sleep(0.5)
        p.press('Enter')
        p.sleep(2)

        btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
        if btn_ok02 !=None:
            c(btn_ok02.x, btn_ok02.y)
        else:
            logging.info('Erro ao processa variavel cancela')
            print('erro')


        #TODO N EXCLUIR ESTE COMENTARIO
        # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        # if cancelar != None:
        #     c(cancelar.x,cancelar.y)

###################################################     LIQUIDAÇÃO      ###################################################


        p.countdown(4)
        print('INCIANDO PROCESSO DE LIQUIDACAO PLUS POSTERIOR')
        logging.info('INCIANDO PROCESSO DE LIQUIDACAO PLUS POSTERIOR')

        titulo_creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while titulo_creditos_debitos2 != None:
            p.sleep(1)
            titulo_creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)

        p.sleep(1)
        btn_incluir = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if btn_incluir != None:
            c(btn_incluir.x, btn_incluir.y)
        
        p.sleep(1)

        btn_incluir3 = p.locateCenterOnScreen(f'{img}incluir6.png', confidence=0.95)
        if btn_incluir3 != None:
            c(btn_incluir3.x,btn_incluir3.y)
        else:
            print('  Erro ao processo variavel incluir')

        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while creditos_debitos2 == None:
            p.sleep(0.5)
            print("  aguarade tela de inclusão aparace")
            creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        if creditos_debitos2 != None:
            c(creditos_debitos2.x+70, creditos_debitos2.y)

        else:
            logging.info('  Erro ao processa variavel creditos_debitos2')  

        print("  Selecioando tipo de Credito/Debito")
        logging.info("  Selecioando tipo de Credito/Debito")
        p.write("LIQUIDAÇÃO(-)(01)")
        p.press('Tab')  
        p.sleep(0.5)
        p.press('Tab')
        p.sleep(0.5)  
        p.press('Tab')
        p.sleep(0.5)  
        p.write('LIQUIDACAO')
        p.sleep(1)
        ag_cobrador = p.locateCenterOnScreen(f'{img}ag_cobrador.png', confidence=0.95)
        if ag_cobrador != None:
            c(ag_cobrador.x+55, ag_cobrador.y)
            p.write('SANTANDER TERRALUZ (Z8)')
            p.press("Enter")
            p.sleep(1)
            p.press('Tab')
        p.sleep(1)

    
        print('Primeira consulta do grupo')
        lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
        if lancamento != None:
            c(lancamento.x+150, lancamento.y)
        p.sleep(1)
        dia = info_plus_posterior['datas'][0:2]
        mes = info_plus_posterior['datas'][3:5]
        ano = info_plus_posterior['datas'][6:-8]
        p.write(f'{dia}{mes}{ano[2:-1]}')
        p.press("Tab")
        data_atual = date(int(ano),int(mes),int(dia))
    
        data_formatada = date.today()
        p.write(data_formatada.strftime('%d%m%y'))
        # p.write('200224')

        p.press("Tab")
        valor_liquito = float(valor_nf) * (100-1.5) / 100
        valor_round = round(valor_liquito, 2)
        valor_final = str(valor_round)
        valor_f = valor_final.replace('.',',')


        print(' Calculo realizado')
        logging.info(' Calculo realizado')

        print(' Inserindo valor liquido')
        logging.info(' Inserindo valor liquido')
        p.write(valor_f)
        p.press('Tab')
        p.write(valor_f)
        p.sleep(1)
        p.press('Enter')
        p.sleep(4)
        sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
        if sem_dados == None:
            p.press('Enter')
        p.sleep(2)
        # lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
        # if lancamento != None:
        p.hotkey('ctrl', 'c')
        p.sleep(1)
        
        numeroDocumentoControlado = pyp.paste()
        print(numeroDocumentoControlado)
        p.press('Tab')
        p.sleep(1)

        btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
        if btn_ok02 !=None:
            c(btn_ok02.x, btn_ok02.y)
        p.sleep(2)
        excessao_titulo = p.locateCenterOnScreen(f'{img}excessao_titulo.png', confidence=0.95)
        print(" Conferir se tem excessao")
        logging.info("  Conferir se tem excessao")
        if excessao_titulo != None:
            print(" Execessao encontrada")
            logging.info('  Excessao encontrada')
            p.press('Enter')
        # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        # if cancelar != None:
        #     c(cancelar.x,cancelar.y)
        
        return True
    except:
        erro = traceback.format_exc()
        logging.info(erro)
        return False
    
   
   
   
    








if __name__=='__main__':
    
   #TODO ALTERAR VALORES FINAIS
    img = 'C:/RPA/arquivos/images/'
    index = 0
    p.sleep(4)
    print('vai')
    pessoas = [
        {'datas' : '01/02/2024 09:28:27','nome' : 'ESTEFANIA MARIA ROCHA SILVA','Valor total nf' : '9700.23', 'valor' : '360.0', 'empresa' : 'NOVALUZ BS','id_cliente' : '0478496'},
        {'datas' : '01/02/2024 09:28:27','nome' : 'ESTEFANIA MARIA ROCHA SILVA ','Valor total nf' : '9700.23', 'valor' : '360.0', 'empresa' : 'NOVALUZ BS','id_cliente' : '0478496'},
    ]
    for index,pessoa in enumerate(pessoas):
        liquidacao_plus_posterior(pessoa)
