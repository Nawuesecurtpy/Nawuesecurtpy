def funcion_Max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(funcion_Max(20,5))
print(funcion_Max(5,355))

def funcion_De_Tres(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

print(funcion_De_Tres(350,20,140))

