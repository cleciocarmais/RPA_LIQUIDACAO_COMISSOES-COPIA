import pyautogui as p
import logging
from datetime import timedelta, datetime, date
import sys

sys.path.append(r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_COMISSOES')
from src.Model.global_clickApi import click2 as c
from src.Model.global_calculo_imposto import glob_calculo_valor

#MODULO ACESSA CONTROLE BANCARIO E PESQUISA VALOR COM DESCONTO DO IMPOSTO

def pesquisar_valor_comissa_spf(conta,data,valor):
    print("*BUSCANDO VALOR VALOR COMISSAO SPF")
    logging.info("*BUSCANDO  VALOR COMISSAO SPF")
    print(data)
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:-8]
    img = 'C:/RPA/arquivos/images/'    
    print("Aguarde!!!")
    logging.info("Aguarde!!!")

    lanca = p.locateCenterOnScreen('C:/RPA/arquivos/images/lancamentos_scb.png', confidence=0.95)
    if lanca != None:
        c(lanca.x, lanca.y)
    p.sleep(2)
    p.write(conta)
    p.press("Tab")
    p.sleep(1)
    p.write(f'{dia}{mes}{ano[2:-1]}')
    p.press('Tab')
    p.sleep(1)
    data_futura = date.today()
    data_formatada = data_futura.strftime('%d%m%y')
    p.write(data_formatada)
    p.press("Tab")
    p.sleep(2)


    result_lançamentos2 = p.locateCenterOnScreen('C:/RPA/arquivos/images/tabela_branco.png', confidence=0.95)
    while result_lançamentos2 != None:
        p.sleep(2)
        print(" aguarde")
        result_lançamentos2 = p.locateCenterOnScreen('C:/RPA/arquivos/images/tabela_branco.png', confidence=0.95)
    p.sleep(2)
  
    contendo = p.locateCenterOnScreen(f'{img}contendo4.png', confidence=0.95)
    p.sleep(1)

    if contendo != None:
        c(contendo.x+45, contendo.y)
    else:
        p.alert('erro na linha 55')

    p.write('TED RECEBIDA CORRETORA DE SEGUROS')
    p.sleep(1)

    saldos_pendentes = p.locateCenterOnScreen('C:/RPA/arquivos/images/saldos_pendentes.png', confidence=0.95)
    if saldos_pendentes != None:
        c(saldos_pendentes.x, saldos_pendentes.y)
    else:
        logging.info('  Erro ao processar variavel saldo_pendentes')
        
    p.sleep(2)
    result_lançamentos2 = p.locateCenterOnScreen('C:/RPA/arquivos/images/tabela_branco.png', confidence=0.95)
    while result_lançamentos2 != None:
        p.sleep(2)
        print(" aguarde")
        result_lançamentos2 = p.locateCenterOnScreen('C:/RPA/arquivos/images/tabela_branco.png', confidence=0.95)
    p.sleep(1)

    valor_entre = p.locateCenterOnScreen('C:/RPA/arquivos/images/valor_entre.png', confidence=0.95)
    if valor_entre != None:
        c(valor_entre.x+40, valor_entre.y)
    else:
        logging.info('  Erro ao processa variavel valor_entre')


    valor_f = glob_calculo_valor(valor)

    p.write(valor_f)
    p.press('Tab')
    p.write(valor_f)

    p.sleep(2)
    
    p.press("Tab")
    
   
    # p.press('Tab')
    
    p.sleep(2)
    result_lançamentos = p.locateCenterOnScreen('C:/RPA/arquivos/images/reseultado_lancamentos.png', confidence=0.95)
    if result_lançamentos == None:
        print("PROCESSO FINALIZADO \n Valor Encontrado")
        logging.info("PROCESSO FINALIZADO \n Valor Encontrado")
        return True
        
    else:
        print("PROCESSO FINALIZADO \n Valor não  Encontrado")
        logging.info("PROCESSO FINALIZADO \n Valor não Encontrado")
        return False

    

# p.sleep(2)
# pesquisar_valor_comissa_spf('41160','23/04/2024 17:37:57','4900.0')


# pesquisar_valor('41160','08/01/2024 16:21:11','3500.0')