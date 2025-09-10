drages=["A","B","E","C","G","F","M","O","H","P","S","V"]
bingo={"A","E","G","H"}

i=0
counter=0
while set(drages[:4]) != bingo :
    
    i+=1
    
    if (i>=1000):
        break

    j=i%len(drages)
    if (i!=0 and i%5==0 ):
        print(f"echange of {drages[j-1]} and {drages[j-2]}")
        drages[j-1],drages[j-2]=drages[j-2],drages[j-1]
        print(drages)
        counter+=1
    
print(drages)
print(counter)
