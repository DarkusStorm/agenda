class Tarefa:

    lista_tarefas = []
    def __init__(self, titulo_tarefa, data_conclusao=None):
        self.titulo_tarefa = titulo_tarefa
        self.data_conclusao = data_conclusao
        # Atrbutos que pertencem ao OBJETO.
        Tarefa.lista_tarefas.append(self)

    def listar_tarefas(cls, titulo_tarefa):
        for tarefa in cls.lista_tarefas:
            if tarefa.titulo_tarefa == titulo_tarefa:
                print(tarefa.titulo_tarefa + ' - ' + tarefa.data_conclusao)