solution = []

for B in range (1,500):
    for R in range (B+1, 500):
        for N in range(R+1,2*B):
                T = R*B*N // 777
                if R*B*N == 777 * T and T< 1000 and T==(B+R+N):
                    solution.append((B,R,N,T))
T_values = [s[3] for s in solution]
print(T_values)

