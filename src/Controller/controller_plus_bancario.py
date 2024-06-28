import pandas as pd
import logging
from src.Model.plus_bancario.listando_nomes_cliente_plus_bancario import listando_clientes_plus_bancario
from src.Model.plus_bancario.liquidacao_plus_bancario import realizaLiquidacao_plus_bancario
from src.Model.plus_bancario.anulacao_Titulo_plus_bancario import anulacao_titulo_plus_bancario
from src.Model.plus_bancario.emali_plus_bancario import email_plus_bancario
from src.Model.plus_bancario.inclusaoTitulo_plus_banacario import incluir_titulo_plus_bancario
from src.Model.global_loginDealer import login_dealer_controle_bancario,login_dealer_contas_receber
from src.Model.global_muda_empresa2 import muda_empresa,muda_empresa_contas_a_receber
from src.Model.global_buscar_valor import glob_pesquisa_valor_dealer
from src.Model.global_Consulta_cadastro import glob_consultar_situacao_cliente
from src.Model.global_pesquisa_titulo import glob_pesquisar_titulo_client
from src.Model.global_utilitarios import glob_contas_gerenciais
from src.Model.global_clickApi import click2 as c
import pandas as pd
import pyautogui as p
import os
import traceback


     

def run_plus_bancario(df,index,lista_qtde_clientes,lista_empresa_fandi):
    try:
        resultadosClientes = []
        primeiro_cliente = False
        print("TIPO DE BONIFICAÇÃO : [Semanal] Plus Bancário - Retorno **")
        logging.info("TIPO DE BONIFICAÇÃO : [Semanal] Plus Bancário - Retorno**")
        p.sleep(1)
        login_dealer_controle_bancario()
        print(f'INICIANDO {df["Empresa"][index]}')
        muda_empresa(df['Empresa'][index])
        p.sleep(1)
        # valor_encontrado_plus_bancario = True
        valor_encontrado_plus_bancario = glob_pesquisa_valor_dealer(glob_contas_gerenciais[df['Empresa'][index]],df['Carimbo de data/hora'][index],df['Valor Total da Nota Fiscal'][index])
        if valor_encontrado_plus_bancario:
            print("VALOR ENCONTRADO!!")
            logging.info("VALOR ENCONTRADO!!")
        
            os.system('TASKKILL /PID scb.exe')
            p.sleep(1)

            lista_clientes_plus_bancario = listando_clientes_plus_bancario(df,index,lista_qtde_clientes,lista_empresa_fandi)
           

            login_dealer_contas_receber()

            p.sleep(2)
                    
            clietes_cadastrados_plus_bancario,clientes_n_cadastrados_plus_bancario = glob_consultar_situacao_cliente(lista_clientes_plus_bancario)
        
            for cliente_n_cadastrado_plus_bancario in clientes_n_cadastrados_plus_bancario:
                resultadosClientes.append(cliente_n_cadastrado_plus_bancario)

            muda_empresa_contas_a_receber(df['Empresa'][index])

            print(3)

            for id_cliente,cliente in enumerate(clietes_cadastrados_plus_bancario):
                print(4)
                if id_cliente == 0:
                            primeiro_cliente = True

                if cliente['Emp fandi'] == df['Empresa'][index]:
                    print("EMPRESA SEMELHANTES PLUS BANCARIO ")
                    logging.info("EMPRESA SEMELHANTES PLUS BANCARIO ")

                    print(f"PESQUISANDO PELO TITULO de {cliente['nome']}")
                    logging.info(f"PESQUISANDO PELO TITULO de {cliente['nome']}")
                    titulo_encontrado_plus_bancario = glob_pesquisar_titulo_client(cliente)
                   
                    if titulo_encontrado_plus_bancario:
                

                       
                        resultado_liquidaca_plus_bancario = realizaLiquidacao_plus_bancario(cliente,primeiro_cliente)
                
                        if resultado_liquidaca_plus_bancario == True:
                            print(" LIQUIDAÇÃO REALIZADA COM SUCESSO!!")
                            logging.info(" LIQUIDAÇÃO REALIZADA COM SUCESSO!!")
                            resultadosClientes.append(
                                {
                                    'nome': cliente['nome'],
                                    'valor': cliente['valor'],
                                    'Emp fandi': cliente['Emp fandi'],
                                    'Valor total nf': cliente['Valor total nf'],
                                    'Empresa': cliente['Empresa'],
                                    'datas': cliente['datas'],
                                    'Status' : 'Liquidacão feita'})
                        if resultado_liquidaca_plus_bancario =='divergente':
                                print("LIQUIDAÇÃA N REALIZADO POR VALOR DIVERGENTE")
                                logging.info("LIQUIDAÇÃA N REALIZADO POR VALOR DIVERGENTE")

                                resultadosClientes.append(
                                {
                                    'nome': cliente['nome'],
                                    'valor': cliente['valor'],
                                    'Emp fandi': cliente['Emp fandi'],
                                    'Valor total nf': cliente['Valor total nf'],
                                    'Empresa': cliente['Empresa'],
                                    'datas': cliente['datas'],
                                    'Status' : 'Valor Divergente no Dealer'})
                                
                    
                        p.sleep(1)
                        fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                        if fechar != None:
                            c(fechar.x, fechar.y)
                    else:
                                #TODO MANDA EMAIL A ALGUEM 
                                print('LIQUIDACÃO NÃO REALIZADA POR CLIENTE SEM TITULO ')
                                logging.info('LIQUIDACÃO NÃO REALIZADA POR CLIENTE SEM TITULO ')

                                resultadosClientes.append( {
                                            'nome': cliente['nome'],
                                            'valor': cliente['valor'],
                                            'Emp fandi': cliente['Emp fandi'],
                                            'Valor total nf': cliente['Valor total nf'],
                                            'Empresa': cliente['Empresa'],
                                            'datas': cliente['datas'],
                                            'Status' : 'Titulo não Encontrado'})
                                logging.info('TITULO NÃO ENCONTRADO')
                                print('TITULO NÃO ENCONTRADO')
                                
                                fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                                if fechar != None:
                                    c(fechar.x, fechar.y)
                else:
                            
                            print('EMPRESA DIVERGENTE   ')
                            logging.info('EMPRESA DIVERGENTE   ')
                            print(f" PESQUISANDO PELO TITULO EMPRESA DIVERGENTE {cliente['nome']}")
                            logging.info(F"  PESQUISANDO PELO TITULO EMPRESE DIVERGENTE {cliente['nome']}")
                            titulo_encontrado_plus_bancario_empresa_divergente = glob_pesquisar_titulo_client(cliente)
                            # titulo_encontrado_plus_bancario_empresa_divergente = True
                            if titulo_encontrado_plus_bancario_empresa_divergente:
                                print('EMPRESA DIVERGENTES, MAS TITULO ENCONTRADO')
                                logging.info('EMPRESA DIVERGENTES, MAS TITULO ENCONTRADO')
                                #TODO CHAMAR DUAS FUNCOES UMA PARA CRIAR UM NOVO TITULO E OUTRA PARA ANULAR O ANTIGO TITULO.
                                # realizaLiquidacao(cliente)
                                p.sleep(1)
                                lancamento_antigo, lancamento_novo,resultado_valores= incluir_titulo_plus_bancario(cliente['id_cliente'],cliente['valor'])
                                p.sleep(0.5)
                                if resultado_valores == 'divergente':
                                        
                                        resultadosClientes.append(
                                        {
                                            'nome': cliente['nome'],
                                            'valor': cliente['valor'],
                                            'Emp fandi': cliente['Emp fandi'],
                                            'Valor total nf': cliente['Valor total nf'],
                                            'Empresa': cliente['Empresa'],
                                            'datas': cliente['datas'],
                                            'Status' : 'Valor Divergente no Dealer'})
                                        fechar = p.locateCenterOnScreen(f'C:/RPA/arquivos/images/fechar38.png',confidence=0.95)
                                        while fechar != None:
                                            print("aguarde")
                                            p.sleep(1)
                                            c(fechar.x, fechar.y)
                                            fechar = p.locateCenterOnScreen(f'C:/RPA/arquivos/images/fechar38.png',confidence=0.95)

                                        p.sleep(1)
                                       
                                        continue

                                
                                anulacao_titulo_plus_bancario(lancamento_antigo, lancamento_novo)
                                p.sleep(1)
                                
                              
                                resultado_liquidaca_plus_bancario_divergente = realizaLiquidacao_plus_bancario(cliente,primeiro_cliente)

                                if resultado_liquidaca_plus_bancario_divergente == True:
                                    print("LIQUIDAÇÃO REALIZADA COM SUCESSO DE EMPRESA DIVERGENTE")
                                    logging.info("LIQUIDAÇÃO REALIZADA COM SUCESSO DE EMPRESA DIVERGENTE")

                                    resultadosClientes.append(
                                        {
                                            'nome': cliente['nome'],
                                            'valor': cliente['valor'],
                                            'Emp fandi': cliente['Emp fandi'],
                                            'Valor total nf': cliente['Valor total nf'],
                                            'Empresa': cliente['Empresa'],
                                            'datas': cliente['datas'],
                                            'Status' : 'Liquidacão feita'})
                                    fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                                    if fechar != None:
                                        c(fechar.x, fechar.y)
                                if resultado_liquidaca_plus_bancario_divergente =='divergente':
                                        
                                        print("LIQUIDAÇÃO NÃO REALIZA POR VALOR DIVERGEENTE")
                                        logging.info("LIQUIDAÇÃO NÃO REALIZA POR VALOR DIVERGEENTE")

                                        resultadosClientes.append(
                                        {
                                            'nome': cliente['nome'],
                                            'valor': cliente['valor'],
                                            'Emp fandi': cliente['Emp fandi'],
                                            'Valor total nf': cliente['Valor total nf'],
                                            'Empresa': cliente['Empresa'],
                                            'datas': cliente['datas'],
                                            'Status' : 'Valor Divergente no Dealer'})
                                        

                            else:
                                print('CLIENTE SEM TITULO ENCONCONTRA DE EMPRESA DIVERGENTE ')
                                resultadosClientes.append({
                                    'nome': cliente['nome'],
                                        'valor': cliente['valor'],
                                        'Emp fandi': cliente['Emp fandi'],
                                        'Valor total nf': cliente['Valor total nf'],
                                        'Empresa': cliente['Empresa'],
                                        'datas': cliente['datas'],
                                        'Status' : 'Titulo não Encontrado'
                                })
                                fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                                if fechar != None:
                                    c(fechar.x, fechar.y)
                                # email_titulo_n_empresa_divergente(cliente)

                                #TODO MANDA EMAIL A ALGUEM 
                               
                primeiro_cliente = False

                
                # df.loc[i, 'Liquidação'] = 'Feito'
                # df = df.astype(str)
                # gd.set_with_dataframe(work, df)
               

                p.sleep(2)
                fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                if fechar != None:
                    c(fechar.x, fechar.y)          
            os.system('TASKKILL /PID scr.exe')
            os.system('TASKKILL /PID scb.exe')
            os.system('TASKKILL /PID scb.exe')
    
            if len(resultadosClientes) > 0:
                    email_plus_bancario(resultadosClientes)
                    resultadosClientes = []
                    return True
                    # df.loc[i, 'Liquidação'] = 'Feito'
                    # df = df.astype(str)
                    # gd.set_with_dataframe(work, df)
            print('Bot em casa de 4s')
            p.sleep(4)
            print(resultadosClientes)
            print("\n\n")
                    
                        
        else:
            print("VALOR  NÃO ENCONTRADO!!")
            logging.info("VALOR NÃO ENCONTRADO!!")
            os.system('TASKKILL /PID scb.exe')
            os.system('TASKKILL /PID scb.exe')
    except:
                mgs_Erro = traceback.format_exc()
                print(mgs_Erro)
                logging.info(f'{mgs_Erro}')