from src.Model.plus_posterior.incluindo_titulo_plus_posterior import incluir_titulo_plus_posterio
from src.Model.plus_posterior.liquidacao_plus_posterior import liquidacao_plus_posterior
from src.Model.plus_posterior.email_plus_posterior import envia_email_plus_posterior
from src.Model.global_buscar_valor import glob_pesquisa_valor_dealer
from src.Model.global_loginDealer import login_dealer_controle_bancario
from src.Model.global_loginDealer import login_dealer_contas_receber
from src.Model.global_muda_empresa2 import muda_empresa
from src.Model.global_muda_empresa2 import muda_empresa_contas_a_receber
from src.Model.global_utilitarios import glob_contas_gerenciais
import logging
import traceback
import pyautogui as p
import os

def run_plus_posterior(df,i):
 
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
        print("VALOR ENCONTRADO COM SUCESSO")
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
        return True
    else:
        print('valor n encontrado')
        os.system('TASKKILL /PID scb.exe')
