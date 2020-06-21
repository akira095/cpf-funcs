from random import randint


def validate(seq):
 
	#  Get numbers from sequence and ignore other characters
	cpf = [int(char) for char in seq if char.isdigit()]

	#  Check if CPF sequence has 11 digits
	if len(cpf) != 11:
		return False

	#  Check if all numbers on sequence are equal, ex.: 111.111.111-11
	if cpf == cpf[::-1]:
		return False

	#  Validate the checksum digits
	for i in range(9, 11):
		value = sum(cpf[num] * ((i + 1) - num) for num in range(0, i))
		digit = ((value * 10) % 11) % 10
		if digit != cpf[i]:
			return False
	return True


def gen():
	#  Generate the first nine digits (and make sure they're not equal)
	while True:
		cpf = [randint(0, 9) for _ in range(9)]
		if cpf != cpf[::-1]:
			break

	#  Generate the checksum digits
	for i in range(9, 11):
		value = sum(cpf[num] * ((i + 1) - num) for num in range(0, i))
		digit = ((value * 10) % 11) % 10
		cpf.append(digit)

	result = ''.join(map(str, cpf))
	return result


if __name__ == '__main__':
	
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
