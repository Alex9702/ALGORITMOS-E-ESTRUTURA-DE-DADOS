lista = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

def mergeSort(lista):
	print('Splitting ', lista)
	if len(lista) > 1:
		mid = len(lista)//2
		lefthalf = lista[:mid]
		righthalf = lista[mid:]

		# recursivo
		mergeSort(lefthalf)
		mergeSort(righthalf)

		i, j, k = 0, 0, 0

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				lista[k] = lefthalf[i]
				i += 1
			else:
				lista[k] = righthalf[j]
				j += 1
			k += 1

		while i < len(lefthalf):
			lista[k] = lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf):
			lista[k] = righthalf[j]
			j += 1
			k += 1
	print('Merging ', lista)


mergeSort(lista)
print(lista)
