from tarefa_enum import Status

class Tarefa:

    contador_id = 1

    def __init__(self, descricao, prazo):
        self.id = Tarefa.contador_id
        self.descricao = descricao
        self.prazo = prazo
        self.status = Status.PENDENTE
        Tarefa.contador_id += 1

    def __str__(self):
        return f"Tarefa: ID: {self.id} | DESCRICAO: {self.descricao} | PRAZO: {self.prazo} | STATUS: {self.status.value}"