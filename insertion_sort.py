lista = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def insertionSort(lista):
	for j in range(1, len(lista)):
		key = lista[j]
		i = j -1
		while i > -1 and lista[i] > key:
			lista[i + 1] = lista[i]
			i -= 1
		lista[i + 1] = key
	return lista

print(insertionSort(lista))