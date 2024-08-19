import pyautogui as p
import logging 
import os
import traceback
from src.Model.global_loginDealer import login_dealer_controle_bancario, login_dealer_contas_receber
import gspread
import gspread_dataframe as gd
import pandas as pd
from src.Model.global_utilitarios import *
from src.Model.global_muda_empresa2 import muda_empresa,muda_empresa_contas_a_receber
from src.Model.global_buscar_valor import glob_pesquisa_valor_dealer
from src.Model.global_Consulta_cadastro import glob_consultar_situacao_cliente
from src.Model.global_pesquisa_titulo import glob_pesquisar_titulo_client
import pyautogui as p
from src.Model.global_clickApi import click2 as c
from src.Model.plus_bancario.inclusaoTitulo_plus_banacario import incluir_titulo_plus_bancario
from src.Model.plus_bancario.anulacao_Titulo_plus_bancario import anulacao_titulo_plus_bancario
from src.Model.plus_bancario.listando_nomes_cliente_plus_bancario import listando_clientes_plus_bancario
from src.Model.plus_bancario.emali_plus_bancario import *
from src.Model.plus_bancario.liquidacao_plus_bancario import realizaLiquidacao_plus_bancario
from src.Model.plus_posterior.incluindo_titulo_plus_posterior import incluir_titulo_plus_posterio
from src.Model.plus_posterior.liquidacao_plus_posterior import liquidacao_plus_posterior
from src.Model.plus_posterior.email_plus_posterior import envia_email_plus_posterior
from src.Model.Comissa_spf.Encontra_valor_spf import pesquisar_valor_comissa_spf
from src.Model.Comissa_spf.pesquisa_titulo_spf import pesquisar_titulo_comissao_spf
from src.Model.Comissa_spf.liquidacaoSPF import Liquidação_comissa_spf
from src.Model.Comissa_spf.inclusaoTitulo_SPF import incluir_titulo_spf
from src.Model.Comissa_spf.emali_comissa_spf import email_comissa_spf
from src.Model.Comissa_spf.anulacao_Titulo_spf import anulacao_titulo_spf
from src.Model.Comissa_spf.emali_comissa_spf import email_comissa_spf
from src.Model.plus_bancario.emali_plus_bancario import email_plus_bancario
with open('C:/RPA/Credenciais/pid_bot_running.txt', 'r') as file:
    pid_bot_anterior = file.readlines()[0] # Lendo o conteudo do arquivo - Numero do processo do bot anterior
    os.system('taskkill /PID  ' + pid_bot_anterior +  '   /F') # Forcando o encerramento do bot anterior

# Gravando o n�mero do processo do bot atual no arquivo pid_bot_running.txt
with open('C:/RPA/Credenciais/pid_bot_running.txt', 'w') as file:
    file.write(str(os.getpid())) # sobrescrevendo o numero do PID

    
with open(r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_COMISSOES\log_RPA_LIQUIDACAO_COMISSOES.txt', 'w') as f:
        pass

logging.basicConfig(filename=r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_COMISSOES\log_RPA_LIQUIDACAO_COMISSOES.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p')
CHAVE_ACESSO = 'C:/RPA/Credenciais/service_account.json'
print('Baixando dados da planilha')
logging.info('Baixando dados da planilha')
gs = gspread.service_account(CHAVE_ACESSO)
sh = gs.open('Nota Fiscal - Comissão Financiamento (respostas)')
work = sh.worksheet('Respostas ao formulário 2')
df = pd.DataFrame(work.get_all_records())
print('Dados baixados')
logging.info('Dados baixados')


lista_qtde_clientes = [str(x) for x in df['Quantidade de Clientes']]
lista_empresa_fandi = [str(x) for x in df['Empresa Fandi']]
resultadosClientes = []
RESULT_SOBRAS = 0

flag = 0

try:
    
    print('***INICIALIZANDO PROCESSO***')
    logging.info('***INCIALIZANDO PROCESSO***')
    
    for i in range(len(df.index)):
        if df['Liquidação'][i] == '':
            if df['Tipo de Bonificação'][i] == '[Semanal] Plus Bancário - Retorno':
            
                print("**  TIPO DE BONIFICAÇÃO : [Semanal] Plus Bancário - Retorno  **")
                logging.info("**  TIPO DE BONIFICAÇÃO : [Semanal] Plus Bancário - Retorno  **")
                p.sleep(1)
                login_dealer_controle_bancario()
                print(f'INICIANDO {df["Empresa"][i]}')
                muda_empresa(df['Empresa'][i])
                p.sleep(1)
                valor_encontrado = glob_pesquisa_valor_dealer(glob_contas_gerenciais[df['Empresa'][i]],df['Carimbo de data/hora'][i],df['Valor Total da Nota Fiscal'][i])
                if valor_encontrado:
                    os.system('TASKKILL /PID scb.exe')
                    p.sleep(1)
                    login_dealer_contas_receber()
                    
                    lista_clientes_plus_bancario = listando_clientes_plus_bancario(df,lista_qtde_clientes,i,lista_empresa_fandi)
                    print(lista_clientes_plus_bancario)
                    
                    p.sleep(2)
                    
                    clietes_cadastrados_plus_bancario,clientes_n_cadastrados_plus_bancario = glob_consultar_situacao_cliente(lista_clientes_plus_bancario)
                
                    for cliente_n_cadastrado_plus_bancario in clientes_n_cadastrados_plus_bancario:
                        resultadosClientes.append(cliente_n_cadastrado_plus_bancario)

                    print(2)

                    muda_empresa_contas_a_receber(df['Empresa'][i])
                    print(3)
                    for index,cliente in enumerate(clietes_cadastrados_plus_bancario):
                            print(4)
                            if cliente['Emp fandi'] == df['Empresa'][i]:

                                print(f"**PESQUISANDO PELO TITULO de {cliente['nome']}**")
                                logging.info("PESQUISANDO PELO TITULO")
                                titulo_encontrado_plus_bancario = glob_pesquisar_titulo_client(cliente)
                                
                                if titulo_encontrado_plus_bancario:
                                    #  p.alert('EMPRSA IGUAIS E TITULO ENCONTRADO')

                                    if index == 0:
                                        
                                        flag = 0
                                    resultado_liquidaca_plus_bancario = realizaLiquidacao_plus_bancario(cliente,flag)
                            
                                    if resultado_liquidaca_plus_bancario == True:
                                        print(" LIQUIDAÇÃO FEITA ")
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
                                            print(" CLIENTE COM DIVERGENCIA ENTRE VALORES ")

                                            resultadosClientes.append(
                                            {
                                                'nome': cliente['nome'],
                                                'valor': cliente['valor'],
                                                'Emp fandi': cliente['Emp fandi'],
                                                'Valor total nf': cliente['Valor total nf'],
                                                'Empresa': cliente['Empresa'],
                                                'datas': cliente['datas'],
                                                'Status' : 'Valor Divergente no Dealer'})
                                            
                                
                                    fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                                    if fechar != None:
                                        c(fechar.x, fechar.y)
                                else:
                                    #TODO MANDA EMAIL A ALGUEM 
                                    print('**********************CLIENTE SEM TITULO**************************************')

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
                                
                                print(' * EMPRESA DIVERGENTE * ')
                                logging.info(' * EMPRESA DIVERGENTE * ')
                                print(f" PESQUISANDO PELO TITULO de {cliente['nome']}")
                                logging.info("  PESQUISANDO PELO TITULO")
                                titulo_encontrado_plus_bancario_empresa_divergente = glob_pesquisar_titulo_client(cliente)
                                # titulo_encontrado_plus_bancario_empresa_divergente = True
                                if titulo_encontrado_plus_bancario_empresa_divergente:
                                    p.printInfo('EMPRESA DIVERGENTES, MAS TITULO ENCONTRADO')
                                    #TODO CHAMAR DUAS FUNCOES UMA PARA CRIAR UM NOVO TITULO E OUTRA PARA ANULAR O ANTIGO TITULO.
                                    # realizaLiquidacao(cliente)
                                    p.sleep(1)
                                    lancamento_antigo, lancamento_novo= incluir_titulo_plus_bancario(cliente['id_cliente'],cliente['valor'])
                                    p.sleep(0.5)
                                    print('INICIALIZANDO ANULACAO DE TITULO')
                                    logging.info('INICIALIZANDO ANULACAO DE TITULO')
                                    anulacao_titulo_plus_bancario(lancamento_antigo, lancamento_novo)
                                    resultado_liquidaca_plus_bancario_divergente = realizaLiquidacao_plus_bancario(cliente)
                                    if resultado_liquidaca_plus_bancario_divergente == True:
                                        print(" SALVANDO CLIENTE NA LISTA DE LIQUIDAÇAO EMPRESA DIVERGENTE ")

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
                                            print(" CLIENTE COM DIVERGENCIA ENTRE VALORES ")

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
                                    print('********************** SALVANDO CLIENTE SEM TITULO DE EMPRESA DIVERGENTE **************************************')
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
                                    print('Empresa divergente com Empresa da Fandi')

                    os.system('TASKKILL /PID scr.exe')
                    df.loc[i, 'Liquidação'] = 'Feito'
                    df = df.astype(str)
                    gd.set_with_dataframe(work, df)
                    print('Bot em casa de 4s')
                    p.sleep(4)
                    print(resultadosClientes)
                    if len(resultadosClientes) > 0:
                            email_plus_bancario(resultadosClientes)
                    df.loc[i, 'Liquidação'] = 'Feito'
                    df = df.astype(str)
                    gd.set_with_dataframe(work, df)
                    
                    p.sleep(4)
                else:
                    os.system('TASKKILL /PID scb.exe')
                    os.system('TASKKILL /PID scb.exe')
                  

             
            ####################################################### PLUS POSTERIOR ##############################################################



            elif df['Tipo de Bonificação'][i] == 'Plus Posterior (Bônus de Comissão)':
                print("INICIANDO PROCESSO DE PLUS POSTERIOR")
                logging.info("INICIANDO PROCESSO DE PLUS POSTERIOR")
                login_dealer_controle_bancario()
                print(f'INICIANDO {df["Empresa"][i]}')
                muda_empresa(df['Empresa'][i])
                p.sleep(1)
                valor_encontrado_plus_posterior = glob_pesquisa_valor_dealer(glob_contas_gerenciais[df['Empresa'][i]],df['Carimbo de data/hora'][i],df['Valor Total da Nota Fiscal'][i])
                p.sleep(1)

                if valor_encontrado_plus_posterior:
                    os.system('TASKKILL /PID scb.exe')

                    #TODO EM FAZER DE TESTE AINDA ESPERANDO ALGUMAS INFORMAÇOES COMO TIPOP DE NS
                    login_dealer_contas_receber()
                    p.sleep(1)
                    muda_empresa_contas_a_receber(df['Empresa'][i])
                    p.sleep(0.5)
                    numero_lancamento_plus_posterior = incluir_titulo_plus_posterio(df['Valor Total da Nota Fiscal'][i],str(df['Nº da NS'][i]))
                    informacoes_para_liquidacao_plus_posterior = {

                            'Valor total nf': df['Valor Total da Nota Fiscal'][i],
                            'Empresa': df['Empresa'][i],
                            'datas': df['Carimbo de data/hora'][i],
                        
                    }
                    
                    liquidacao_plus_posterior(informacoes_para_liquidacao_plus_posterior,numero_lancamento_plus_posterior)
                    informaçao = {
                            'EMPRESA' : df['Empresa'][i],
                            'NUMERO_TITULO' : df['Nº da NS'][i],
                            'Valor Total da Nota Fiscal' : df['Valor Total da Nota Fiscal'][i],
                            'Status' : 'Liquidacão feita'
                        }
                    p.sleep(1)
                    envia_email_plus_posterior(informaçao)
                else:
                    os.system('TASKKILL /PID scb.exe')


            ####################################################### COMISSÃO SPF ##############################################################


            elif df['Tipo de Bonificação'][i] == 'Comissão SPF':
                print('INCIANDO PROCESSO DE COMISSAO SPF')
                logging.info('INCIANDO PROCESSO DE COMISSAO SPF')
                
                login_dealer_controle_bancario()
                p.sleep(1)
                muda_empresa(df['Empresa'][i])
                p.sleep(0.5)
                valor_encontrado = pesquisar_valor_comissa_spf(glob_contas_gerenciais[df['Empresa'][i]], df['Carimbo de data/hora'][i],df['Valor Total da Nota Fiscal'][i])
                valor_encontrado = True
                if valor_encontrado:
                    os.system('TASKKILL /PID scb.exe')

                    LISTA_CLIENTES_SPF = listando_clientes_plus_bancario(df,lista_qtde_clientes,i,lista_empresa_fandi)
                    p.sleep(2)
                    login_dealer_contas_receber()
                    p.sleep(2)
                    muda_empresa_contas_a_receber(df['Empresa'][i])
                
                    clientes_cadastros_spf,clientes_n_cadastrados_spf = glob_consultar_situacao_cliente(LISTA_CLIENTES_SPF)
                    print(clientes_cadastros_spf)
               
                
                    for cliente_n_cadastro_spf in clientes_n_cadastrados_spf:
                        resultadosClientes.append(cliente_n_cadastro_spf)

                    for id, cliente_spf in enumerate(clientes_cadastros_spf):

                        if cliente_spf['Emp fandi'] == df['Empresa'][i]:
                            print(f"PESQUISANDO PELO TITULO de {cliente_spf['nome']} COMISSÃO SPF")
                            logging.info("PESQUISANDO PELO TITULO DA COMISSÃO  SPF")
                            resultado_pesquisa_spf = pesquisar_titulo_comissao_spf (cliente_spf)
                            if resultado_pesquisa_spf:
                                #  p.alert('EMPRSA IGUAIS E TITULO ENCONTRADO')
                                print("TITULO ENCONTRADO SPF COMISSAO")
                                logging.info("Titulo Encontrado Comissão SPF")
                                resultado_da_liquidaca_spf, valorSobras, valor_cliete = Liquidação_comissa_spf(cliente_spf)
                        
                                if resultado_da_liquidaca_spf == True:
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
                            print(f" PESQUISANDO PELO TITULO de {cliente_spf['nome']}")
                            logging.info("PESQUISANDO PELO TITULO COMISSAO SPF")
                            resultado_pesquisa_spf = pesquisar_titulo_comissao_spf (cliente_spf)
                            # esultado_pesquisa_spf = True
                            if resultado_pesquisa_spf:
                                p.printInfo('TITULO ENCONTRADO COMISSAO SPF' )
                                #TODO CHAMAR DUAS FUNCOES UMA PARA CRIAR UM NOVO TITULO E OUTRA PARA ANULAR O ANTIGO TITULO.
                                # realizaLiquidacao(cliente_spf)
                                p.sleep(1)
                                lancamento_antigo_spf, lancamento_novo_spf = incluir_titulo_spf(cliente_spf['id_cliente'])
                                p.sleep(0.5)
                                print('INICIALIZANDO ANULACAO DE TITULO COMISSAO SPF')
                                logging.info('INICIALIZANDO ANULACAO DE TITULO COMISSAO SPF')
                                anulacao_titulo_spf(lancamento_antigo_spf, lancamento_novo_spf)
                                resultado_da_liquidaca_spf, valorSobras, valor_cliete = Liquidação_comissa_spf(cliente_spf)

                                if resultado_da_liquidaca_spf == True:
                                    print("SALVANDO LIQ COMISSAO SPF")
                                    logging.info('SALVANDO LIQ COMISSAO SPF')

                                    resultadosClientes.append(
                                        {
                                            'nome': cliente_spf['nome'],
                                            'valor': valor_cliete,
                                            'Emp fandi': cliente_spf['Emp fandi'],
                                            'Valor total nf': cliente_spf['Valor total nf'],
                                            'Empresa': cliente_spf['Empresa'],
                                            'datas': cliente_spf['datas'],
                                            'Status' : 'Liquidacão feita'})
                                    RESULT_SOBRAS += float(valorSobras)

                                    fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
                                    if fechar != None:
                                        c(fechar.x, fechar.y)
                                        

                            else:
                                print(' SALVANDO CLIENTE SEM TITULO DE EMPRESA DIVERGENTE COMISSAO SPF')
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

                                    # email_titulo_n_empresa_divergente(cliente_spf)
                    
                    email_comissa_spf(resultadosClientes)

                    # RESULT_SOBRAS += float(valorSobras)
                    # if RESULT_SOBRAS != 0:
                    #     print(RESULT_SOBRAS)
                    #     if len(resultadosClientes) > 0:
                    #         p.alert('45 ')
                    #         email_comissa_spf(resultadosClientes)

                        #  incluir_titulo_spf()
                                    
                else:
                    print('Valor n Encontrado')
                    os.system('TASKKILL /PID scb.exe')

                     

                 
                 
            
                     
                    
        else:
                print(f'** EMPRESA JA PROCESSADA {df["Empresa"][i]} **')
                logging.info(f'** EMPRESA JA PROCESSADA {df["Empresa"][i]} **')

                     
            # else:
            #     print('Valor processado')
            #     os.system('TASKKILL /PID scb.exe')

        
    
                 

except:
        mgs = traceback.format_exc()
        logging.info(mgs)
        print(mgs)

finally:
        
        os.system('TASKKILL /PID scb.exe')
        os.system('TASKKILL /PID scr.exe')


