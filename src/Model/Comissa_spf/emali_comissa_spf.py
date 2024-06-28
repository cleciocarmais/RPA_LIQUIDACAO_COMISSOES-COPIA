from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from datetime import datetime
from datetime import datetime
import sys
sys.path.append(r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_COMISSOES')
from src.Model.global_utilitarios import escreva
from src.Model.global_calculo_imposto import glob_calculo_valor
    
chave_de_acesso_Email = open(r'C:\RPA\credenciais\credenciais_gmail.txt', 'r')
chaves = chave_de_acesso_Email.readlines()
chave_de_acesso_Email.close()


sender = chaves[0][:-1]
password = chaves[1]
data_atual = datetime.now().strftime('%d/%m/%Y')


def email_comissa_spf(informacoes, montante):
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.ehlo()
    servidor.login(sender, password)

    
    receiver = ('morgana.sousa@carmais.com.br,contasareceber_veiculos@carmais.com.br,daniel@carmais.com.br,fcoventura@carmais.com.br,alan.estevao@carmais.com.br')
    # receiver = 'francisco.clecio@carmais.com.br'
    body = ""
    print("*ENVIANDO EMAIL DE COMISSAO SPF*")
    logging.info("*ENVIANDO EMAIL DE COMISSAO SPF*")
    mgs = MIMEMultipart('related')
    mgs['From'] = sender
    mgs['To'] = receiver
    mgs['Subject'] = f'RPA - LIQUIDAÇÃO DE COMISSÃO SPF -  {data_atual} '

    mgsAlternativa = MIMEMultipart('alternative')
    mgs.attach(mgsAlternativa) 
    for dado in informacoes:
        if dado['Status'] == 'Titulo não Encontrado' or dado['Status'] == 'Cliente não Encontrado' or dado['Status'] == 'Valor Divergente no Dealer':
            nome =  f"❌ {dado['nome']}"

        else:
            nome =  f" ✅ {dado['nome']}"
        


        body = body + f'''<h3> {nome}</h3>
        <b>Empresa do Financiamento:</b> {dado['Empresa']} <br>
        <b>Empresa Fandi:</b> {dado['Emp fandi']}<br>
        <b>Valor Total da Notal Fiscal:</b> R$ {glob_calculo_valor(dado['Valor total nf'])}<br>
        <b>Valor do Cliente:</b> R$ {dado['valor'].replace(".",",")}<br>
        <b>Status:</b> {escreva(dado['Status'])}

        
'''
    body = body + f'<h2>Valor Restante  R$ : {round(montante,2)}</h2>'
    mgsText = MIMEText(body,  'html')
    mgsText1 = MIMEText(f"VALOR ")
    mgsAlternativa.attach(mgsText)

    text = mgs.as_string()
    servidor.sendmail(sender,receiver.split(','),text)
    print('EMAIL ENVIADO COM SUCESSO!!!!')
    logging.info('EMAIL ENVIANDO COMO SUCESSO!!!')






# dados = [
# {
# 'nome' : 'VALDINEI RAMOS DOS SANTOS',
# 'valor' : '700.0',
# 'Emp fandi' : 'JANGADA VEICULOS',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Liquidacão feita'

# },
# {
# 'nome' : 'YNGRED MAIA MENESES COELHO',
# 'valor' : '700.0',
# 'Emp fandi' : 'NOVALUZ SUL',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Titulo não Encontrado'

# },
# {
# 'nome' : 'RONALDO DO NASCIMENTO FERREIRA',
# 'valor' : '700.0',
# 'Emp fandi' : 'NOVALUZ WS',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Liquidacão feita'

# },
# {
# 'nome' : 'JOAO PAULO CAVALCANTE TEIXEIRA',
# 'valor' : '700.0',
# 'Emp fandi' : 'NOVALUZ WS',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Liquidacão feita'

# },
# {
# 'nome' : 'FABIOLA DE ALMEIDA XAVIER',
# 'valor' : '700.0',
# 'Emp fandi' : 'NOVALUZ WS',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Liquidacão feita'

# },
# {
# 'nome' : 'AURIO LUCIO LEOCADIO DA SILVA',
# 'valor' : '700.0',
# 'Emp fandi' : 'NOVALUZ WS',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Liquidacão feita'

# },
# {
# 'nome' : 'JOSE GUTEMBERG DA COSTA PEREIRA',
# 'valor' : '700.0',
# 'Emp fandi' : 'NOVALUZ WS',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Liquidacão feita'

# },
# {
# 'nome' : 'FRANCISCO HELDER DO VALE MARTINS',
# 'valor' : '700.0',
# 'Emp fandi' : 'NOVALUZ WS',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Liquidacão feita'

# },
# {
# 'nome' : 'MARY ANNE LUCIO PEREIRA RAMOS',
# 'valor' : '700.0',
# 'Emp fandi' : 'NOVALUZ WS',
# 'Valor total nf' : 6300.0,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/05/2024 17:13:45',
# 'Status' : 'Liquidacão feita'

# },

# ]
# email_comissa_spf(dados,2700)

    # clientes_n_Encontrados = []
    # resultadosClientes = []
    # resultadosClientes = []
    # valoresDivergente = []

    # dados = [
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'},
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'},
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'}
    # ]
    # dadoos = [
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'},
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'},
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'}
    # ]
    # dadosas = [
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'},
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'},
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'}
    # ]
    # dadosasa = [
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'},
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'},
    #     {'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52', 'id_cliente': '0108167'}
    # ]

    # for dado4 in dados:
    #     resultadosClientes.append(dado4)    

    # for dado5 in dadoos:
    #     clientes_n_Encontrados.append(dado5) 

    # for dado6 in dadosas:
    #     resultadosClientes.append(dado6)
    
    # for dado7 in dadosasa:
    #     valoresDivergente.append(dado7)

    # for liquidado in clientes_liquidados:
    #     liquidado['Status'] = 'teste1'

        
    # for enco in clientes_n_Encontrados:
    #     enco['Status'] = 'teste2'

    # print(clientes_liquidados)
    # print('*/////////////////////////////////')
    # print(clientes_n_Encontrados)

    # listas_de_valores = zip(resultadosClientes,clientes_n_Encontrados,valoresDivergente,resultadosClientes)
    # print(listas_de_valores)
    # lista_total = [
    #     {'nome': 'TIAGO CARVALHO GOIS', 'valor': '396.0', 'Emp fandi': 'NOVALUZ WS', 'Valor total nf': 8217.72, 'Empresa': 'NOVALUZ WS', 'datas': '21/03/2024 11:30:28', 'id_cliente': '0108167', 'Status' : 'Valor Divergente no Dealer'},
    #     {'nome': 'PATRICIA MESQUITA VILAS BOAS', 'valor': '2465.91', 'Emp fandi': 'NOVALUZ WS', 'Valor total nf': 8217.72, 'Empresa': 'NOVALUZ WS', 'datas': '22/03/2024 09:47:51', 'id_cliente': '0108167', 'Status' : 'Liquidacão feita'},
    #     {'nome': 'IDELMA BEZERRA DINIZ', 'valor': '3032.92', 'Emp fandi': 'NISSAN MATRIZ', 'Valor total nf': 8217.72, 'Empresa': 'NOVALUZ WS', 'datas': '22/03/2024 09:47:51', 'id_cliente': '0108167', 'Status' : 'Titulo não Encontrado'},
    #     {'nome': 'ARITUZA TIMBO FREITAS', 'valor': '2322.89', 'Emp fandi': 'JANGADA VEICULOS', 'Valor total nf': 8217.72, 'Empresa': 'NOVALUZ WS', 'datas': '22/03/2024 09:47:51', 'id_cliente': '0108167', 'Status' : 'Liquidacão feita'},
    # ]

    # for id, infor in enumerate(listas_de_valores):
    #     if id == 0:
    #         print('id zero')
    #         for i in infor:
    #             i['Status'] = 'Liquidacão Feita'
    #             lista_total.append(i)
    #     elif id == 1:
    #         for i in infor:
    #             i['Status'] = 'Cliente não Encontrado'
    #             lista_total.append(i)
        
    #     elif id == 2:
    #         for i in infor:
    #             i['Status'] = 'Valor Divergente no Dealer'
    #             lista_total.append(i)
        
    #     else:
    #         for i in infor:
    #             i['Status'] = 'Titulo não Encontrado'
    #             lista_total.append(i)
    # print(lista_total)
    # # print('ola mundo')

        
 
    # email_geral(lista_total)
                    

    
