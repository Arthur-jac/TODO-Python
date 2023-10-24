from tarefa_controller import *

def menu():
    try:
        print("TODO")
        print("0 - SAIR")
        print("1 - CADASTRAR TAREFA")
        print("2 - LISTAR TAREFAS")
        print("3 - ATUALIZAR TAREFA")
        print("4 - DELETAR TAREFA")
        op = int(input("Digite a sua opção: "))
        return op
    except ValueError:
        print("Digite apenas números")


def opcoes():
    try:
        rodar = True
        while rodar:
            op = menu()

            if op == 0:
                print("Programa encerrado")
                rodar = False
            elif op == 1:
                cadastrar_tarefa()
            elif op == 2:
                listar_tarefas()
            elif op == 3:
                atualizar_status()
            elif op == 4:
                deletar_tarefa()
            else:
                print("Opção inválida")
    except (ValueError, KeyboardInterrupt, EOFError) as er:
        print("Erro ao rodar a aplicação", er)