from random import randint

fiscalCodes = {
    1: ('DF', 'GO', 'MT', 'MS', 'TO'),
    2: ('AC', 'AP', 'AM', 'PA', 'RO', 'RR'),
    3: ('CE', 'MA', 'PI'),
    4: ('AL', 'PB', 'PE', 'RN'),
    5: ('BA', 'SE'),
    6: 'MG',
    7: ('ES', 'RJ'),
    8: 'SP',
    9: ('PR', 'SC'),
    0: 'RS'
}

def validate(sequence, state=False):
    #  Get numbers from CPF sequence; ignore other characters
    cpf = [int(char) for char in sequence if char.isdigit()]

    #  Check if it has 11 digits
    if len(cpf) != 11:
        return False

    #  Check if all numbers are equal, e.g. '111.111.111-11'
    #  These CPFs sequences are invalid, though they pass the checksum validations
    #  Old line for reference: if all(cpf[i] == cpf[i+1] for i in range(0, len(cpf)-1)
    if cpf == cpf[::-1]:
        return False
    
    #  Validate checksum digits
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return 'CPF inválido.'
    
    #  Get state of origin
    if state:
        code = cpf[8]
        print(f'Região fiscal: {", ".join(fiscalCodes[code])}')

    return 'CPF válido.'

def gen(originState=None):
    #  Generate the first digits (and make sure they're not all equal)
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
                break
    
    #  User can inform the state of origin by typing the state abbreviation.
    #  If the input is not valid, the program will just generate a random CPF.
    if originState is not None:
        if originState.isalpha and len(originState) == 2:
            for k, v in fiscalCodes.items():
                if originState in v:
                    cpf[8] = k

    #  Generate the checksum digits
    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    #  Return CPF as string
    result = ''.join(map(str, cpf))
    return result

#  Validador: validate('79225304390')
#  Para mostrar a região fiscal do CPF, se válido, use state=True no comando anterior.
#  Gerador: gen()
#  Para gerar um CPF de um determinado estado, informe a sigla entre os parênteses, ex.: gen('CE')