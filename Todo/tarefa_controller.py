from datetime import datetime
from tarefa_model import Tarefa
from tarefa_enum import Status

tarefas = []

def procurar_tarefa(id):
    for t in tarefas:
        if t.id == id:
            print("Tarefa encontrada!")
            return t
    return None
    

def cadastrar_tarefa():
    try:
        print("CADASTRO DE TAREFA")
        descricao = input("Digite a descricao da tarefa: ")
        prazo_string = input("Digite o prazo no formato: 'dia/mês/ano': ")
        prazo = datetime.strptime(prazo_string, "%d/%m/%Y") 
        tarefa = Tarefa(descricao, prazo)
        tarefas.append(tarefa)
        print("Tarefa cadastrada com sucesso!")
    except ValueError as erro:
        print("Erro ao ler data:", erro)
    except:
        print("Erro ao cadastrar tarefa")

def atualizar_status():
    try:
        if tarefas:
            print("ATUALIZAR STATUS")
            id = int(input("Digite o ID  da tarefa para atualizar: "))
            tarefa = procurar_tarefa(id)
            if tarefa is not None:
                status_string = input("Digite o status da tarefa para atualizar [PENDENTE, PRONTO, FAZENDO]:")
                formatada = status_string.upper()
                if formatada in [status.value for status in Status]:
                    tarefa.status = Status[formatada]
                    print(tarefa)
                else:
                    print("Digite apenas status presentes")
            else:
                print("Tarefa inexistente")
        else:
            print("A lista está vazia")
    except ValueError as er:
        print("Erro ao atualizar tarefa", er)
    except:
        print("Erro ao atualizar tarefa")

def deletar_tarefa():
    try:
        if tarefas:
            print("DELETAR TAREFA")
            id = int(input("Digite o id da tarefa: "))
            tarefa = procurar_tarefa(id)
            if tarefa is not None:
                tarefas.remove(tarefa)
                print("Tarefa deletada com sucesso")
            else:
                print("Tarfa inexistente")
        else:
            print("A lista de tarefas está vazia")
    except ValueError as er:
        print("Digite no id apenas um número inteiro!")

def listar_tarefas():
    try:
        if tarefas:
            print("Listando as tarefas")
            for tarefa in tarefas:
                print(tarefa)
        else:
            print("A lista está vazia")
    except:
        print("Erro ao listar as tarefas!")