def imprime_quadro(numeros):
	print('.' * (len(numeros) + 2))
	maior_numero = max(numeros)
	numeros_traduzidos = []
	for numero in numeros:
		numeros_traduzidos.append(['|' if n < numero else ' ' for n in range(maior_numero)][::-1])
	for linha in zip(*numeros_traduzidos):
		print('.' + ''.join(linha) + '.')
	print('.' * (len(numeros) + 2))

def bubble_sort(numeros):
	while numeros != sorted(numeros):
		for index in range(len(numeros) - 1):
			if numeros[index] > numeros[index + 1]:
				numeros[index], numeros[index + 1] = numeros[index + 1], numeros[index]
		imprime_quadro(numeros)

def selection_sort(numeros):
	index = 0
	while numeros != sorted(numeros):
		menor_numero = min(numeros[index:])
		index_menor_numero = numeros[index:].index(menor_numero) + index
		if numeros[index] > menor_numero:
			numeros[index], numeros[index_menor_numero] = menor_numero, numeros[index]
		index += 1
		imprime_quadro(numeros)

def insertion_sort(numeros):
	index_main = 1
	while numeros != sorted(numeros):
		index = index_main
		while index > 0 and numeros[index] < numeros[index - 1]:
			numeros[index], numeros[index - 1] = numeros[index - 1], numeros[index]
			index -= 1
		index_main += 1
		imprime_quadro(numeros)

algoritmos = {'bubble':bubble_sort, 'selection':selection_sort, 'insertion':insertion_sort}
algoritmo_escolhido = input()
numeros = [int(n) for n in input().split()]
imprime_quadro(numeros)
algoritmos[algoritmo_escolhido](numeros)