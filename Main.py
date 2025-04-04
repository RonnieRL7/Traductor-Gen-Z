import random


thng = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
p1 = int(input("Cuantos caracteres quieres que tenga tu contrasena"))
con = ""
for i in range(p1):
    con += random.choice("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

print(con)
