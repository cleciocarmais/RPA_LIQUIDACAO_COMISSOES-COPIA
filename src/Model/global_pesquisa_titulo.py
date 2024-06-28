import logging
import pyautogui as p
import traceback
import pyperclip as pyp
from src.Model.global_utilitarios import glob_nomes_empresas_Delear

# from clickApi import click2 as c
from src.Model.global_clickApi import click2 as c
def glob_pesquisar_titulo_client(infor_cliente):
    """
        PESQUISA TITULO DO CLIENTE PELO, CASO ENCONTRE O TITULO RETORNA TRUE \n
        CASO N ENCONTRO RETORNA FALSE \n

        ------ PARAMENTRO ------ \n
        
        DICIONARIO DE INFORMACOES DE CLIENTE
    """
    Nome_cliente = infor_cliente['nome']
    id = infor_cliente['id_cliente']
    img = 'C:/RPA/arquivos/images/'
    print(Nome_cliente)
    p.alert('ola')
    
    p.sleep(0.5)
    p.hotkey('alt','u') #acessando titulos
    p.sleep(0.5)
    p.press('Enter')
    p.sleep(1 )
    print("aguarde!!!")
    
    p.sleep(2)

    ancora_titulo = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)
    while ancora_titulo == None:
        p.sleep(1)
        print("Aguarde tela de titulos")
        ancora_titulo = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)

    if ancora_titulo != None:
        c(ancora_titulo.x+100, ancora_titulo.y)
    else:
        logging.info('Erro na imagem ancora_titulo')
    p.sleep(1)

    if infor_cliente['Empresa'] != infor_cliente['Emp fandi']:
        empresa_tituto_consulta = p.locateCenterOnScreen(f'{img}empresa_consulta_titulo.png', confidence=0.95)
        if empresa_tituto_consulta != None:
            c(empresa_tituto_consulta.x+90, empresa_tituto_consulta.y)
        p.sleep(1)
        p.write(glob_nomes_empresas_Delear[infor_cliente['Emp fandi']])
        p.press('Enter')
        
    p.sleep(1)

    ancora_endosado = p.locateCenterOnScreen(f'{img}endosado.png', confidence=0.95)

    if ancora_endosado != None:
        c(ancora_endosado.x+25,ancora_endosado.y)
        p.write(id)
    else:
        logging.info("Erro na variavel ancora_endosado")


    p.press('Tab')
    p.sleep(1)
    if Nome_cliente == 'FRANCISCO HELIOMAR DE LIMA BERNARDO        ':
        p.write('PP')
        p.press('Tab')
        p.sleep(0.5)
    else:
        p.write('PB')
        p.press('Tab')
        p.sleep(0.5)

    emAberto = p.locateCenterOnScreen(f'{img}em_aberto_liquidacao.png', confidence=0.95)
    if emAberto != None:
        c(emAberto.x,emAberto.y)
    else:
        logging.info('Erro na variavel emAberto')
    p.sleep(1)

    #TODO NÃO EXCLUIR ESSA COMENTARIO
    # todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
    # if todos != None:
    #     c(todos.x, todos.y)
    # else:
    #    print("  Erro na variavel todos")
    

    btn_ok = p.locateCenterOnScreen(f'{img}btn_ok_desmarcado.png', confidence=0.95)

    if btn_ok !=None:
        c(btn_ok.x,btn_ok.y)
    else:
        logging.info('Erro ao processa Variavel btn_ok')


    p.sleep(3)
    sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
    btn_ok = p.locateCenterOnScreen(f'{img}ok100.png', confidence=0.95)
    if sem_dados != None:
        print('( X ) TITULO NÃO ENCONTRADO ( X )')
        logging.info('( X ) TITULO NÃO ENCONTRADO ( X )')
        p.sleep(1)
        c(btn_ok.x,btn_ok.y)
        p.sleep(1)
        
        cancela = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        if cancela !=None:
            c(cancela.x, cancela.y)
        p.sleep(0.5)

        fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        while fechar != None:
                c(fechar.x,fechar.y)
                p.sleep(1)
                fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        
        return False
    else:
        print("( OK ) TITULO ENCONTRADO ( OK )")
        logging.info("( OK ) TITULO ENCONTRADO ( OK )")
        todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
        while todos !=None:
            p.sleep(0.5)
            todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
            p.sleep(1)
        p.press('Enter')
        p.sleep(1)
        p.sleep(1)
        return True
    

if __name__ == '__main__':
    p.sleep(2)
    dados = {'nome': 'Paulo Roberto lima castelo ', 'valor': '1003.54', 'Emp fandi': 'NISSAN MATRIZ', 'Valor total nf': '6886.44', 'Empresa': 'NOVALUZ WS', 'datas': '20/01/2024 09:10:33', 'id_cliente': '0476729'}
    
    glob_pesquisar_titulo_client(dados)
