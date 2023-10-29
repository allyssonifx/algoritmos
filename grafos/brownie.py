# def lucro(precos, g):
#     memo = [0] * (g + 1)
#     for i in range(1, g + 1):
#         max_lucro = 0
#         for j in range(1, i + 1):
#             preco = precos[j - 1 if j <= len(precos) else 0]
#             if j % 100 != 0:
#                 preco = 0
#             ganho = memo[i - j] + preco
#             if ganho > max_lucro:
#                 max_lucro = ganho
#         memo[i] = max_lucro
#     return "R$ {:.2f}".format(memo[g]).replace(".", ",")


# def main():
#     precos = list(map(float, input().replace(',', '.').split()))
#     gramas = int(input())
#     resultado = lucro(precos, gramas)
#     print(resultado)

# if __name__ == '__main__':
#     main()

# def lucro(precos,g):
#     dp = [[0 for j in range(g+1)] for i in range(len(precos))]
    
#     for i in range(len(precos)):
#         for j in range(g+1):
#             if i == 0:
#                 dp[i][j] = precos[i] * (j // (i+1))
#             else:
#                 dp[i][j] = dp[i-1][j]
#                 for k in range(j // (i+1) + 1):
#                     dp[i][j] = max(dp[i][j], k * precos[i] + dp[i-1][j - k * (i+1)])
    
#     return "R$ {:.2f}".format(dp[-1][-1]/100).replace(".", ",")

def lucro(precos, g):
    n = len(precos)
    dp = [[0 for _ in range(g + 1)] for _ in range(n)]
    peso = [100 * (i + 1) for i in range(n)]
    
    for j in range(1, g + 1):
        dp[0][j] = j // peso[0] * precos[0]
    
    for i in range(1, n):
        for j in range(1, g + 1):
            dp[i][j] = dp[i - 1][j]
            qtd = j // peso[i]
            for k in range(1, qtd + 1):
                lucro = k * precos[i] + dp[i - 1][j - k * peso[i]]
                if lucro > dp[i][j]:
                    dp[i][j] = lucro
    
    return "R$ {:,.2f}".format(dp[n - 1][g] / 100)


def main():
    precos = list(map(float, input().replace(',', '.').split()))
    g = int(input())
    print(lucro(precos, g).replace('.',','),end='')

if __name__ == '__main__':
    main()


