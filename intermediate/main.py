import json
import re
import requests
import time
import threading

# 1. Programação Orientada a Objetos (POO)
# Implemente uma classe Carro com atributos como marca, modelo e ano, e métodos para acelerar e frear.
class Car:
    def __init__(self, model, year, brand, maximum_speed):
        self.__model = model
        self.__year = year
        self.__brand = brand
        self.__speed = 0
        self.__maximum_speed = maximum_speed

    def get_speed(self):
        return self.__speed

    def break_speed(self):
        # """ => gera uma documentação
        """Reduz a velocidade em 20 km/h, sem permitir valores negativos."""
        self.__speed = max(0, self.__speed - 20)

    def accelerate_speed(self):
        """Aumenta a velocidade em 20 km/h, respeitando o limite máximo."""
        self.__speed = min(self.__speed, self.__speed + 20)

big_car = Car('Civic', 2020, 'Honda', 150)
big_car.accelerate_speed()
big_car.accelerate_speed()

big_car.break_speed()

print(f"Velocidade {big_car.get_speed()}")

# 2. Geradores e Iteradores
# Crie um gerador que forneça os números da sequência de Fibonacci até um determinado número.

def start_solution_2():
    def generate_fibonacci(max_value):
        result_fibonaci = []
        index = 0
        searched = False
        while not searched:
            if index == 0 or index == 1:
                result_fibonaci.append(1)
            else:
                last_two_values = result_fibonaci[index - 2:index]
                new_value = sum(last_two_values)
                if new_value >= max_value:
                    searched = True
                    break

                result_fibonaci.append(new_value)
            index += 1

        return result_fibonaci

    print(generate_fibonacci(100))

def end_solution_2():
    def generate_fibonacci(max_value):
        """Gera a sequência de Fibonacci até um valor máximo."""
        result_fibonacci = [1, 1]  # Começa com os dois primeiros valores

        while True:
            new_value = result_fibonacci[-1] + result_fibonacci[-2]  # Soma os dois últimos valores
            if new_value >= max_value:
                break
            result_fibonacci.append(new_value)

        return result_fibonacci

    print(generate_fibonacci(100))

start_solution_2()
end_solution_2()

# 3. Expressões Regulares
# Desenvolva um validador de e-mails utilizando a biblioteca re.

def check_email(email):
    # r Evita que a barra invertida (\) seja tratada como caractere de escape
    regex = r'\b[A-Za-z0-9._%*-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

    isValid = re.fullmatch(regex, email)
    print('e-mail valido' if isValid else 'e-mail inválido')

check_email('ailson@dev.com')

# 4. Manipulação de JSON
# Escreva um programa que leia um arquivo JSON contendo informações de produtos
# e exiba os produtos com preço acima de um determinado valor.

# o uso de with garante que o arquivo vai ser fechado após o script ser executado
with open('products.json') as products:
    products_parsed = json.load(products)

    for product in products_parsed:
        if product['value'] > 1000:
            print(f'Product "{product["name"]}" enable')


# 5. Requests e Consumo de APIs
# Utilize requests para consumir uma API pública e exibir dados formatados.

def get_address_by_cep(cep):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json')
        data = response.json()

        print(f'Endereço: {data['logradouro']}, {data['bairro']}, {data['localidade']}-{data['uf']}')
    except Exception as error:
        print(f'Endereço não encontrado para o cep {cep}')
        print(f'Error: {error}')

get_address_by_cep('69086001')
get_address_by_cep('xxxxxxxx')


# 6. Threads e Multiprocessamento
# Implemente um programa que execute duas tarefas simultaneamente
# usando threading ou multiprocessing.

# Threads (threading): Permitem que um programa execute várias tarefas ao mesmo tempo dentro do mesmo processo. Elas compartilham a mesma memória, o que pode levar a concorrência de recursos.
# Ideal para tarefas I/O-bound (exemplo: baixar arquivos da internet, ler um banco de dados, esperar por respostas de uma API).
# Multiprocessamento (multiprocessing): Permite executar múltiplos processos independentes, cada um com sua própria memória.
# Ideal para tarefas CPU-bound (exemplo: cálculos matemáticos pesados, processamento de imagens).

def contar_ate_5():
    for i in range(1, 6):
        print(f"Contagem: {i}")
        time.sleep(1)

def mostrar_mensagem():
    for _ in range(5):
        print("Executando outra tarefa simultânea...")
        time.sleep(1)

#Criando as threads
thread1 = threading.Thread(target=contar_ate_5)
thread2 = threading.Thread(target=mostrar_mensagem)

#Iniciando as threads
thread1.start()
thread2.start()

#Esperando as threads terminarem
thread1.join()
thread2.join()

print("Thread finalizado!")


# 7. Decorators
# Crie um decorator que meça o tempo de execução de uma função.
def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Marca o tempo inicial
        func(*args, **kwargs)  # Executa a função original
        fim = time.time()  # Marca o tempo final
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
    return wrapper  # Retorna a função modificada


@medir_tempo
def carregar_dados():
    print("Carregando dados...")
    time.sleep(2)  # Simula um processamento demorado
    print("Dados carregados!")


carregar_dados()