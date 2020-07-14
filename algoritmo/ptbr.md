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

# Estado de origem do CPF

O último dígito anterior aos dois dígitos verificadores identifica a região fiscal do Brasil onde o CPF foi cadastrada:
- 1 - Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins
- 2 - Pará, Amazonas, Acre, Amapá, Rondônia e Roraima
- 3 - Ceará, Maranhão e Piauí
- 4 - Pernambuco, Rio Grande do Norte, Paraíba e Alagoas
- 5 - Bahia e Sergipe
- 6 - Minas Gerais
- 7 - Rio de Janeiro e Espírito Santo
- 8 - São Paulo
- 9 - Paraná e Santa Catarina
- 0 - Rio Grande do Sul
