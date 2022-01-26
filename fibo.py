import time
import numpy as np
import statistics as stats

#Función para medir el tiempo, recibe una función y regresa el valor del tiempo de ejecución de ésta
def mide_tiempo(funcion):
	def funcion_medida(*args, **kwargs):
		inicio = time.time()
		c = funcion(*args, **kwargs)
		D = time.time() - inicio
		return D
	return funcion_medida
	
#Función de Fibonacci Recursiva
def fiboRecursivo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fiboRecursivo(n-1) + fiboRecursivo(n-2)
		
#Función iterativa de Fibonacci
def fiboiterativo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		a = 0
		b = 1
		for i in range(2,n+1):
			c = a + b
			a = b
			b = c
		return c
    	
    	
def main():
	#Se relacionan las funciones recursiva e iterativa con la función que mide el tiempo
	frc = mide_tiempo(fiboRecursivo) 
	fit = mide_tiempo(fiboiterativo)
	matrix_Rec = np.empty((5,5))
	matrix_Ite = np.empty((5,5))
	
	for j in range(0, 5): #Ciclo para realizar la medición 5 veces para cada valor de n
		print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
		it = 0
		
		for i in range(0, 25, 5):
			#Se guardan los valores obtenidos en las 5 mediciones para obtener un promedio
			matrix_Rec[it][j] = frc(i)
			matrix_Ite[it][j] = fit(i)
			it += 1
			print("Indice: ", i, "\nRecursivo: ")
			print(frc(i)) #Se llama a la función recursiva para obtener su tiempo de ejecución
			print("\nIterativo: ")
			print(fit(i)) #Se llama a la función iterativa para obtener su tiempo de ejecución
			print()
	
	#Ciclo para imprimir el promedio de tiempo de ejecución para los valores de 0 a 20, para ambas funciones
	for k in range(0,5):
		print("\n\nPromedio de tiempo de ejecucion para el valor ", k*5," de la funcion RECURSIVA: ")
		print(stats.mean(matrix_Rec[k]))
		print("Promedio de tiempo de ejecucion para el valor ", k*5," de la funcion ITERATIVA: ")
		print(stats.mean(matrix_Ite[k]))
		print()
		
	return 0
	
if __name__=='__main__':
	main()