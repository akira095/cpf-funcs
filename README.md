# Validação

A validação de um CPF é feita por um algoritmo que calcula a soma de verificação dos nove primeiros dígitos e a compara com os dois últimos dígitos. Considerando a estrutura do CPF como "ABC-DEF-GHI-JK":
- "A-H" são números gerados aleatoriamente;
- "I" é o dígito que indica a região onde o CPF foi cadastrado;
- "J" e "K" são os dígitos de verificação que precisamos validar.
    
A primeira parte da validação consiste em calcular 10*a + 9*b + 8*c + 7*d + 6*e + 5*f + 4*g + 3*h + 2*i, multiplicar a soma por 10 e dividir o resultado por 11.
    
O que precisamos é do resto da divisão, que deve ser igual ao primeiro dígito verificador do CPF, no nosso exemplo, "J". Sendo igual, a primeira parte foi validada.

Na segunda parte da validação, incluímos o primeiro dígito que validamos anteriormente. Assim, calculamos 11*a + 10*b + 9*c + 8*d + 7*e + 6*f + 5*g + 4*h + 3*i + 2*j, multiplicamos a soma por 10 e dividimos o resultado por 11.
    
Novamente, precisamos comparar o resto da divisão com o segundo dígito verificador do CPF, no nosso exemplo, "K". Sendo igual, terminamos a validação do CPF.

<b>Notas:</b>
- Se o resto da divisão por 11 for 10, consideramos como 0.
- CPFs que contém todos os números iguais, como 111.111.111-11, são inválidos, embora passem na validação dos dígitos.

# Validation

The validation of a CPF number is made by an algorithm that calculates the checksum of the first nine digits and compares it with the last two digits. Considering the following CPF structure ABC.DEF.GHI-JK:
- "A-H" are random generated numbers;
- "I" it's the digit that indicates the fiscal state the CPF was registrated;
- "J" and "K" are the checksum digits we need to valuate.

The first part of the validation consists in calculating 10*a + 9*b + 8*c + 7*d + 6*e + 5*f + 4*g + 3*h + 2*i, multiplying the sum by 10 and then dividing the result by 11.

What we need it's the remainder of the division, that must be equal to the first checksum digit of the CPF, i.e. "J" in our example. If it is, then the first part is done.

In the second part of the validation we include the first checksum digit we evaluated before. So we calculate 11*a + 10*b + 9*c + 8*d + 7*e + 6*f + 5*g + 4*h + 3*i + 2*j, multiply the sum by 10 and divide by 11.
    
Again, we take the remainder of the division and check if it's equal to the second checksum digit of the CPF, i.e. "K" in our example. If it is, then the validation is done.
   
<b>Notes:</b>
- If the remainder of the division by 11 it's 10, we consider it as 0.
- CPF sequences where all numbers are equal, eg. 111.111.111-11, are invalid, though they pass the validation of the checksum digits.