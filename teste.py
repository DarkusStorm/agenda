# from random import randint
# from pprint import pprint


# class Jigsaw:

#     def __init__(self, r, c):
#         self.pieces = []
#         self.row = r
#         self.col = c

#     def __str__(self):
#         """
#         Writes the state and value to a string.
#         """
#         s =" "
#         d = ""
#         f = ""
#         g = ""
#         for row in self.pieces:
#         #print(row)
#             for col in row:
#                #print(col)
#                 d = d +" "+ format(col[0])
#         print(d)
#         for row in self.pieces:
#             #print(row)
#             for col in row:
#             #print(col)
#                 f = f +" " + format(col[1])
#         print(f)

#         for row in self.pieces:
#             #print(row)
#             for col in row:
#                 #print(col)
#                 g = g +" "+ format(col[2])
#         print(g)



#     #     return pce
#     # result = 'ball : %s' \
#     #     % (pce)
#         #return r

#     def __repr__(self):
#         """
#         Returns the string representation.
#         """
#         return str(self)

#     def puzzle_board(self):
#         for c in range(self.row):
#             for d in range(self.col):
#                 self.pieces.append(self.add_piece)

#         return self.pieces

#     def add_piece(self):
#         a = PieceGenerator()
#         b = self.a_piece(a.idn,a.top,a.left,a.right,a.bottom)
#         self.pieces.append(b)
#         return(b)


#     def mis(self):
#         self.add_piece()

#      # def boardShuffle(self,board):

#     def a_piece(self, id, top,left,right,bottom):
#         """
#         Returns the piece values.
#         """
#         pce = [[" ", top, " "], [left, id, right], [" ", bottom, " "]]
#         return(pce)

#     # def puzzleSolve(self,board):

# class PieceGenerator:
#     """
#     Creates new puzzle pieces with their values.
#     """
#     idn = 0 #Global variable to keep track of all the pieces
#     def __init__(self):
#         """
#         A piece have top, bottom, right, left values and puzzle piece it self
#         """
#         self.top = randint(10,99)
#         self.bottom = randint(10,99)
#         self.right = randint(10,99)
#         self.left = randint(10,99)
#         PieceGenerator.idn += 1

# print(Jigsaw(3,5).puzzle_board())


from models.database import Database

# Teste do gerenciador de contexto
with Database('./data/tarefas.sqlite3') as db:
    db.executar('INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);', ('Usar o gerenciador de contexto', '2026-02-03'))