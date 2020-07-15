## Uso
Para validar números de CPF, use o validate(). Você pode adicionar o argumento state=True para mostrar também a região fiscal onde o número foi validado.

A função gen() irá gerar um número de CPF válido aleatório. Para gerar um CPF de um determinado estado, informe a sigla dentro dos parênteses.

        > from cpf import validate, gen
        > validate('79225304390')
        > validate('79225304390', state=True)
        > gen()
        > gen('CE')

        #  Output
        > True
        > Região fiscal: CE, MA, PI
        True
        > '40422942600'
        > '66663338374'


## Aviso
Este programa foi criado com o intuito de testar softwares e outras aplicações, e os dados aqui gerados são aleatórios e não têm a intenção de representar pessoas reais. A má utilização deste programa é de total responsabilidade do usuário.