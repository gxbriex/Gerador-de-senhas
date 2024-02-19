#importa o módulo random, que é utilizado para gerar números aleatorios
import random

print("Bem vindo ao gerador de senhas.")

#carateres utilizados para o gerador de senhas
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%#&*().,?0123456789"

#solicita ao usuario a quantidade de senhas que ele deseja
numero = input("Quantas senhas você deseja?: ")

#converte o valor inserido em um numero inteiro
numero = int(numero)

#solicita ao usuario quantos caracteres totais será gerado
comprimento = input("Quantos caractéres você deseja que a(s) sua(s) senha(s) tenham?")

#converte o valor inserido em um numero inteiro
comprimento = int(comprimento)

print("\nSua(s) senha(s) gerada(s):")
for pwd in range(numero): #inicio do loop
    senhas = '' #string vazia para que senha armazenada a senha
    for c in range (comprimento): #loop aninhado e 'c' será um indice de iteração
        senhas += random.choice(caracteres) #a
    print(senhas) #mostra a senha gerada
