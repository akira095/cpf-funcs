from src import validate, gen

option = int(input('1 - Validar CPF\n'
		   '2 - Gerar CPF válido\n'
		   '>>> '))
	
if option == 1:
    number = input('Digite o CPF: ').strip()
    if validate(number):
        print('CPF válido.')
    else:
        print('CPF inválido.')

elif option == 2:
    cpf = gen()
    print(f'CPF gerado automaticamente: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
    
else:
    print('Inválido.')
