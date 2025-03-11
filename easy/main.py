# 1. Manipulação de Strings
# Crie um programa que receba uma string e retorne a versão invertida dela.

def start_solution():
    text_reverse = ""
    message = input("Digite o texto: ")
    for index in range(len(message)):
        text_reverse += message[-(index + 1)]

    print(text_reverse)

def end_solution():
    message = input("Digite o texto: ")

    # Inverte a string utilizando slicing:
    # message[início:fim:passo]
    # - início (vazio) → começa do primeiro caractere
    # - fim (vazio) → vai até o último caractere
    # - passo (-1) → percorre a string de trás para frente, invertendo a ordem dos caracteres
    print(message[::-1])

# 2. Listas e Tuplas
# Crie uma função que receba uma lista de números e retorne a média aritmética.

def get_media(numbers):
    total = sum(numbers)
    return total / len(numbers)

numbers = [10, 20, 30, 40, 50]
media = get_media(numbers)
print(f"Sua média é {media:.2f}")

# 3. Dicionários
# Crie um dicionário que armazene nomes de usuários e idades. Permita buscar a idade de um usuário pelo nome.
def get_age(name):
    users = {
        "ailson": 23,
        "pedro": 17
    }
    return str(users.get(name, f"not found for {name}"))

print("result age: " + get_age("pedro"))
print("result age: " + get_age("mateus"))

# 4. Laços de Repetição (FizzBuzz)
# Escreva um programa que imprima os números de 1 a 100, substituindo múltiplos de 3 por "Fizz" e múltiplos de 5 por "Buzz". Para múltiplos de ambos, imprima "FizzBuzz".
def print_values():
    for index in range(1, 101):

        is_multiple_of_three = index % 3 == 0
        is_multiple_of_five = index % 5 == 0

        if is_multiple_of_three and is_multiple_of_five:
            print("FizzBuzz")
        elif is_multiple_of_three:
            print("Fizz")
        elif is_multiple_of_five:
            print("Buzz")
        else:
            print(index)

# print_values()

# 5. Leitura e Escrita de Arquivos
# Crie um programa que leia um arquivo de texto e conte quantas palavras existem nele.
file = open('users.txt')
content_file = file.read()
print(len(content_file.split(',')))
file.close()


# 6. Tratamento de Exceções (Divisão por Zero)
# Crie um programa que receba dois números do usuário e realize a divisão, tratando erros como divisão por zero.

def start_solution_6():
    def subtract(value1, value2):
        if value2 == 0: return None
        return value1 / value2

    print(f'Divisão: {subtract(0, 2)}')

def end_solution_6():
    def subtract(value1, value2):
        try:
            result = value1 / value2
            return f"O resultado da divisão é: {result:.2f}"
        except ZeroDivisionError:
            return "Erro: Divisão por zero não é permitida."
        except TypeError:
            return "Erro: Insira apenas números válidos."

    try:
        num1 = float(input("Digite o numerador: "))
        num2 = float(input("Digite o divisor: "))
        print(subtract(num1, num2))
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")

end_solution_6()

