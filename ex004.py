#Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ele.

n = int(input('Digite algo: '))
print(type(n))
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isupper())
print(n.islower())
