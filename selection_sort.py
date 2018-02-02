lista = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def selectionSort(lista):
	for i in range(len(lista) - 1):
		current_min = i
		for j in range(current_min + 1, len(lista)):
			if lista[j] < lista[current_min]:
				current_min = j

		lista[i], lista[current_min] = \
		lista[current_min], lista[i]
	return lista

print(selectionSort(lista))
