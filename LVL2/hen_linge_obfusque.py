from modules.fonction_html import extract_into_file
from bs4 import BeautifulSoup

# with open("assets\html\hen.html","r", encoding="utf-8")as file:
#     soup = BeautifulSoup(file,"html.parser")

# list_of_secret_word=[]

# for li in soup.find_all("li"):
#     b_tag=li.find("b")
#     if b_tag:
#         list_of_secret_word.append(b_tag.get_text())
# print(list_of_secret_word)

message= """MzZfiIFmMpPizwWZkbByYKfFjJkKusSbBUplLqisSlLdDIQPnrRnuUuU
sgkKfFdDGSxhHmMmMXgGjaAJpzZpeEPPnNpncmMinNIwpPWfFcCCNPnq
QxXNeqQhHraefFEdkKDpmMPARaqQqQikjJKmMoOIrRpPoOnNmyYMfFxX
koOsSKzZwefFEWvV yYyYjJpPEviIzeExXZxgGwWjkKJXmMxXVvVkqQo
OagxXGeEAoOpPtTntTNnNKjtTxXwWgGJunjJdDoONUspPSutTtgGTUhH
qlLrRQmuUjJnwfFWNxXpzZPyYlLzZMoOnweEfFWkwpPjJWnNxXKyYjJy
YfFuUicbBCcCpuUoOPoeEoOsgwWsaAsSSjJGkKeEnNSpPvVsmyYMoOsS
SOxXdyqQzZmMmMYnNDd"""
message=message.replace(" ","")
message=message.replace("\n","")
# print(type(message))
# stop_boucle=False
# while not stop_boucle:
#     for i in range (len(message)):
#         if message[i].islower() and message[i+1].isupper() and message[i]==message[i+1].lower():
#             message.pop(i),message.pop(i+1)

decrypted_message=[]
for i, letter in enumerate(message, start=0):
    if letter.isupper() and i>0 and letter.lower()==decrypted_message[len(decrypted_message)-1]:
        decrypted_message.pop()
    else:
        decrypted_message.append(letter)
print("".join(decrypted_message))

