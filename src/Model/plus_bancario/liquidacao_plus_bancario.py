import logging
import pyautogui as p
# from clickApi import click2 as c
import sys
# sys.path.append('C:/RPA_O_MAIS_LINDO_DA_EQUIPE/RPA_LIQUIDACAO_COMISSOES')
from src.Model.global_clickApi import click2 as c
import traceback
from src.Model.global_calculo_imposto import glob_imposto_irrf
# from calculo_imposto import imposto_irrf  5693,46 
# from muda_empresa2 import muda_empresa_contas_a_receber
from datetime import timedelta, datetime, date
import traceback
import pyperclip as pyp
from src.Model.token import SetToken, GetToken
numeroDocumentoControlado = 0

def realizaLiquidacao_plus_bancario(pessoa,flag):

    """
      REALIZA IRRF E LIQUIDACAO 
    
    
    
    ----- PARAMENTROS ------
        FLAG  - > BOOLONG\n
        DICIONARIO COM AS SEGUINTE CHAVES : \n
        'Valor' \n
        'Valor total nf'\n
        'Empresa'\n
        'datas \n

    ---- RETORNO ---- \n

        RETORNA RESULTADO DA LIQUIDACAO : \n 
        VALOR DIVERGENTE \n
        TRUE - > LIQUIDACAO REALIZADA \n
        FALSE - > LIQUIDACAO N REALIZADA
    """ 
    
    global numeroDocumentoControlado
    infor = GetToken()
    if flag:

        numeroDocumentoControlado = 0
    try :
        print("REALIZANDO LIQUIDACAO PLUS BANCARIO")
        logging.info("REALIZANDO LIQUIDACAO PLUS BANCARIO")
        print("aguarde!!")
        # SALVANDO NUMERO_LANCAMENTO 

        p.sleep(2)
        valor_cliente= pessoa['valor']
        valor_nf = pessoa['Valor total nf']
        p.hotkey('ctrl','c')
        LANCAMENTO = pyp.paste()
        
        img = 'C:/RPA/arquivos/images/'
        p.press('Tab')
        p.sleep(1)
        creditos_debitos = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)
        while creditos_debitos == None:
            p.sleep(0.5)
            print('Carregando pagina titutos')
            creditos_debitos = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)

        else:
            logging.info('  Erro ao processa varivael creditos_debitos')
        p.sleep(1)
        p.press('Esc')
        p.sleep(1)

        incluir_tituto = p.locateCenterOnScreen(f'{img}incluir_titulo.png', confidence=0.95)
        if incluir_tituto != None:
            c(incluir_tituto.x, incluir_tituto.y)

        p.sleep(0.5)

        valor_titulo = p.locateCenterOnScreen(f'{img}valor_titulo.png', confidence=0.95)
        if valor_titulo != None:
            c(valor_titulo.x+75, valor_titulo.y)
            p.press("End")
            p.hotkey('ctrl','c')

        valorDealer = pyp.paste()
        valorDealer = valorDealer.replace('.',"")
        valorDealer = valorDealer.replace(',','.')


        p.sleep(1)
        p.press('Esc')
        p.sleep(0.5)
        p.write(LANCAMENTO)
        p.press('tab')
        p.sleep(1)
        list_ta = valor_cliente.split(".")
        if len(list_ta[1]) == 1:
            valor_cliente+= "0"
        p.sleep(1)

        if valorDealer != valor_cliente:
            print("Identificado valor divergente")
            logging.info("Identificado valor divergente")
            print(type(valor_cliente))
            print(type(valorDealer))
            fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
            while fechar != None:
                print("aguarde")
                c(fechar.x, fechar.y)
                p.sleep(1)
                fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
            return 'divergente'



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

        print('INICIALIZANDO PROCESSO DE INCLUSÃO IRRF')
        logging.info('INICIALIZANDO PROCESSO DE INCLUSÃO IRRF')
        incluir = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if incluir != None:
            c(incluir.x,incluir.y)
        else:
            print('  Erro ao processo variavel incluir')
        p.sleep(1)

        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while creditos_debitos2 == None:
            p.sleep(0.5)
            print("  aguarade tela de inclusão aparace")
            creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        p.sleep(1)
        if creditos_debitos2 != None:
            c(creditos_debitos2.x+70, creditos_debitos2.y)

        else:
            logging.info('Erro ao processa variavel creditos_debitos2')  

        p.write("IRRF RETIDO (-)(-)(31)")
        p.press('Enter')
        p.sleep(2)
        p.press("Tab") # buscando informaçoes
        p.sleep(1)
        p.press("Tab") # pula data movimento 
        p.sleep(1)
        p.press("Tab") # pula data de caixa
        p.sleep(1)
   
        p.sleep(0.5)

        p.hotkey('ctrl','shift','right')   
        p.press('backspace', presses=300)
        print(valorDealer)
        print(valor_cliente)

        
        valor_finals = glob_imposto_irrf(valor_cliente)

        p.write(valor_finals)
        p.press("Tab")
        p.sleep(1)
        p.write('IRRF')
    
        p.sleep(1)
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
            p.alert('ola')
        print("PROCESSO FINALIZAD DE IRRF")
        # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        # if cancelar != None:
        #     c(cancelar.x,cancelar.y)
# 2637665
###################################################     LIQUIDAÇÃO      ###################################################


        p.sleep(3)
        print('INCIANDO PROCESSO DE LIQUIDACAO')
        logging.info('INCIANDO PROCESSO DE LIQUIDACAO')

        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while creditos_debitos2 != None:
            p.sleep(1)
            creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        p.sleep(1)

        incluir2 = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if incluir2 != None:
            c(incluir2.x, incluir2.y)
        
        p.sleep(1)

        incluir3 = p.locateCenterOnScreen(f'{img}incluir6.png', confidence=0.95)
        if incluir3 != None:
            c(incluir3.x,incluir3.y)
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
            if pessoa['Empresa'] != 'NOVALUZ SUL':
                p.write('SANTANDER TERRALUZ (Z8)')
            else:
                p.write('SANTANDER TERRALUZ (ZV)')

            p.press("Enter")
            p.sleep(1)
            p.press('Tab')
        p.sleep(1)

        if numeroDocumentoControlado == 0 and GetToken()["numero_lanc"] == 0:
            print('PRIMEIRA CONSULTA DO GRUPO')
            lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
            if lancamento != None:
                c(lancamento.x+150, lancamento.y)
            p.sleep(1)
            dia = pessoa['datas'][0:2]
            mes = pessoa['datas'][3:5]
            ano = pessoa['datas'][6:-8]
            p.write(f'{dia}{mes}{ano[2:-1]}')
            p.press("Tab")
            data_atual = date(int(ano),int(mes),int(dia))
            data_futura = data_atual + timedelta(days=3)
            data_formatada = date.today()
            p.write(data_formatada.strftime('%d%m%y'))
            # p.write('200224')

            p.press("Tab")
            valor_liquito = float(valor_nf) * (100-1.5) / 100
            valor_round = round(valor_liquito, 2)
            valor_final = str(valor_round)
            valor_f = valor_final.replace('.',',')


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
            SetToken(lanc=numeroDocumentoControlado)
            print(numeroDocumentoControlado)
            p.press('Tab')
            p.sleep(1)

            btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
            if btn_ok02 !=None:
                c(btn_ok02.x, btn_ok02.y)
            p.sleep(2)
            excessao_titulo = p.locateCenterOnScreen(f'{img}excessao_titulo.png', confidence=0.95)
        
            if excessao_titulo != None:
                print(" Execessao encontrada")
                logging.info('  Excessao encontrada')
                p.press('Enter')
            # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
            # if cancelar != None:
            #     c(cancelar.x,cancelar.y)
        else:

            lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
            if lancamento != None:
                c(lancamento.x+55, lancamento.y)
                p.write(infor["numero_lanc"])
                p.press('Tab')

            btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
            if btn_ok02 !=None:
                c(btn_ok02.x, btn_ok02.y)
            p.sleep(1.5)
            excessao_titulo = p.locateCenterOnScreen(f'{img}excessao_titulo.png', confidence=0.95)
            if excessao_titulo != None:
                print(" Execessao encontrada")
                logging.info('  Excessao encontrada')
                p.press('Enter')
            # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
            # if cancelar != None:
            #     c(cancelar.x,cancelar.y)
        
        p.sleep(3)
        fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
        while fechar != None:
            print("aguarde")
            c(fechar.x, fechar.y)
            p.sleep(1.5)
            fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)

        print("PROCESSO FINALIZADO !! ")
        logging.info("PROCESSO FINALIZADO !! ")
        return True
    except:
        fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
        while fechar != None:
            print("aguarde")
            c(fechar.x, fechar.y)
            p.sleep(1.5)
            fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
        erro = traceback.format_exc()
        print(erro)
        return False
    
   
   
   
    










#TODO ALTERAR VALORES FINAIS
# img = 'C:/RPA/arquivos/images/'
# index = 0
# p.sleep(4)
# print('vai')
# pessoas = [
# {'nome': 'SANDRO RIOS SILVEIRA', 'valor': '240.0', 'Emp fandi': 'NOVALUZ WS', 'Valor total nf': 5780.16, 'Empresa': 'NOVALUZ WS', 'datas': '23/04/2024 17:29:42'}    ]
# for index,pessoa in enumerate(pessoas):
#     realizaLiquidacao(pessoa)
    # print('INCIANDO PROCESSO DE LIQUIDACAO')
    # logging.info('INCIANDO PROCESSO DE LIQUIDACAO')
    # incluir = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
    # if incluir != None:
    #     c(incluir.x,incluir.y)
    # else:
    #     print('  Erro ao processo variavel incluir')

    # creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
    # while creditos_debitos2 == None:
    #     p.sleep(0.5)
    #     print("  aguarade tela de inclusão aparace")
    #     creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
    # if creditos_debitos2 != None:
    #     c(creditos_debitos2.x+70, creditos_debitos2.y)

    # else:
    #     logging.info('Erro ao processa variavel creditos_debitos2')  

    # print("  Selecioando tipo de Credito/Debito")
    # logging.info("  Selecioando tipo de Credito/Debito")
    # p.write("LIQUIDAÇÃO(-)(01)")
    # p.press('Tab')
    # p.sleep(1)
    # ag_cobrador = p.locateCenterOnScreen(f'{img}ag_cobrador.png', confidence=0.95)
    # if ag_cobrador != None:
    #     c(ag_cobrador.x+55, ag_cobrador.y)
    #     p.write('SANTANDER TERRALUZ (Z8)')
    #     p.press("Enter")
    #     p.sleep(1)
    #     p.press('Tab')
    # p.sleep(1)
    # # for pesso in pessoas:
    # #     realizaLiquidacao(pesso)
    # if index == 0:
    #     lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
    #     if lancamento != None:
    #         c(lancamento.x+150, lancamento.y)
    #     p.sleep(1)
    #     p.write('01/02/24')
    #     p.press("Tab")
    #     p.write('15/02/24')
    #     p.press("Tab")
    #     p.write('5078,51')
    #     p.press('Tab')
    #     p.write('5078,51')
    #     p.press('Enter')
    #     p.sleep(4)
    #     sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
    #     if sem_dados == None:
    #         p.press('Enter')
    #     p.sleep(2)
    #     # lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
    #     # if lancamento != None:
    #     p.hotkey('ctrl', 'c')
    #     p.sleep(1)
    #     numero_lancamento = pyp.paste()
    #     print(id_lancamento)
    #     p.press('Tab')
    # else:
    #     lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
    #     if lancamento != None:
    #         c(lancamento.x+55, lancamento.y)
    #         p.write(id_lancamento)
    #         p.press('Tab')
    



