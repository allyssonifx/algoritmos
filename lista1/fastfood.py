class caixa:
    def __init__(self):
        self.livre = True
        self.valorPerdido = 0
    def somarValor(self,valor):
        if(self.livre==False):
            self.valorPerdido = self.valorPerdido+valor
        else:
            self.livre=False
    def status(self):
        if(self.livre):
            self.livre = False
        else:
            self.livre = True


def main():
    caixa1 = caixa()
    caixa2 = caixa()
    caixa3 = caixa()
    while True:
        try:
            entrada = input()
            divisor = entrada.split(" ")
            if(divisor[0]=="PROXIMO"):
                if(divisor[1]=="1"):
                    caixa1.status()
                elif(divisor[1]=="2"):
                    caixa2.status()
                else:
                    caixa3.status()
            else:
                if(divisor[0]=="1"):
                    caixa1.somarValor(int(divisor[1]))
                elif(divisor[0]=="2"):
                    caixa2.somarValor(int(divisor[1]))
                else:
                    caixa3.somarValor(int(divisor[1]))
        except:
            break
        
    print(f'CAIXA 1: {caixa1.valorPerdido}')
    print(f'CAIXA 2: {caixa2.valorPerdido}')
    print(f'CAIXA 3: {caixa3.valorPerdido}') 
            
if __name__ == '__main__':
    main()
