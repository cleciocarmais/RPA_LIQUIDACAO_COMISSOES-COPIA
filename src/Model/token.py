import json
import os

def GetToken():
    with open(f"{os.getcwd()}\\token.json", "r") as file:
        informacao  =  json.load(file)
    return informacao

def SetToken(valor = None, lanc = None):
    dados =  GetToken()
    with open(f"{os.getcwd()}\\token.json", "w") as file:
        if valor != None:
            dados["valor"] = valor
        if lanc != None:
            dados["numero_lanc"] = lanc
        json.dump(dados, file, indent=4)
def resert():
    dados =  GetToken()
    with open(f"{os.getcwd()}\\token.json", "w") as file:
            dados["valor"] = 0
            dados["numero_lanc"] = 0
            json.dump(dados, file, indent=4)
        










if __name__ == "__main__":
    
    infor  = GetToken()
    print(infor["valor"])