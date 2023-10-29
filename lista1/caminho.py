
def juntarTudo(caminhoList):
    listaAuxiliar = []
    caminhoFinal = ""
    print(caminhoList)
    #Monta o caminho final
    for c in range(0,len(caminhoList)):
        #Ignora os pontos
        if(caminhoList[c]=='.' or caminhoList[c]==''
    ):
            pass
        #quando for .. ignora a informação atual e mantém a anterior
        elif(caminhoList[c]=='..'):
            if(len(listaAuxiliar)-2>=0):
                listaAuxiliar.pop()
        else:
            listaAuxiliar.append(caminhoList[c])

    for caminhos in listaAuxiliar:
        if(caminhos != ''):
            caminhoFinal = caminhoFinal + caminhos+"/"

    if(len(caminhoFinal)==0):
        return "/"
    else:
        return caminhoFinal

def main():
    while True:
        try:
            caminho = input()
            caminhoList = caminho.split("/")
            caminho = juntarTudo(caminhoList)
            caminho = "/"+caminho
            if(caminho[len(caminho)-1]=="/"):
                caminho = caminho[:-1]
            print(caminho)
        except:
            break     

if __name__ == '__main__':
    main()
