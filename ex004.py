#Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ele.

n = (input('Digite algo: '))
print('O tipo primitivo dessa variável é:', type(n))
print('É um número? ', n.isnumeric())
print('É uma letra? ', n.isalpha())
print('É alfanúmerico? ', n.isalnum())
print('Está em maiúsculo? ', n.isupper())
print('Está em minúsculo? ', n.islower())
print('Está capitalizada?', n.istitle())
