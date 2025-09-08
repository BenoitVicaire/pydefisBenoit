message="""←↓↓↓↑←←AB←↓BBA→→↓↑↓B→→→←↓B↑←→←←A→→↑B→←→↑
↓AA↓↓B→→↑↓→↑→A→→A↓↓↓↑←BA←B→→→←AAAA↑←↓↓↓A
↓↑→B→→←↓BA→→↑←BA→A→←↑←AB→→→↑←→↑↑→↑↓↑↓↓A→
→←↑↓←↓BA→→ABBA←A→→←A↓↑→←↓↑↓BBA←A→→→→←→↓↓
→←→↑→→BA↓↑→→←A↓B↑←↑B→BA↓↓B→→→←↓B→→↑↓→←←↓
←↓BA↓↑→→ABBA←A→→←A↓↓↓BA↓↓↓↓B↑↑BA←A←B→→→←
↑↑↑←↓←←A→→→←↑B↓↓→↑↑←→→↓↑BA↓A↓B→→↓↑BB↓↑BA
→→→←↓B↑→→→→←←→→↑↑↓BA←A→→→→↓↑BA↓A↓↑→←A↓↓B
←↓→←→↑↑←BA←A←B→→↓↑↓B→→BA↓A↓↑↑←BA↑←→←←A→→
BA↓AAA→↑↓A→→AB→←↓A←A→→←↓→←→→↑↓→←←ABA→→AB
BA←A→→↑↓→←A↓↓↑→B↑←→↑→←↓A←A→→↑↑BA↓B↑↑←↓→B
BA→→ABBA→→↑←↓↓↑↓↓↓↓↑←A→→↑↓→↑↑↑↓←ABBA←A↓→
→→↑↑↓B→↑←A←B→→↓↑↓B→→AB→BA↓↓↓↓B↑B↑←→↑↑←→←
←A→→←↓BA→→A↓BA↑←↑BBA→←↓B←B→→B←↓BB→→↑←↓→→
↓↑BA→→AA→←↓BAB↑←→←→→AB→B↓↑↑←↓B→↑↑←BA↓→→→
BA↓↑→→↓ABA→→↓↑B→→←↑B→↑←ABA→→↑↑→←←A→→ABBA
→→A↓↓↓←→←→BA↓AA↓BA↑←→→A←→→AB→BA↓←←→↑AAAA
↑←BA↑←→→A↓BA→→←→BA←A←A→←→ABA→→A←→→←↓→←→→
←→→←→↑↓A→→BA↓A→→↑↑→←↑←↓↑→←↓A↓↑→→ABBA→→←↓
→←→→AA→↑↓A←B→→A↓→←↑←→→←→↓↓↓A→→↓↓↑↓↑ABAA↓
↓↑→↑AA→→BA←A↓↑→→ABBA→→↓↑BA→→AB→BA↓↓↓↓B↑←
→←→ABA↑←→→ABB→→←→A→↑↑←→→ABBA→→←↓→←→→←A↓↓
↑←↓↑BA↓→"""
decypher_input="""←← -> h
←↑ -> !
←→ -> m
←↓ -> l
←A -> s
←B -> ,
↑← -> r
↑↑ -> p
↑→ -> x
↑↓ -> b
↑A -> j
↑B -> v
→← -> a
→↑ -> i
→→ ->  
→↓ -> w
→A -> g
→B -> é
↓← -> è
↓↑ -> t
↓→ -> .
↓↓ -> o
↓A -> n
↓B -> u
A← -> à
A↑ -> ?
A→ -> y
A↓ -> c
AA -> f
AB -> d
B← -> q
B↑ -> k
B→ -> '
B↓ -> z
BA -> e
BB -> ê"""
# decypher_input=decypher_input.replace("\n",",")
# print(decypher_input)

instruction_raw=decypher_input.replace(" ","")
instruction_raw=instruction_raw.split("\n")

message=message.replace("\n","")



instruction_dict={}
for element in instruction_raw:
    splited_element=element.split("->")
    instruction_dict.update({splited_element[0]:splited_element[1]})
# print(instruction_dict.get("BB"))

# option 1 : boucler sur le dico de decryptage et modifier tout le message

# decyphered_message=message
# for key in instruction_dict:
#     decyphered_message=decyphered_message.replace(key,instruction_dict.get(key))
# print(decyphered_message)

# option 2: split tout les 2 char le message, boucler sur la liste et convertir l'instruction

# option 3 : Boucler sur le message
decyphered_message=""
for i in range (0,len(message)-1,+2): 
    couple=message[i]+message[i+1]
    decyphered_message+=instruction_dict[couple]
splited_message=decyphered_message.split(",")
print(splited_message[4])