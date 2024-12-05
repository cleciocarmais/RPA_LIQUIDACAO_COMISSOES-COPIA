import json



def GetToken():
    with open("token.json", "r") as file:
        informacao  =  json.load(file)
    return informacao

def SetToken(valor = None, lanc = None):
    dados =  GetToken()
    with open("token.json", "w") as file:
        if valor != None:
            dados["valor"] = valor
        if lanc != None:
            dados["numero_lanc"] = lanc
        json.dump(dados, file, indent=4)

        










if __name__ == "__main__":
    
    infor  = GetToken()
    print(infor["valor"])