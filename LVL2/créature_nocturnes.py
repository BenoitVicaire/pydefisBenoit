def time(seconde):
    minutes=seconde//60
    secondes_restantes=seconde%60
    heures=minutes//60
    minutes_restantes=minutes%60
    hours = f"h:{heures} ,m:{minutes_restantes} ,s:{secondes_restantes}"
    return hours

print(time(50*60))

chauves_souris=0
skellingtons=0
zombies=0
fantomes_baveux=0
pU=0


t=0

while (t<(50*60)):
    
    pU=t//(4*60)
    powerUp_cs=2*pU
    powerUp_s=pU
    powerUp_z=pU
    powerUp_fb=pU
    if t%2==0:
        chauves_souris+=10
    if t%5==0:
        skellingtons+=5
    if t%6==0:
        zombies+=4
    if t%10==0:
        fantomes_baveux+=3 
    if t%6==0:
        chauves_souris-=2+powerUp_cs
        chauves_souris=max(0,chauves_souris)
    if t%20==0:
        skellingtons-=1+powerUp_s
        skellingtons=max(0,skellingtons)
    if t%30==0:
        zombies-=1+powerUp_z
        zombies=max(0,zombies)
    if t%40==0:
        fantomes_baveux-=1+powerUp_fb
        fantomes_baveux=max(0,fantomes_baveux)
    t+=1
print(f"{chauves_souris}, {skellingtons}, {zombies}, {fantomes_baveux}")
print(powerUp_cs,powerUp_s,powerUp_z,powerUp_fb)
    

    