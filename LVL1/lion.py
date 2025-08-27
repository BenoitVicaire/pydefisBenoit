import string

abc=list(string.ascii_uppercase)
divinite ="ARTEMIS ASCLEPIOS ATHENA ATLAS CHARON CHIRON CRONOS DEMETER EOS ERIS EROS GAIA HADES HECATE HEPHAISTOS HERA HERMES HESTIA HYGIE LETO MAIA METIS MNEMOSYNE NYX OCEANOS OURANOS PAN PERSEPHONE POSEIDON RHADAMANTHE SELENE THEMIS THETIS TRITON ZEUS"
listdiv = divinite.split(" ")
dictionarie_word_value={}

# listdiv[i] retourne l'item i de listdiv, donc un mot entier
# listdiv[i][j] retourne l'item j de listdiv[i] : donc une lettre

for i in range (0,len(listdiv)):
    word=listdiv[i]
    word_value=0
    for j in range (0,len(word)):       
        word_value=word_value+abc.index(word[j])+1
        dictionarie_word_value[listdiv[i]]=word_value
        # print(word_value)
                
# print(dictionarie_word_value)
swapkey = ""
swapvalue = 0
# for i in dictionarie_word_value.items():
#     # if i[1] < (i-1)[1] :
#     #     swapkey = i[0]
#     #     swapvalue=i[1]
#     #     dictionarie_word_value.update(i)
#     print(i[1])

        # dictionarie_word_value.pop(i)
    # print(i)
    # print(i[1])
print(dictionarie_word_value.items())   
