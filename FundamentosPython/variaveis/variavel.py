#Crie um programa que para ptricar o uso de variaveis com estrada e saída 
# de dados. Declare três variáveis, idade = 0, altura = 0.0 e nome = ""
# * peça para o usuário informar a idade, altura e nome de uma pessoa, e armazene
# nas respectivas variáveis, mantendo seus tipos de dados conforme o 
# estabelecido durante a declaração delas.
# * Ao final, os dados informados na tela.

idade = 0;
altura = 0.0; 
nome = "";

#Vamos já fazer a atribuição do tipo do dado pq cojitamos que o usuário vai informar os dados corretos.
print ("Solicitação de dados do usuário"); 
idade = int(input("Digite sua idade: "));
altura = float (input("Digite sua altura: "));
nome = input("Digite seu nome:");
# print ("Os dados do usuário são: ", idade, altura, nome);
print("A idade digitada foi:", idade);
print("A altura digitada foi:", altura);
print("O nome digitado foi:", nome);

