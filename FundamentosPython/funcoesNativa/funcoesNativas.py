# exemplo de funcionamento de todas as funções nativas que foram passadas no curso.

# abs(): Retorna o valor absoluto (positivo) de um número
numero_negativo = -15
print("abs():", abs(numero_negativo))

# all(): Retorna True se todos os elementos de um iterável forem verdadeiros
elementos_true = [True, 1, "texto"]
print("all():", all(elementos_true))

# any(): Retorna True se pelo menos um elemento de um iterável for verdadeiro
elementos_misto = [False, 0, True]
print("any():", any(elementos_misto))

# bool(): Converte um valor em um booleano (True ou False)
print("bool():", bool(10))

# callable(): Verifica se um objeto pode ser chamado como uma função
print("callable():", callable(print))

# chr(): Retorna o caractere correspondente a um código Unicode específico
print("chr():", chr(65))  # Retorna 'A'

# dir(): Lista os atributos e métodos disponíveis de um objeto
print("dir():", dir([])[:3])  # Mostra os 3 primeiros métodos de uma lista

# enumerate(): Adiciona um contador a um iterável, retornando pares de índice e valor
for indice, valor in enumerate(["a", "b", "c"]):
  print(f"enumerate() -> Índice: {indice}, Valor: {valor}")
  break  # Apenas para o exemplo não ficar longo

# eval(): Avalia e executa uma expressão em formato de string matemática
print("eval():", eval("5 + 5 * 2"))

# exec(): Executa dinamicamente um bloco de código Python passado como string
exec('print("exec(): Olá executado via string!")')

# filter(): Filtra elementos de um iterável onde uma função retorna verdadeiro
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("filter():", pares)

# float(): Converte um valor para um número de ponto flutuante (decimal)
print("float():", float(7))

# globals(): Retorna um dicionário com as variáveis globais do escopo atual
print("globals(): Contém", len(globals()), "itens globais.")

# help(): Invoca o sistema de ajuda interativo (aqui chamamos a string de ajuda de um objeto)
print("help() (resumo):", type(help(int)))

# id(): Retorna o identificador único (espaço na memória) de um objeto
variavel_exemplo = 42
print("id():", id(variavel_exemplo))

# input(): Lê uma string digitada pelo usuário via terminal (comentado para não travar a execução automática)
# nome_usuario = input("input() - Digite seu nome: ")

# isinstance(): Verifica se um objeto é uma instância de uma classe específica
print("isinstance():", isinstance(10, int))

# int(): Converte um valor para um número inteiro
print("int():", int(5.99))

# len(): Retorna o tamanho (número de itens) de um objeto ou coleção
print("len():", len([10, 20, 30, 40]))

# locals(): Retorna um dicionário com as variáveis locais do escopo atual
print("locals():", locals() is not None)

# map(): Aplica uma função a cada item de um iterável
dobro = list(map(lambda x: x * 2, [1, 2, 3]))
print("map():", dobro)

# max(): Retorna o maior valor de um iterável ou entre argumentos
print("max():", max([4, 9, 2, 7]))

# min(): Retorna o menor valor de um iterável ou entre argumentos
print("min():", min([4, 9, 2, 7]))

# open(): Abre um arquivo e retorna um objeto de arquivo (criando um arquivo de teste rápido)
with open("teste_exemplo.txt", "w") as arquivo:
  arquivo.write("Testando a função open()")
print("open(): Arquivo criado e escrito com sucesso.")

# print(): Exibe mensagens ou objetos formatados no console
print("print(): Olá, Jhon o Magnífico!")

# range(): Gera uma sequência de números com base em um intervalo
print("range():", list(range(0, 5)))

# sorted(): Retorna uma nova lista ordenada com os elementos de um iterável
print("sorted():", sorted([5, 1, 3, 8]))

# str(): Converte um valor em uma string (texto)
print("str():", str(123) + "456")

# sum(): Retorna a soma dos elementos de um iterável
print("sum():", sum([10, 20, 30]))

# type(): Retorna o tipo de dado de um objeto
print("type():", type(3.14))

# zip(): Combina múltiplos iteráveis em tuplas correspondentes
nomes = ["Ana", "Bruno"]
idades = [20, 25]
print("zip():", list(zip(nomes, idades)))

# Limpando o arquivo temporário criado no exemplo do 'open()'
import os

os.remove("teste_exemplo.txt")


