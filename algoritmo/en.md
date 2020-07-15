# Validation

The validation of a CPF number is made by an algorithm that calculates the checksum of the first nine digits and compares it with the last two digits. Considering the following CPF structure ABC.DEF.GHI-JK:
- "A-H" are random generated numbers;
- "I" it's the digit that indicates the fiscal state the CPF was registered;
- "J" and "K" are the checksum digits we need to valuate.

The first part of the validation consists in calculating 10*a + 9*b + 8*c + 7*d + 6*e + 5*f + 4*g + 3*h + 2*i, multiplying the sum by 10 and then dividing the result by 11.

What we need it's the remainder of the division, that must be equal to the first checksum digit of the CPF, i.e. "J" in our example. If it is, then the first part is done.

In the second part of the validation we include the first checksum digit we evaluated before. So we calculate 11*a + 10*b + 9*c + 8*d + 7*e + 6*f + 5*g + 4*h + 3*i + 2*j, multiply the sum by 10 and divide by 11.
    
Again, we take the remainder of the division and check if it's equal to the second checksum digit of the CPF, i.e. "K" in our example. If it is, then the validation is done.
   
<b>Notes:</b>
- If the remainder of the division by 11 it's 10, we consider it as 0.
- CPF sequences where all numbers are equal, eg. 111.111.111-11, are invalid, though they pass the validation of the checksum digits.

# State of origin

The last digit before the checksum digits identifies the Brazilian fiscal state where the CPF was registered:
- 1 - Distrito Federal, Goiás, Mato Grosso do Sul and Tocantins
- 2 - Pará, Amazonas, Acre, Amapá, Rondônia and Roraima
- 3 - Ceará, Maranhão and Piauí
- 4 - Pernambuco, Rio Grande do Norte, Paraíba and Alagoas
- 5 - Bahia and Sergipe
- 6 - Minas Gerais
- 7 - Rio de Janeiro and Espírito Santo
- 8 - São Paulo
- 9 - Paraná and Santa Catarina
- 0 - Rio Grande do Sul
