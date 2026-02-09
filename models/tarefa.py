from sqlite3 import Cursor
from models.database import Database
from typing import Self, Any, Optional

class Tarefa:
        def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str] = None, id_tarefa: Optional[int] = None) -> None:
                self.titulo_tarefa: Optional[str] = titulo_tarefa
                self.data_conclusao: Optional[str] = data_conclusao
                self.id_tarefa: Optional[int] = id_tarefa
                # Atrbutos que pertencem ao OBJETO.
        
        @classmethod
        def id(cls, id: int):
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = 'SELECT titulo_tarefa, data_conclusao FROM tarefas WHERE id = ?;'
                        params: tuple = (id,)
                        resultado = db.buscar_tudo(query, params)
                        # Desempacotamento de coleção
                        [[titulo, data]] = resultado
                return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data)
                # "cls" é usar a própria classe como parâmetro. O método ID retorna a própria classe, mas apenas com o ID.
                
        def salvar_tarefa(self: Self) -> None:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
                        params: tuple = (self.titulo_tarefa, self.data_conclusao)
                        db.executar(query, params)
                        # POST;

        @classmethod
        def obter_tarefas(cls) -> list[Self]:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "SELECT titulos_tarefa, data_conclusao FROM tarefas;"
                        resultados: list[Any] = db.buscar_tudo(query)
                        tarefas: list[Self] = [cls(titulo, data) for titulo, data in resultados]
                        return tarefas
                        # GET;

        def excluir_tarefa(self) -> Cursor:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = 'DELETE FROM tarefas WHERE id = ?;'
                        params: tuple = (self.id_tarefa,)
                        resultado = db.executar(query, params)
                        return resultado
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