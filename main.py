print('Olá mundo!')

nome = input('Qual seu nome? ')
print(nome)

print('=============== Desafio 03 =============')

primeiro = int(input('Digite um numero '))
segundo = int(input('Digite outro numero '))
valor = primeiro + segundo

print('A soma do numero {} com o numero {}, é: {}'.format(primeiro,segundo,valor))
#print('A soma do numero {0} com o numero {1}, é: {2}'.format(primeiro,segundo,valor))
print(type(segundo))

print('=============== Desafio 04 ===============')

a = input('Digite algo ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numérico? ', a.isnumeric())
print('É alfabético?', a.isalpha())
