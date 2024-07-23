a = 10
b = 15
c = 20
resultado = ( (a<b) and (b<c) )
print(a<b , " and ", b<c, " : ", resultado)
resultado = ( (a>b) and (b<c) )
print(a<b , " and ", b<c, " : ", resultado)
resultado = ( (a<b) or (b<c) )
print(a>b , " or ", b<c, " : ", resultado)
resultado = ( (a<b) and (b<c) )
print(a<b , " and ", b<c, " : ", resultado)
resultadoNegado = not resultado
print("Mi resultado negado", resultado, " : ", resultadoNegado, "Le ponemos NOT y cambiamos el resultado FINAL")