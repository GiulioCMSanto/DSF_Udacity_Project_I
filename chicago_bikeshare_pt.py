#Giulio Cesare Mastrocinque Santo
#Project I
# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

#Definição das Funções Criadas

def column_to_list(data, index):
    """
      Cria uma lista de colunas a partir de uma lista de listas.
      Argumentos:
          param1: uma lista de listas.
          param2: O índice das colunas que serão transformadas em uma lista.
      Retorna:
          Uma lista de colunas.
      """
    column_list = []
    for line in range(len(data)):
        column_list.append(data[line][index])
    return column_list

def count_gender(data_list):
    """
    Retorna uma Lista com o Número de Gênros Masculino e Feminino no formato
    [count_male, count_female].
    Argumentos:
        param1: uma lista de dados.
    Retorna:
        Uma lista com o número de cada gênero.
    """
    male = 0
    female = 0
    for column in column_to_list(data_list,-2):
        if column == 'Male':
            male += 1
        elif column == 'Female':
            female += 1
    return [male, female]

def most_popular_gender(data_list):
    """
    Retorna o gênero mais popular, ou seja, aquele que tem maior moda.
    Argumentos:
        param1: uma lista de dados.
    Retorna:
        "Masculino", "Feminino" ou "Igual" dependendo de qual for mais frequente.
    """

    if count_gender(data_list)[0] > count_gender(data_list)[1]:
        answer = "Masculino"
    elif count_gender(data_list)[0] == count_gender(data_list)[1]:
        answer = "Igual"
    else:
        answer = "Feminino"

    return answer

def count_user_types(data_list):
    """
    Retorna uma lista com o número de User_Types no seguinte formato:
    [count_subscriber,count_customer, count_dependent].
    Arguments:
        param1: uma lista de dados.
    Retorna:
        Uma lista com o número de Cada User Type(Subscriber, Customer e Dependent).
    """
    subscriber = 0
    customer = 0
    dependent = 0
    for column in column_to_list(data_list, -3):
        if column == "Subscriber":
            subscriber += 1
        elif column == "Customer":
            customer += 1
        else:
            dependent += 1

    return [subscriber, customer, dependent]

def max_value(data_list):
    """
    Calcula o valor maximo de uma lista - o mesmo que max()
    """
    auxiliar = 0
    for data in data_list:
        if(float(data) >= auxiliar):
            auxiliar = float(data)
    return auxiliar

def min_value(data_list):
    """
    Calcula o valor mínimo de uma lista - o mesmo que min()
    """
    auxiliar = float(data_list[0])
    for data in data_list:
        if(float(data) <= auxiliar):
            auxiliar = float(data)
    return auxiliar

def mean_value(data_list):
    """
    Calcula a média dos valores de uma lista - o mesmo que mean()
    """
    auxiliar = 0
    for data in data_list:
        auxiliar += float(data)/len(data_list)
    return auxiliar


def median_value(data_list):
    """
    Calcula a mediana de uma lista - o mesmo que median(). Não modifica a entrada.
    Argumentos:
        param1: uma lista de dados.
    Retorna:
        O valor da mediana da lista.
    """
    auxiliar = 0
    is_even = lambda x: len(x)%2 == 0

    if(is_even(data_list)):
        auxiliar = (float(sorted(data_list, key=int)[int(len(data_list)/2)]) \
        + float(sorted(data_list, key=int)[int(len(data_list)/2 + 1)]))/2
    else:
        auxiliar = float(sorted(data_list, key=int)[int((len(data_list) + 1)/2)])

    return auxiliar

def count_items(column_list):
    """
    Conta a ocorrência de qualquer coluna, sem necessidade de especificação.
    Argumentos:
        param1: uma lista de colunas.
    Retorna:
        Duas listas: uma lista contendo todos os tipos de ocorrência desta lista
        e outra contendo quantos elementos existem em cada tipo.
    """
    item_types = list(set(column_list))
    count_items = [column_list.count(item_type) for item_type in item_types]
    return item_types, count_items

#Executáveis
def main():
    # Vamos ler os dados como uma lista
    print("Lendo o documento...")
    with open("chicago.csv", "r") as file_read:
        reader = csv.reader(file_read)
        data_list = list(reader)
    print("Ok!")

    # Vamos verificar quantas linhas nós temos
    print("Número de linhas:")
    print(len(data_list))

    # Imprimindo a primeira linha de data_list para verificar se funcionou.
    print("Linha 0: ")
    print(data_list[0])
    # É o cabeçalho dos dados, para que possamos identificar as colunas.

    # Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
    print("Linha 1: ")
    print(data_list[1])

    input("Aperte Enter para continuar...")
    # TAREFA 1
    # TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.

    print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
    for line in range(20):
        print(data_list[line])

    # Vamos mudar o data_list para remover o cabeçalho dele.
    data_list = data_list[1:]

    # Nós podemos acessar as features pelo índice
    # Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

    input("Aperte Enter para continuar...")
    # TAREFA 2
    # TODO: Imprima o `gênero` das primeiras 20 linhas

    print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
    for line in range(20):
        print(data_list[line][6])

    # Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
    # Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

    input("Aperte Enter para continuar...")
    # TAREFA 3
    # TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem


    # Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
    print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
    print(column_to_list(data_list, -2)[:20])

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
    assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
    assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
    # -----------------------------------------------------

    input("Aperte Enter para continuar...")
    # Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
    # TAREFA 4
    # TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
    male = 0
    female = 0
    for column in column_to_list(data_list,-2):
        if column == 'Male':
            male += 1
        elif column == 'Female':
            female += 1


    # Verificando o resultado
    print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
    print("Masculinos: ", male, "\nFemininos: ", female)

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
    # -----------------------------------------------------

    input("Aperte Enter para continuar...")
    # Por que nós não criamos uma função parTODO isso?
    # TAREFA 5
    # TODO: Crie uma função para contar os gêneros. Retorne uma lista.
    # Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

    print("\nTAREFA 5: Imprimindo o resultado de count_gender")
    print(count_gender(data_list))

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
    assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
    assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
    # -----------------------------------------------------

    input("Aperte Enter para continuar...")
    # Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
    # TAREFA 6
    # TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
    # Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.


    print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
    print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
    assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
    # -----------------------------------------------------

    # Se tudo está rodando como esperado, verifique este gráfico!
    types = ["Male", "Female"]
    quantity = count_gender(data_list)
    y_pos = list(range(len(types)))
    plt.bar(y_pos, quantity)
    plt.ylabel('Quantidade')
    plt.xlabel('Gênero')
    plt.xticks(y_pos, types)
    plt.title('Quantidade por Gênero')
    plt.show(block=True)

    input("Aperte Enter para continuar...")
    # TAREFA 7
    # TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

    #Vide função criada

    print("\nTAREFA 7: Verifique o gráfico!")
    types = ["Subscriber", "Customer", "Dependent"]
    quantity = count_user_types(data_list)
    y_pos = list(range(len(types)))
    plt.bar(y_pos, quantity)
    plt.ylabel('Quantidade')
    plt.xlabel('Tipo de Usuários')
    plt.xticks(y_pos, types)
    plt.title('Quantidade por Tipo de Usuários')
    plt.show(block=True)


    input("Aperte Enter para continuar...")
    # TAREFA 8
    # TODO: Responda a seguinte questão
    male, female = count_gender(data_list)
    print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
    print("male + female == len(data_list):", male + female == len(data_list))
    answer = ("A condição é Falsa porque temos {} elementos vazios na coluna gênero "
              "além dos {} gêneros Masculino "
              "e Feminino na lista de dados.").format(len(data_list) - (male + female),male + female)
    print("resposta:", answer)

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
    # -----------------------------------------------------

    input("Aperte Enter para continuar...")
    # Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
    # TAREFA 9
    # TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
    # Você não deve usar funções prontas parTODO isso, como max() e min().
    trip_duration_list = column_to_list(data_list, 2)

    # As funções abaixo foram criadas no início do código. Favor verificar.

    min_trip = min_value(trip_duration_list)
    max_trip = max_value(trip_duration_list)
    mean_trip = mean_value(trip_duration_list)
    median_trip = median_value(trip_duration_list)

    print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
    print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
    assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
    assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
    assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
    # -----------------------------------------------------

    input("Aperte Enter para continuar...")
    # TAREFA 10
    # Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
    # TODO: Verifique quantos tipos de start_stations nós temos, usando set()
    user_types = set(column_to_list(data_list,3))

    print("\nTAREFA 10: Imprimindo as start stations:")
    print(len(user_types))
    print(user_types)

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
    # -----------------------------------------------------

    input("Aperte Enter para continuar...")
    # TAREFA 11
    # Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
    # def new_function(param1: int, param2: str) -> list:
    #    """
    #      Função de exemplo com anotações.
    #      Argumentos:
    #          param1: O primeiro parâmetro.
    #          param2: O segundo parâmetro.
    #      Retorna:
    #          Uma lista de valores x.
    #      """

    input("Aperte Enter para continuar...")
    # TAREFA 12 - Desafio! (Opcional)
    # TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
    # para que nós possamos usar essa função com outra categoria de dados.
    answer = input("Você vai encarar o desafio? (yes ou no): ")

    #A função foi criada no início do código. Favor verificar.

    if answer == "yes":
        # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
        column_list = column_to_list(data_list, -2)
        types, counts = count_items(column_list)
        print("\nTAREFA 11: Imprimindo resultados para count_items()")
        print("Tipos:", types, "Counts:", counts)
        assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
        assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
        # -----------------------------------------------------
if __name__ == "__main__":
    main()
