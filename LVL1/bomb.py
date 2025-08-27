serial_number=797114

U = serial_number // 1000
N = serial_number % 1000


# Version à moi
# for x in range (N):
#     U=U *13
#     U = U % 1000
#     print(f"{U:03d}")

# Version propre

U_final = (U *pow(13, N , 1000)) % 1000
print(f"{U_final:03d}")