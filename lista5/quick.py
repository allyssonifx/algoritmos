def quick_sort(vetor, inicio, fim, relatorio):
    if inicio < fim:
        pivo = vetor[inicio]
        esquerda = inicio + 1
        direita = fim
        while esquerda <= direita:
            while esquerda <= direita and vetor[esquerda][0] <= pivo[0]:
                esquerda += 1
            while esquerda <= direita and vetor[direita][0] >= pivo[0]:
                direita -= 1
            if esquerda < direita:
                vetor[esquerda], vetor[direita] = vetor[direita], vetor[esquerda]
                relatorio.append((vetor[esquerda][0], vetor[direita][0]))
        vetor[inicio], vetor[direita] = vetor[direita], vetor[inicio]
        relatorio.append((vetor[inicio][0], vetor[direita][0]))
        quick_sort(vetor, inicio, direita - 1, relatorio)
        quick_sort(vetor, direita + 1, fim, relatorio)

bases = []
while True:
    try:
        posicao, base = input().split()
        bases.append((int(posicao), base))
    except:
        break

retorno = []
quick_sort(bases, 0, len(bases) - 1, retorno)

count = 0
for pos1, pos2 in retorno:
    if pos1 != pos2:
        if count < len(retorno)-1:
            print(pos2,pos1)
        else:
            print(pos2,pos1,end='')
