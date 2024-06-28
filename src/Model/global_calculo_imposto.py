import pyautogui as p
def glob_imposto_irrf(valor_cliente):
    valor = float(valor_cliente) * (1.5 / 100)
    valor_round = round(valor,2)
    valor_transf_strint= str(valor_round)
    valor_irrf = valor_transf_strint.replace(".",",")
    return valor_irrf
def glob_calculo_valor(valor):
    valor_desconto = float(valor) * (100-1.5) / 100
    valor_round = round(valor_desconto, 2)
    valor_final = str(valor_round)
    valor_com_Desconto = valor_final.replace('.',',')
    return valor_com_Desconto


        
if __name__=='__main__':
    print("ola")
    # valor_resultao1 = calculo_valores_divergente(360,365.93)
    # valor_resultao2 = calculo_valores_divergente(365.93,360)
    # valor_resultao3 = calculo_valores_divergente(45,89)
    # print(f" VALOR IGUAL :{valor_resultao1}", '\n')
    # print(f" VALOR MAIOR DEALER :{valor_resultao2}", '\n')
    # print(f" VALOR  MAIOR DEALER:{valor_resultao3}", '\n')