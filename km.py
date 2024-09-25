print(" ") # print imprime un espacio

print("Briana Sarahi Sanchez Perez 3-w") 
print(" ") # print imprime un espacio

def div(l, k): # se da el nombre de la funcion y los argumentos 
    return (l / k) # indica el final de la funcion

k = float(input('Ingrese la cantidad de kilometros recorridos: '))# se solicita la canidad de kilometros 
l = float(input('Ingrese la cantidad de litros de combustible utilizdos: ')) # se solicita la cantidad de litros

print(f'El consumo de combustible por kilómetro de {k} kilometos y de {l} litos de combustible es: {div(l, k)}') # se hace la peracion de la funcion y se imprime

print(" ") # print imprime un espacio