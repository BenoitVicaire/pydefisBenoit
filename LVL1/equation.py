# Enoncé :
# A=8
# B=5
# T=11
# R=74
# x*A+y*B=74
# x+y=11
A=8
B=5
T=11
R=74
possible=False
for x in range (0,T+1):
    y=T-x
    if A*x + B*y ==R:
        print(f"x={x} et y={y}")
        possible=True
if possible==False:
    print("pas de solution")

  