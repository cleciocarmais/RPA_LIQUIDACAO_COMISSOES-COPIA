import pyautogui as p
import logging
from src.Model.global_clickApi import click2 as c
# from clickApi import click2 as c
from unidecode import unidecode as uni
import pyperclip as pyp
from pynput.keyboard import Controller


def glob_consultar_situacao_cliente(lista_clientes):
    """
    RECEBE UM LISTA DE DADOS COM INFORMAÇÕES DO CLIENTE

    ---------------------------------------------------
    CONSULTA ESSA INFORMAÇÃO NO DEALER \n
    
    RETORNA DUAS LISTA UMA DE CLIENTE CADASTRO E OUTRA DE CLIENTE NA CADASTRADO\n
        
    ---------- PARAMENTRO -----------

        LISTA DE CLIENTE CONTENDO OS SEGUINTE CHAVES : \n    
        NOME   

    --------- RETORNO ----------\n
             'nome':            ---,\n
             'valor':           ---,\n
             'Emp fandi':       ---,\n
             'Valor total nf':  ---,\n
             'Empresa':         ---,\n
             'datas':           ---,\n
             'id_cliente':      ---
             }

    """
    keyboard = Controller()

    cliente_n_encontrado = []
    clientes_encontrados = []
    
    print("CONSULTANDO SITUACAO DO CLIENTE NO DEALER**")
    logging.info('CONSULTANDO SITUACAO DO CLIENTE NO DEALER **')
    img = 'C:/RPA/arquivos/images/'
    print("Aguarde!!")
    btn_cliente = p.locateCenterOnScreen(f'{img}cliente_btn.png', confidence=0.95)

    if btn_cliente != None:
        c(btn_cliente.x, btn_cliente.y)
    else:
        logging.info('   Erro ao processa variavel btn_cliente do metedo Consulta_Cliente')
    p.sleep(1)

    ancora_cliente = p.locateCenterOnScreen(f'{img}Cliente_tipo.png', confidence=0.95)

    
    for id,cliente in enumerate(lista_clientes):

        while ancora_cliente == None:
            p.sleep(1)
            ancora_cliente = p.locateCenterOnScreen(f'{img}Cliente_tipo.png', confidence=0.95)
        c(ancora_cliente.x+80, ancora_cliente.y)
        p.sleep(1)
    
        contendo = p.locateCenterOnScreen(f'{img}contendo3.png', confidence=0.95)
        while contendo == None: 
            p.sleep(1)
            contendo = p.locateCenterOnScreen(f'{img}contendo3.png', confidence=0.95)

        c(contendo.x+85, contendo.y)
        p.sleep(1)
        p.write(uni(cliente['nome']))
        p.sleep(1)
        p.press('Enter')
        p.sleep(3)
        sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
        p.sleep(1)
        if sem_dados != None:
            p.press('Enter')
            p.sleep(2)
            c(ancora_cliente.x+80, ancora_cliente.y)
            c(contendo.x+85, contendo.y)
            keyboard.type(cliente['nome'])
            p.press("Enter")
        p.sleep(2)

        sem_dados2 = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
        if sem_dados2 == None:
            p.press('Enter')
            p.sleep(1)
            print(' --> CLIENTE ENCONTRADO  <-- ')
            logging.info(' --> CLIENTE ENCONTRADO <-- ')
            p.sleep(0.5)
            p.hotkey("ctrl", 'c')
            id_cliente = pyp.paste()
            clientes_encontrados.append({
            'nome': cliente['nome'],
             'valor': cliente['valor'],
             'Emp fandi': cliente['Emp fandi'],
             'Valor total nf': cliente['Valor total nf'],
             'Empresa': cliente['Empresa'],
             'datas': cliente['datas'],
             'id_cliente': id_cliente})
        else :
            print(' ( x ) CLIENTE NAO ENCONTRADO ( x )')
            logging.info(' ( x ) CLIENTE NAO ENCONTRADO ( x )')

            cliente_n_encontrado.append({
            'nome': cliente['nome'],
             'valor': cliente['valor'],
             'Emp fandi': cliente['Emp fandi'],
             'Valor total nf': cliente['Valor total nf'],
             'Empresa': cliente['Empresa'],
             'datas': cliente['datas'],
             'Status' : 'Cliente não Encontrado'
             
            })
            p.press('Enter')
            p.sleep(2)




    fechar = p.locateCenterOnScreen(f'{img}fechar12.png', confidence=0.95)
    if fechar != None:
        c(fechar.x, fechar.y)
    else:
        print('VARIAVEL N LOCALIZADA')
        logging.info('VARIAVEL N LOCALIZADA')
    print("CONSULTA FINALIZADA!!")
    logging.info("CONSULTA FINALIZADA!!")
    
    
    return clientes_encontrados, cliente_n_encontrado  



       

        
        

    



    # for dados in lista_clientes:




if __name__=='__main__':
    p.sleep(2)
    lista_usuarios= [{'nome': 'MIRLLA MOURA ALVES', 'valor': '6133.47', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52'}, {'nome': 'RAIMUNDO CAMPOAMOR DE AGUIAR ROCHA FILHO', 'valor': '1920.0', 'Emp fandi': 'JANGADA VEICULOS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52'}, {'nome': 'SAMIA MARIA ALENQUER DA SILVA', 'valor': '3807.53', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52'}, {'nome': 'JULIO CEZAR LIMA CAMINHA', 'valor': '2943.01', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52'}, {'nome': 'ESTEFANIA MARIA ROCHA SILVA', 'valor': '360.0', 'Emp fandi': 'NOVALUZ BS', 'Valor total nf': 15164.01, 'Empresa': 'NOVALUZ BS', 'datas': '04/03/2024 09:05:52'}]
                    
    a, _ = glob_consultar_situacao_cliente(lista_usuarios)
    print(a)
    


    


