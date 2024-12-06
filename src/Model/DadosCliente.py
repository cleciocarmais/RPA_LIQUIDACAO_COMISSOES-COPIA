import json
import os
def OPenJson():
    with open(f"{os.getcwd()}\\Cliente_feitos.json" , "r") as file:
        informacao = json.load(file)
        file.close()
    return informacao

def GetDadosCliente():
    infor = OPenJson()
    return infor['dados']

def SetDadosCliente(dados):
    infor = OPenJson()
    print(infor)
    with open(f"{os.getcwd()}\\Cliente_feitos.json", "w") as save:
        infor["dados"].append(dados)
        json.dump(infor, save, indent=4)
        save.close()

def DestroyInfor():
    infor = OPenJson()
    print("ZERANDO DADOS DA LIQUIDACAO")
    
    print(infor)
    with open(f"{os.getcwd()}\\Cliente_feitos.json", "w") as save:
        infor["dados"] = []
        json.dump(infor, save, indent=4)
        save.close()



if __name__ == "__main__":
    # SetDadosCliente({"nome" : "clecio", "senha" : "123"})
    infor = GetDadosCliente()
    for a in infor:
        print(a["nome"])
