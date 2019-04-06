
lista_usuarios = []

for n in range(10):
	usuario = {
		'nome': input('Digite seu nome'),
		'idade': input('Digite sua idade'),
		'email': input('Digite seu email'),
	
	}
	
	lista_usuarios.append(usuario)


for usuario in lista_usuarios:
	print(usuario['nome'])

exit()











lista_populada = [1,2,3,4,5,6,7,8,9,10]
lista_vazia = []

lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)
lista_vazia.append(4)
lista_vazia.append(5)
lista_vazia.append(6)
lista_vazia.append(7)
lista_vazia.append(8)
lista_vazia.append(9)
lista_vazia.append(10)

print(lista_vazia[4])

print(lista_populada)
print(lista_vazia)

for n in lista_vazia:
	print('Imprimindo o numero' + str(n))






