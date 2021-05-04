# """ Estruturas de Repetição """

number = input("Digite um número de 1 a 9: ")
name = input("Digite um nome:")

for i in range(10):
 if(i ==  int(number)):

  print(f"{i} - Seu nome é:  {name}")

 else:

  print(f"{i}- Não encontramos seu nome")

j = 0
while(j<=2):

  print("...Script sendo executado...")
  j = j + 1