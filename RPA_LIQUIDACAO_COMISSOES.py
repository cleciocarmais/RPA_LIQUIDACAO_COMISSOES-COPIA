import logging
import os
import pyautogui as p
import gspread
import pandas as pd
import gspread_dataframe as gd
import os


from src.Controller.controller_plus_bancario import run_plus_bancario
from src.Controller.controller_plus_posterior import run_plus_posterior
from src.Controller.controller_comissa_spf import run_comissao_Spf

with open('C:/RPA/Credenciais/pid_bot_running.txt', 'r') as file:
    pid_bot_anterior = file.readlines()[0] # Lendo o conteudo do arquivo - Numero do processo do bot anterior
    os.system('taskkill /PID  ' + pid_bot_anterior +  '   /F') # Forcando o encerramento do bot anterior

# Gravando o n�mero do processo do bot atual no arquivo pid_bot_running.txt
with open('C:/RPA/Credenciais/pid_bot_running.txt', 'w') as file:
    file.write(str(os.getpid())) # sobrescrevendo o numero do PID

    
with open(r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_COMISSOES - Copia\log_RPA_LIQUIDACAO_COMISSOES.txt', 'w') as f:
        pass

logging.basicConfig(filename=r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_COMISSOES - Copia\log_RPA_LIQUIDACAO_COMISSOES.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s',
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


for linha in range(len(df.index)):
    if df['Liquidação'][linha] == '':
        print(f"PROCESSANDO LINHA N° {linha}")
        logging.info(f"PROCESSANDO LINHA N° {linha}")
        if df['Tipo de Bonificação'][linha] == '[Semanal] Plus Bancário - Retorno':
            result = run_plus_bancario(df,linha,lista_qtde_clientes[linha],lista_empresa_fandi[linha])
            if result:
                    print("ATUALIZANDO PLANILHA")
                    logging.info("ATUALIZANDO PLANILHA")
                    df.loc[linha, 'Liquidação'] = 'Feito'
                    df = df.astype(str)
                    gd.set_with_dataframe(work, df)
        
            
        elif df['Tipo de Bonificação'][linha] == 'Plus Posterior (Bônus de Comissão)':
            resultado_plus_posterior = run_plus_posterior(df,linha)
            if resultado_plus_posterior:
                print("ATUALIZANDO PLANILHA")
                logging.info("ATUALIZANDO PLANILHA")
                df.loc[linha, 'Liquidação'] = 'Feito'
                df = df.astype(str)
                gd.set_with_dataframe(work, df)
           
            print('\n\n')
                 
        elif df['Tipo de Bonificação'][linha] == 'Comissão SPF':
            result_spf =  run_comissao_Spf(df,linha,lista_qtde_clientes[linha],lista_empresa_fandi[linha])
            if result_spf:
                print("ATUALIZANDO PLANILHA")
                logging.info("ATUALIZANDO PLANILHA")
                df.loc[linha, 'Liquidação'] = 'Feito'
                df = df.astype(str)
                gd.set_with_dataframe(work, df)
            
            
        os.system('TASKKILL /PID scb.exe')
        os.system('TASKKILL /PID scr.exe')
        print('\n\n')



