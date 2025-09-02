def time(seconde):
    minutes=seconde//60
    secondes_restantes=seconde%60
    heures=minutes//60
    minutes_restantes=minutes%60
    hours = f"h:{heures} ,m:{minutes_restantes} ,s:{secondes_restantes}"
    return hours

print(time(300))

chauves_souris=0
skellingtons=0
zombies=0
fantomes_baveux=0
t=0
while (t<(50*60)):
    if t%2==0:
        chauves_souris+=10
    if t%5==0:
        skellingtons+=5
    if t%6==0:
        
    t+=1