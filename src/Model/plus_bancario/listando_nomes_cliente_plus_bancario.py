import pandas as pd
import pyautogui as p
import logging
def listando_clientes_plus_bancario(df,index,lista_qtde_clientes,lista_empresa_fandi):
    """
        PEGA OS NOME E EMPRESA FANDI DE CADA CLIENTE SALVA 
        DENTRO DE  ARRAY DICIONARIO. RETORNO UM ARRAY DE DICIONARIO\n
        CONTENDO : \n
        [{   
        Emp fandi           : exemplo
            Valor total nf  : exemplo
            Empresa         : exemplo
            datas        : exemplo
        }]\n
-------- PARAMETROS -------- \n
            DATAFRAME \n
            INDEX DO DATAFRAME \n
            ARRAY DE CLIENTE\n
            ARRAY DE EMPRESA FANDI :

    
    """
    print("*LISTANDO NOMES DOS CLIENTES ")
    logging.info("*LISTANDO NOMES DOS CLIENTES ")
    print("Aguarde!!!")
    lista_clientes = []
    # Percorrendo cada linha da planilha
    # Limpando a lista de clientes para a próxima iteração
    lista_clientes.clear()
    # Calculando o incio do for de clientes
    inicio = (10 - int(lista_qtde_clientes)) + 1
    # Percorrendo cada cliente
    for j in range(inicio, 11):
        # Criando list_comprehensions para os clientes que existem
        nome_cliente = [str(x) for x in df[f'Nome do Cliente {j}']][index]
        valor_cliente = [str(x) for x in df[f'Valor {j}']][index]
        # Adicionando os clientes em uma lista
        lista_clientes.append({
        'nome': nome_cliente,
        'valor': valor_cliente,
        })
   
    nova_lista_empresa_fandi = lista_empresa_fandi.split(',')
    for posicao,cliente in enumerate(lista_clientes):

            cliente['Emp fandi'] = nova_lista_empresa_fandi[posicao]
            cliente['Valor total nf'] = df['Valor Total da Nota Fiscal'][index]
            cliente['Empresa'] = df['Empresa'][index]
            cliente['datas'] = df['Carimbo de data/hora'][index]
    print('PROCESSO FINALIZADO!!!!')
    logging.info('PROCESSO FINALIZADO!!!!')
    return lista_clientes
     
