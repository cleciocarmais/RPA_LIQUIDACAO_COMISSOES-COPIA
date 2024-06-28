from src.Model.Comissa_spf.Encontra_valor_spf import pesquisar_valor_comissa_spf
from src.Model.Comissa_spf.pesquisa_titulo_spf import pesquisar_titulo_comissao_spf
from src.Model.Comissa_spf.inclusaoTitulo_SPF import incluir_titulo_spf
from src.Model.Comissa_spf.anulacao_Titulo_spf import anulacao_titulo_spf
from src.Model.Comissa_spf.liquidacaoSPF import Liquidação_comissa_spf
from src.Model.global_loginDealer import login_dealer_contas_receber
from src.Model.global_loginDealer import login_dealer_controle_bancario
from src.Model.global_utilitarios import glob_contas_gerenciais
from src.Model.global_muda_empresa2 import muda_empresa
from src.Model.global_muda_empresa2 import muda_empresa_contas_a_receber
from src.Model.Comissa_spf.nomes_clientesSPF import salvando_nomes_clientes
from src.Model.global_Consulta_cadastro import glob_consultar_situacao_cliente
from src.Model.global_clickApi import click2 as c
from src.Model.Comissa_spf.emali_comissa_spf import email_comissa_spf
import logging
import pandas as pd
import pyautogui as p
import os


def run_comissao_Spf(df,i,lista_qtde_clientes,lista_empresa_fandi):
    """
    passa algumentos respectivamente\n
    df = dataframe da planilha que esta lendo   \n 
    LISTA QTDE CLIENTE = QUANTIDADE DE CLIENTE \n
    i =  index de cade linha da planilha\n
    lista de empresa fandi
    
    função retorna true quando for email for enviado 
    """
    flag = False

    resultadosClientes  = []

    print('\nINCIANDO PROCESSO DE COMISSAO SPF')
    logging.info('\nINCIANDO PROCESSO DE COMISSAO SPF')
    
    login_dealer_controle_bancario()
    p.sleep(1)
    muda_empresa(df['Empresa'][i])
    p.sleep(0.5)
    valor_encontrado_spf = pesquisar_valor_comissa_spf(glob_contas_gerenciais[df['Empresa'][i]], df['Carimbo de data/hora'][i],df['Valor Total da Nota Fiscal'][i])
 
    if valor_encontrado_spf:
        p.sleep(1)
        os.system('TASKKILL /PID scb.exe')

        LISTA_CLIENTES_SPF = salvando_nomes_clientes(df,i,lista_qtde_clientes,lista_empresa_fandi)
 
        p.sleep(2)
        login_dealer_contas_receber()
        p.sleep(2)
        muda_empresa_contas_a_receber(df['Empresa'][i])
    
        clientes_cadastros_spf,clientes_n_cadastrados_spf = glob_consultar_situacao_cliente(LISTA_CLIENTES_SPF)
        print(clientes_cadastros_spf)
    
    
        for cliente_n_cadastro_spf in clientes_n_cadastrados_spf:
            resultadosClientes.append(cliente_n_cadastro_spf)
        VALOR_NONTANTE = 0

        for id, cliente_spf in enumerate(clientes_cadastros_spf):
            if id == 0:
                        flag = True
                        VALOR_NONTANTE = 0

            if cliente_spf['Emp fandi'] == df['Empresa'][i]:

                print(f"PESQUISANDO PELO TITULO de {cliente_spf['nome']} COMISSÃO SPF")
                logging.info(f"PESQUISANDO PELO TITULO de {cliente_spf['nome']} COMISSÃO SPF")
                resultado_pesquisa_spf = pesquisar_titulo_comissao_spf (cliente_spf)

                if resultado_pesquisa_spf:
                    #  p.alert('EMPRSA IGUAIS E TITULO ENCONTRADO')
                    
                    resultado_da_liquidaca_spf, valorSobras, valor_cliete = Liquidação_comissa_spf(cliente_spf,flag)
                 
                    if resultado_da_liquidaca_spf == True:
                        VALOR_NONTANTE = VALOR_NONTANTE + valorSobras
                        print("LIQUIDAÇÃO FEITA COMISSÃO SPF ")
                        resultadosClientes.append(
                            {
                                'nome': cliente_spf['nome'],
                                'valor': valor_cliete,
                                'Emp fandi': cliente_spf['Emp fandi'],
                                'Valor total nf': cliente_spf['Valor total nf'],
                                'Empresa': cliente_spf['Empresa'],
                                'datas': cliente_spf['datas'],
                                'Status' : 'Liquidacão feita'})
                
                    fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                    if fechar != None:
                        c(fechar.x, fechar.y)
                    
                else:
                    #TODO MANDA EMAIL A ALGUEM 
                    print(' CLIENTE SEM TITULO COMISSÃO SPF ')
                    VALOR_NONTANTE = VALOR_NONTANTE + float(cliente_spf['valor'])

                    resultadosClientes.append( {
                                'nome': cliente_spf['nome'],
                                'valor': cliente_spf['valor'],
                                'Emp fandi': cliente_spf['Emp fandi'],
                                'Valor total nf': cliente_spf['Valor total nf'],
                                'Empresa': cliente_spf['Empresa'],
                                'datas': cliente_spf['datas'],
                                'Status' : 'Titulo não Encontrado'})
                    logging.info('TITULO NÃO ENCONTRADO')
                    print('TITULO NÃO ENCONTRADO')
                            
                    fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                    if fechar != None:
                        c(fechar.x, fechar.y)
        

            else:
                    
                print('EMPRESA DIVERGENTE COMISSAO SPF  ')
                logging.info('EMPRESA DIVERGENTE COMISSAO SPF ')

                print(f" PESQUISANDO PELO TITULO  COMISSAO SPF DIVERGENTE : {cliente_spf['nome']}")
                logging.info(f"PESQUISANDO PELO TITULO COMISSAO SPF DIVERGENTE : {cliente_spf['nome']}")
                resultado_pesquisa_spf = pesquisar_titulo_comissao_spf (cliente_spf)
                # esultado_pesquisa_spf = True
                if resultado_pesquisa_spf:
                    print('TITULO ENCONTRADO COMISSAO SPF DIVERGENTE' )
                    logging.info('TITULO ENCONTRADO COMISSAO SPF DIVERGENTE' )
                    
                  
                    # realizaLiquidacao(cliente_spf)
                    p.sleep(1)
                    lancamento_antigo_spf, lancamento_novo_spf = incluir_titulo_spf(cliente_spf['id_cliente'])
                    p.sleep(0.5)
                    print('INICIALIZANDO ANULACAO DE TITULO COMISSAO SPF')
                    logging.info('INICIALIZANDO ANULACAO DE TITULO COMISSAO SPF')
                    anulacao_titulo_spf(lancamento_antigo_spf, lancamento_novo_spf)
                    
                    resultado_da_liquidaca_spf, valorSobras, valor_cliete = Liquidação_comissa_spf(cliente_spf,flag)
# 2638886
                    if resultado_da_liquidaca_spf == True:
                        print("SALVANDO LIQ COMISSAO SPF")
                        logging.info('SALVANDO LIQ COMISSAO SPF')
                        VALOR_NONTANTE = VALOR_NONTANTE + valorSobras

                        resultadosClientes.append(
                            {
                                'nome': cliente_spf['nome'],
                                'valor': valor_cliete,
                                'Emp fandi': cliente_spf['Emp fandi'],
                                'Valor total nf': cliente_spf['Valor total nf'],
                                'Empresa': cliente_spf['Empresa'],
                                'datas': cliente_spf['datas'],
                                'Status' : 'Liquidacão feita'})
                       

                        fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                        if fechar != None:
                            c(fechar.x, fechar.y)
                            

                else:
                    print(' SALVANDO CLIENTE SEM TITULO DE EMPRESA DIVERGENTE COMISSAO SPF')
                    VALOR_NONTANTE = VALOR_NONTANTE + float(cliente_spf['valor'])

                    resultadosClientes.append({
                        'nome': cliente_spf['nome'],
                            'valor': cliente_spf['valor'],
                            'Emp fandi': cliente_spf['Emp fandi'],
                            'Valor total nf': cliente_spf['Valor total nf'],
                            'Empresa': cliente_spf['Empresa'],
                            'datas': cliente_spf['datas'],
                            'Status' : 'Titulo não Encontrado'
                    })
                    fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                    if fechar != None:
                        c(fechar.x, fechar.y)
            flag = False
            

        if len(resultadosClientes) > 0:
            email_comissa_spf(resultadosClientes, VALOR_NONTANTE)
        return True