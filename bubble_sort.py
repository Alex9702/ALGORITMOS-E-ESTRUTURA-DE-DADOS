lista = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def bubbleSort(lista):
	swapped = True

	while swapped:
		swapped = False
		for i in range(0, len(lista)-1):
			if lista[i] > lista[i + 1]:
				lista[i], lista[i + 1] = \
				lista[i + 1], lista[i]	
				swapped = True
	return lista

print(bubbleSort(lista))

