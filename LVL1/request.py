from defisurl import DefisUrl

d = DefisUrl('https://pydefis.callicode.fr/defis/ExempleURL/get/BenoitVicaire/561b4', verify=True) # Mettez votre URL personnalisée ici
lignes = d.get()

# Affichage pour contrôle :
print("\n".join(lignes))
answer=int(lignes[0])+int(lignes[1])
print(answer)

rep=d.post(answer)