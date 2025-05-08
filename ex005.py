# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

x = int(input('Digite um número inteiro: '))
print('O antecessor de {} é {} e o sucessor é {}'.format(x, (x-1), (x+1)))