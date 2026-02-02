from models.database import Database
from typing import Self

class Tarefa:
        def __init__(self: Self, titulo_tarefa: str, data_conclusao: str =None) -> None:
                self.titulo_tarefa: str = titulo_tarefa
                self.data_conclusao: str = data_conclusao
                # Atrbutos que pertencem ao OBJETO.

        def salvar_tarefa(self: Self) -> None:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
                        params: tuple = (self.titulo_tarefa, self.data_conclusao)
                        db.executar(query, params)

# class Tarefa:

#     lista_tarefas = []
#     def __init__(self, titulo_tarefa: str, data_conclusao: str =None) -> None:
#         self.titulo_tarefa: str = titulo_tarefa
#         self.data_conclusao: str = data_conclusao
#         # Atrbutos que pertencem ao OBJETO.
#         self.lista_tarefas.append(self)

#     def listar_tarefas(cls, titulo_tarefa):
#         for tarefa in cls.lista_tarefas:
#             if tarefa.titulo_tarefa == titulo_tarefa:
#                 print(tarefa.titulo_tarefa + ' - ' + tarefa.data_conclusao)