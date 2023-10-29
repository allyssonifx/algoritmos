# def main():
#     MOD = 10**9 + 7
#     N, K = map(int, input().split())

#     divisors = [[] for _ in range(N+1)]
#     for i in range(1, N+1):
#         for j in range(1, int(i**0.5)+1):
#             if i % j == 0:
#                 divisors[i].append(j)
#                 if j != i//j:
#                     divisors[i].append(i//j)

#     memo = [[-1] * (K+1) for _ in range(N+1)]
#     def count_seqs(n, k):
#         if k == 1:
#             return 1
#         if memo[n][k] != -1:
#             return memo[n][k]
#         seqs = 0
#         for d in divisors[n]:
#             seqs += count_seqs(d, k-1) % MOD
#         memo[n][k] = seqs % MOD
#         return seqs % MOD

#     seqs = sum(count_seqs(i, K) for i in range(1, N+1)) % MOD

#     print(seqs, end='')

# if __name__ == '__main__':
#     main()

def count_seqs(N, K):
    MOD = 10**9 + 7
    memo = [[0] * (N+1) for _ in range(K+1)]
    for n in range(1, N+1):
        memo[1][n] = 1

    for k in range(2, K+1):
        for n in range(1, N+1):
            for d in range(1, n+1):
                if n % d == 0:
                    memo[k][n] = (memo[k][n] + memo[k-1][d]) % MOD

    return sum(memo[K]) % MOD

N, K = map(int, input().split())
print(count_seqs(N, K),end='')

