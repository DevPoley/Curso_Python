a = {1,2,3}
b = {4,5,6}
c = {1,2,3,8}
e = {11,12,13,14,15}
print ("a==b ", a==b)
print ("a==b ", a==c)
d = a|b|c # Une conjuntos (AltGr+1= |), UNION
print ("a|b|= ", d) # Res= {1, 2, 3, 4, 5, 6, 8}, Descarta los duplicados

d = a&c
print ("a&c=", d) # Res= {1, 2, 3}, INTERSECCIÓN, solo comunes a los 2 conjuntos

d = a-b
print ("a-b=", d) # Res= {1, 2, 3} DIFERENCIA A con respecto B, aquellos no repetidos en "a"

d = a^b # DIFERENCIA SIMETRICA
print("a^b= ", d) # Res= {1, 2, 3, 4, 5, 6}, todos menos los que se repiten entre ellos

# a es SUBCONJUNTO DE c ?
print("a.issubset", a.issubset(c)) # a es subconjunto de c
print("a.issubset(c)", a.issubset(c)) # a es subconjunto  de c
print("a.issuperset(c)", a.issuperset(c)) # d es subconjunto  de c
print("a.isdisjoint(e)", a.isdisjoint(e)) # A es disconexo de e, ningun componente en común

# f.add(4) , frozenset(conjunto}) hace que no se puede modificar el conjunto
f = frozenset({1,2,3}) # pasa a ser un conjunto inmutable
f ={1,2,3}
f.add(4)
print("permite agregar: ", f) # este si es mutable(que se puede modificar)

print(a <= c) # Res= True, forma 2
print(a >= c) # Res= True, forma 2

