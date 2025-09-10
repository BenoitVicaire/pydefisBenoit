data_raw="NDNKCNVNUGYWRGCNABGSNCRACGSHWNNCYBCSNVUAAGDCMNKNYNNBNCGUBHUNRANDGDMDRSYMGSNWHNDNCVCMAMCANWKYRKVMWMKC"
arn_possible=""
list_arn_possible=[]

i=0

# def write_variations(index,data,variation_actuelle): 
#     nouvelle_variation=variation_actuelle
    
#     if (index==len(data)):
#         list_arn_possible.append(nouvelle_variation)
#         return
#     if (data[index]=="A"):
#         nouvelle_variation=variation_actuelle+"A"
#         write_variations(index+1,data,nouvelle_variation)
#     if (data[index]=="C"):
#         nouvelle_variation=variation_actuelle+"C"
#         write_variations(index+1,data,nouvelle_variation)
#     if (data[index]=="G"):
#         nouvelle_variation=variation_actuelle+"G"
#         write_variations(index+1,data,nouvelle_variation)
#     if (data[index]=="U"):
#         nouvelle_variation=variation_actuelle+"U"
#         write_variations(index+1,data,nouvelle_variation)
#     if (data[index]=="R"):
#             for j in range (2):
#                 if (j==0):
#                     nouvelle_variation=variation_actuelle+"A"
#                     write_variations(index+1,data,nouvelle_variation)
#                 if (j==1):
#                     nouvelle_variation=variation_actuelle+"G"
#                     write_variations(index+1,data,nouvelle_variation)

# write_variations(0,data_raw,"")
# print(list_arn_possible)

# création d'une dictionaire des symboles possibles


# Soltuion theoriquement fonctionnelle mais trop couteuse
# dict_symbole ={
#     "R":["A","G"],
#     "Y":["C","U"],
#     "K":["G","U"],
#     "M":["A","C"],
#     "S":["C","G"],
#     "W":["A","U"],
#     "B":["C","G","U"],
#     "D":["A","G","U"],
#     "H":["A","C","U"],
#     "V":["A","C","G"],
#     "N":["A","C","G","U"]
# }


# def write_variation(index,data,variation_actuelle):
#     if (index==len(data)):
#         list_arn_possible.append(variation_actuelle)
#         return
#     lettre=data[index]
#     if (lettre in dict_symbole):
#         for element in dict_symbole[lettre]:
#             write_variation(index+1,data,variation_actuelle+element)
#     else:
#         write_variation(index+1,data,variation_actuelle+lettre)
        
# write_variation(0,data_raw,"")
# signature=len(list_arn_possible)%100000


dict_symbole ={
    "A":[1],
    "C":[1],
    "G":[1],
    "U":[1],
    "R":[2],
    "Y":[2],
    "K":[2],
    "M":[2],
    "S":[2],
    "W":[2],
    "B":[3],
    "D":[3],
    "H":[3],
    "V":[3],
    "N":[4]
}


combinaison=1
for letter in data_raw:
    combinaison*=dict_symbole[letter][0]
result=combinaison%100000
print(result)



# # Bonus : 
# score = {c: 1 for c in 'ACGU'}
# score |= {c: 2 for c in 'RYKMSW'}
# score |= {c: 3 for c in 'BDHV'}
# score['N'] = 4

# print(score)

# score = {}
# for value, word in zip(range(1,5), ('ACGU', 'RYKMSW', 'BDHV', 'N')):
#     print(f'Adding letters of {word} with value {value}')
#     score |= {c: value for c in word}
# print(score)