
operacao = (input('Digite qual operação quer realizar(+, -, *, /)'))
    

numero1 = int(input('Digite o primeiro número'))
numero2 = int(input('Digite o segundo número'))

if operacao == '+':
    resultado = numero1 + numero2
    print(resultado)

elif operacao == '-':
    resultado = numero1 - numero2
    print(resultado)

elif operacao == '*':
    resultado = numero1 * numero2
    print(resultado)

elif operacao == '/':
    resultado = numero1 / numero2
    print(resultado)
else: 
    print('Operação inválida')    
