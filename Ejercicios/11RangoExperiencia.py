'''entre 0 y 1(junior) , 1 y 3 semi junior, 3 y 5 senior, mas de 5 Director'''
anios = int(input("Cuantos años de experiencia tienes: "))
if anios >= 0 and anios <1: # opcion 2: if 0 <= anios < 1
    print("Eres Junior")
elif anios >= 1 and anios <3:# opcion 2: if 1 <= anios <3
    print("Eres Semi-Junior")
elif anios >= 3 and anios -5:
    print("Eres Senior")
elif anios >= 5:
    print("Eres Director")
else: 
    print("Introduce cantidades positivas") 