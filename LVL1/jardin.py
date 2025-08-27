# 50 E 

# pyramide = []

# for E in range (0,51):
#     P = E**2
#     pyramide.append(P)
# print(pyramide[50])

# somme=[]
# for E in range (0,51):
#     if E%3==0:
#         P=E**2
#         somme.append(P)
# tupsomme=tuple(somme)
# total=sum(tupsomme)
# print(total)

total= sum(n**2 for n in range(51) if n%3==0)
print(total)



    