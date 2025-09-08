import string

abc=list(string.ascii_uppercase)
divinite ="ARTEMIS ASCLEPIOS ATHENA ATLAS CHARON CHIRON CRONOS DEMETER EOS ERIS EROS GAIA HADES HECATE HEPHAISTOS HERA HERMES HESTIA HYGIE LETO MAIA METIS MNEMOSYNE NYX OCEANOS OURANOS PAN PERSEPHONE POSEIDON RHADAMANTHE SELENE THEMIS THETIS TRITON ZEUS"
listdiv = divinite.split(" ")
# dictionarie_word_value={}
list_word_value=[]

# listdiv[i] retourne l'item i de listdiv, donc un mot entier
# listdiv[i][j] retourne l'item j de listdiv[i] : donc une lettre

for i in range (len(listdiv)):
    word=listdiv[i]
    word_value=0
    for j in range (len(word)):       
        word_value=word_value+abc.index(word[j])+1
    temp_tuple=(listdiv[i],word_value)
    list_word_value.append(temp_tuple)


# print(list_word_value)
# for i in range (len(list_word_value)**5):
#     if list_word_value[i%34][1] < list_word_value[i%34+1][1]:
#         list_word_value[i%34],list_word_value[i%34-1] = list_word_value[i%34-1],list_word_value[i%34]
# print(list_word_value)

list_word_value.sort(key=lambda a: a[1])
solution=""
for i in range (len(list_word_value)):
    solution=solution+" " +list_word_value[i][0]
print(solution)

print(ord("B")-ord("A"))
print(chr(65+19))