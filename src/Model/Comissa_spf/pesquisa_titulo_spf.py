import logging
import pyautogui as p
import traceback
import pyperclip as pyp
import sys
sys.path.append(r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_COMISSOES')
from src.Model.global_utilitarios import glob_nomes_empresas_Delear

# from clickApi import click2 as c
from src.Model.global_clickApi import click2 as c

def pesquisar_titulo_comissao_spf(infor_cliente):

    """
    FUNÇÃO QUE BUSCA TITULO DO CLIENTE USANDO NUMERO DO CLIENTE \n 
    RETORNO UM TRUE CASO ENCONTRE
    RETORNO UM FALSE CASO NÃO ENCONTRE 
    
    
    
    
    """
    Nome_cliente = infor_cliente['nome']
    img = 'C:/RPA/arquivos/images/'
    print(f'*PESQUISADO TITULO  DE { Nome_cliente }')   
    logging.info(f'*PESQUISADO TITULO  DE { Nome_cliente }')
    p.sleep(0.5)
    p.hotkey('alt','u') #acessando titulos
    p.sleep(0.5)
    p.press('Enter')
    p.sleep(1 )
    
    p.sleep(2)

    ancora_titulo = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)
    while ancora_titulo == None:
        p.sleep(1)
        print(" aguarde")
        ancora_titulo = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)

    if ancora_titulo != None:
        c(ancora_titulo.x+100, ancora_titulo.y)
    else:
        logging.info('  Erro na imagem ancora_titulo')
    p.sleep(1)
    if infor_cliente['Empresa'] != infor_cliente['Emp fandi']:
        empresa_tituto_consulta = p.locateCenterOnScreen(f'{img}empresa_consulta_titulo.png', confidence=0.95)
        if empresa_tituto_consulta != None:
            c(empresa_tituto_consulta.x+90, empresa_tituto_consulta.y)
            
        
        p.sleep(1)
        p.write(glob_nomes_empresas_Delear[infor_cliente['Emp fandi']])
        p.press('Enter')

        
    p.sleep(1)
 
    p.sleep(1)
    input_sacador = p.locateCenterOnScreen(f'{img}sacado.png', confidence=0.95)
    if input_sacador != None:
        c(input_sacador.x+80, input_sacador.y)
        p.write("0048438")
        p.press("Tab")

    ancora_endosado = p.locateCenterOnScreen(f'{img}endosado.png', confidence=0.95)

    if ancora_endosado != None:
        c(ancora_endosado.x+80,ancora_endosado.y)
    else:
        logging.info("Erro na variavel ancora_endosado")

    form_cpf = p.locateCenterOnScreen(f'{img}cpf.png', confidence=0.95)
    
    while form_cpf == None:
        p.sleep(1)
        form_cpf = p.locateCenterOnScreen(f'{img}cpf.png', confidence=0.95)
    cpf = (infor_cliente['cpfs_cnpj'])
    c(form_cpf.x+45, form_cpf.y)
    p.press('backspace',presses=3000)
    
    cpf = str(cpf)
    cpf = cpf.zfill(11)
    p.write(cpf)
    p.press('Enter')
    p.sleep(5)
 
    sem_dados2 = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
    if sem_dados2 != None:
        print("CLIENTE NÃO ENCONTRADO")
        logging.info("CLIENTE NÃO ENCONTRADO")
        p.press('Enter')
        p.sleep(2)
        p.hotkey('alt','c')
        p.sleep(2)
        p.hotkey('alt','c')
        fechar = p.locateCenterOnScreen(f'{img}fechar12.png', confidence=0.95)
        if fechar != None:
            c(fechar.x, fechar.y)
            return 'n_encontrado',""

    p.press('Enter')
    p.sleep(1)
    p.hotkey("Ctrl","c")
    id_cliente = pyp.paste()
    p.press('tab')
    p.sleep(1)
    
    p.write('SP')
    p.press('Tab')
    p.sleep(0.5)

    emAberto = p.locateCenterOnScreen(f'{img}em_aberto_liquidacao.png', confidence=0.95)
    if emAberto != None:
        c(emAberto.x,emAberto.y)
    else:
        logging.info('Erro na variavel emAberto')
    p.sleep(1)

    
    # todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
    # if todos != None:
    #     c(todos.x, todos.y)
    # else:
    #    print("  Erro na variavel todos")
    

    btn_ok = p.locateCenterOnScreen(f'{img}btn_ok_desmarcado.png', confidence=0.95)

    if btn_ok !=None:
        c(btn_ok.x,btn_ok.y)
    else:
        logging.info('  Erro ao processa Variavel btn_ok')
    print('    Esperando carregar infomaçoes')

    p.sleep(3)
    sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
    btn_ok = p.locateCenterOnScreen(f'{img}ok100.png', confidence=0.95)
    if sem_dados != None:
  
        p.sleep(1)
        c(btn_ok.x,btn_ok.y)
        cancela = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        if cancela !=None:
            c(cancela.x, cancela.y)
        p.sleep(0.5)
        fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        while fechar != None:
                c(fechar.x,fechar.y)
                p.sleep(1)
                fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        print("TITULO NÃO ENCONTRADO ")    
        logging.info("TITULO NÃO ENCONTRADO ")    
        return False,""
    
    else:
        print("TITULO ENCONTRADO COM SUCESSO!!")
        logging.info("TITULO ENCONTRADO COM SUCESSO!!")
        todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
        while todos !=None:
            print("  carregando informaçoes!!!!")
            p.sleep(0.5)
            todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
            p.sleep(1)
        p.press('Enter')
        p.sleep(1)
      

        p.sleep(1)
        
        #     p.sleep(2)
        return True,id_cliente
    

if __name__ == '__main__':
    p.sleep(2)
    dados = {'nome': 'Paulo Roberto lima castelo ', 'valor': '1003.54', 'Emp fandi': 'NISSAN MATRIZ', 'Valor total nf': '6886.44', 'Empresa': 'NOVALUZ WS', 'datas': '20/01/2024 09:10:33', 'id_cliente': '0476729'}
    
    pesquisar_titulo_comissao_spf(dados)
