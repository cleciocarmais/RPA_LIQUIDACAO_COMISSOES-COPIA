from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import smtplib
from datetime import datetime
from datetime import datetime
import sys
sys.path.append('C:/RPA_O_MAIS_LINDO_DA_EQUIPE/RPA_LIQUIDACAO_COMISSOES')
from src.Model.global_utilitarios import escreva
from src.Model.global_calculo_imposto import glob_calculo_valor
    


def envia_email_plus_posterior(Informacao):
    print("ENVIANDO EMAIL DE PLUS POSTERIOR")
    logging.info("ENVIANDO EMAIL DE PLUS POSTERIOR")
    print("AGUARDE!!!")
    #SCRIPT RESPONSAVEL POR ENVIAR EMAIL DE LIQUIDACAO DE PLUS  POSTERIOR 
    # receiver = 'francisco.clecio@carmais.com.br'
    receiver = ('morgana.sousa@carmais.com.br,contasareceber_veiculos@carmais.com.br,daniel@carmais.com.br,fcoventura@carmais.com.br,alan.estevao@carmais.com.br')



    chave_de_acesso_Email = open(r'C:\RPA\credenciais\credenciais_gmail.txt', 'r')
    chaves = chave_de_acesso_Email.readlines()
    chave_de_acesso_Email.close()
    sender = chaves[0][:-1]
    password = chaves[1]
    data_atual = datetime.now().strftime('%d/%m/%Y')
    servidor = smtplib.SMTP()
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.ehlo()
    servidor.login(sender, password)

    mgs = MIMEMultipart()
    mgs['From'] = sender
    mgs['To'] = receiver
    mgs['Subject'] =  f'RPA - LIQUIDAÇÃO DE COMISSÃO - PLUS POSTERIOR -  {data_atual}' 

    mgsAlternative = MIMEMultipart('alternative')
    mgs.attach(mgsAlternative)
    print(type(Informacao['Valor Total da Nota Fiscal']))
  

    body = f"""
    
        <h3> ✅ {Informacao['EMPRESA']}</h3>  <br>
        <b> Numero do Titulo </b> {Informacao['NUMERO_TITULO']}<br>
        <b> Valor Total da Nota Fiscal R$ : </b> {str(Informacao['Valor Total da Nota Fiscal']).replace(".",',')}<br>
        <b> Valor liquido R$ : </b> {str(glob_calculo_valor(Informacao['Valor Total da Nota Fiscal']).replace(".",','))}<br>
        <b> Status </b> : {escreva(Informacao['Status'])}




"""
    mgsText = MIMEText(body, 'html')
    mgs.attach(mgsText)

    text = mgs.as_string()

    servidor.sendmail(sender, receiver.split(','), text)
    print('EMAIL ENVIANDO COM SUCESSO!!!!')
    logging.info('EMAIL ENVIANDO COM SUCESSO!!!!')

    
# if __name__=='__main__':
#     import sys
#     sys.path.append('C:/RPA_O_MAIS_LINDO_DA_EQUIPE/RPA_LIQUIDACAO_COMISSOES')
    
# informaçao = [{
#     'EMPRESA' : 'NOVALUZ WS',
#     'NUMERO_TITULO' : '179013',
#     'Valor Total da Nota Fiscal' : '19234.79',
#     'Status' : 'Liquidacão feita'
# }
# ]
# for i in informaçao:
#     print(i)
#     envia_email_plus_posterior(i)    