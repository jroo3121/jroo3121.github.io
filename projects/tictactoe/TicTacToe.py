import tkinter as tk
from random import choice

class Game(tk.Tk):
    
    def win(self):
        self.game_over = True
        self.title("X Wins!")
        line = self.board.getWinningLine()
        self.drawWinningLine(line)
    
    def lose(self):
        self.game_over = True
        self.title("O Wins!")
        line = self.board.getWinningLine()
        self.drawWinningLine(line)
        
    def tie(self):
        self.game_over = True
        self.title("Tie!")
        for i in range(3):
            for j in range(3):
                self.cells[(i,j)].config(bg="#f3dcc5")
    
    def getLevel(self):
        if self.ai_level_var.get() == "Easy": return 1
        elif self.ai_level_var.get() == "Medium": return 2
        elif self.ai_level_var.get() == "Hard": return 3
        else: return 2
        
    def cellClick(self, i, j):
        if self.board.isOccupied(i, j) or self.game_over:
            return

        if self.turn == "X":
            self.cells[(i, j)].config(text="X", fg="red", font=("Arial", 100, "bold"))
            self.board.enter(i, j, 1)
        else:
            self.cells[(i, j)].config(text="O", fg="blue", font=("Arial", 100, "bold"))
            self.board.enter(i, j, 0)

        if self.board.xWin(): 
            self.win()
            return
        if self.board.oWin(): 
            self.lose()
            return
        if self.board.isTie(): 
            self.tie()
            return

        if self.multiplayer_var.get():
            self.turn = "O" if self.turn == "X" else "X"
        else:
            if self.turn == "X":
                self.turn = "O"
                self.after(200, lambda: self.computerMove())
            else:
                self.turn = "X"
        
        if self.board.xWin(): 
            self.win()
            return
        if self.board.oWin(): 
            self.lose()
            return
        if self.board.isTie(): 
            self.tie()
            return
    
    def computerMove(self):
        comp_move = self.ai.AIMove(self.board)
        self.cells[(comp_move[0], comp_move[1])].config(text="O", fg="blue", font=("Arial", 100, "bold"))
        self.board.enter(comp_move[0], comp_move[1], 0)
        if self.board.oWin(): self.lose()
        if self.board.isTie(): self.tie()
        self.turn = "X"
        
    def newGame(self, level=3, multiplayer=False, player_starts=True):
        self.game_over = False
        self.board = Board()
        self.ai = AI(level)
        self.title("Tic Tac Toe")
        self.turn = "X" if player_starts else "O"
        for (r, c), cell in self.cells.items():
            cell.config(text="", bg="white")
        if not player_starts and not multiplayer:
            self.computerMove()
    
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        w = 500
        h = 650
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - w) // 2
        y = (screen_height - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y-30}")
        
        self.rowconfigure(1, weight=7)
        
        frame = tk.Frame(self, width=500, height=500, bg="black")
        frame.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="nsew", padx=0, pady=0)
        frame.grid_propagate(False) 

        for r in range(3):
            frame.rowconfigure(r, weight=20, uniform="board")
        for c in range(3):
            frame.columnconfigure(c, weight=20, uniform="board")
        
        self.cells = {}
        for r in range(3):
            for c in range(3):
                cell = tk.Label(frame, borderwidth=1, relief="solid", bg="white")
                cell.grid(row=r, column=c, sticky="nsew")
                cell.bind("<Button-1>", lambda e, row=r, col=c: self.cellClick(row, col))
                cell.bind("<Button-2>", lambda e, row=r, col=c: self.cellClick(row, col))
                cell.bind("<Button-3>", lambda e, row=r, col=c: self.cellClick(row, col))
                self.cells[(r, c)] = cell

        footer = tk.Frame(self)
        footer.grid(row=3, column=0, columnspan=3, pady=10, sticky="ew")
        
        footer.rowconfigure(0, weight=1)
        footer.rowconfigure(1, weight=1)
        
        for i in range(3):
            footer.columnconfigure(i, weight=1)

        self.multiplayer_var = tk.BooleanVar(value=False)
        self.multiplayer_check = tk.Checkbutton(footer, text="Multiplayer?", variable=self.multiplayer_var, font=("Arial", 12), anchor="center", command=lambda: self.newGame(multiplayer=self.multiplayer_var.get(), player_starts=self.x_starts_var.get(), level=self.getLevel()))
        self.multiplayer_check.grid(row=0, column=0, padx=10, pady=20, sticky="w")

        self.ai_level_var = tk.StringVar(value="Medium")
        self.ai_dropdown = tk.OptionMenu(footer, self.ai_level_var, "Easy", "Medium", "Hard", command=lambda _: self.newGame(multiplayer=self.multiplayer_var.get(), player_starts=self.x_starts_var.get(), level=self.getLevel()))
        self.ai_dropdown.config(font=("Arial", 12))
        self.ai_dropdown.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

        self.new_game_btn = tk.Button(footer, text="New Game", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=3, command=lambda: self.newGame(multiplayer=self.multiplayer_var.get(), player_starts=self.x_starts_var.get(), level=self.getLevel()))
        self.new_game_btn.grid(row=0, column=2, padx=10, pady=20, sticky="nsew")
        
        self.quit_btn = tk.Button(footer, text="Quit", font=("Arial", 12, "bold"), bg="red", fg="white", padx=10, pady=3, command=lambda: exit())
        self.quit_btn.grid(row=1, column=2, padx=10, pady=20, sticky="nsew")

        self.x_starts_var = tk.BooleanVar(value=True)
        self.x_starts_check = tk.Checkbutton(footer, text="X starts?", variable=self.x_starts_var, font=("Arial", 12), anchor="center", command=lambda: self.newGame(multiplayer=self.multiplayer_var.get(), player_starts=self.x_starts_var.get(), level=self.getLevel()))
        self.x_starts_check.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="w")


        self.newGame()

    def drawWinningLine(self, cells):
        for i, j in cells:
            self.cells[(i, j)].config(bg="lightgreen")


# -----------------------------------------------------------------------------------------

class Board(list):
    def __init__(self, matrix=None):
        if matrix is None:
            matrix = [[None, None, None], [None, None, None], [None, None, None]]
        super().__init__(matrix)

    def copy(self):
        return Board([list(row) for row in self])
    
    def flatten(self):
        return [self[i][j] for i in range(3) for j in range(3)]
    
    def getCell(self, i, j):
        return self[i][j]

    def isOccupied(self, i, j):
        return self[i][j] is not None
    
    def isFree(self, i, j):
        return self[i][j] is None
    
    def letter(self, n):
        if n==0: return 'O'
        if n==1: return 'X'
        return None
    
    def __repr__(self):
        s = ""
        for row in self:
            for i in row:
                s += (self.letter(i) if i is not None else ".") + " "
            s += "\n"
        return s
    
    def enter(self, i, j, value):
        self[i][j] = value
        
    def xWin(self):
        return any([
            # Rows
            self[0][0]==1 and self[0][1]==1 and self[0][2]==1,
            self[1][0]==1 and self[1][1]==1 and self[1][2]==1,
            self[2][0]==1 and self[2][1]==1 and self[2][2]==1,
            # Columns
            self[0][0]==1 and self[1][0]==1 and self[2][0]==1,
            self[0][1]==1 and self[1][1]==1 and self[2][1]==1,
            self[0][2]==1 and self[1][2]==1 and self[2][2]==1,
            # Diagonals
            self[0][0]==1 and self[1][1]==1 and self[2][2]==1,
            self[0][2]==1 and self[1][1]==1 and self[2][0]==1
        ])

    def oWin(self):
        return any([
            # Rows
            self[0][0]==0 and self[0][1]==0 and self[0][2]==0,
            self[1][0]==0 and self[1][1]==0 and self[1][2]==0,
            self[2][0]==0 and self[2][1]==0 and self[2][2]==0,
            # Columns
            self[0][0]==0 and self[1][0]==0 and self[2][0]==0,
            self[0][1]==0 and self[1][1]==0 and self[2][1]==0,
            self[0][2]==0 and self[1][2]==0 and self[2][2]==0,
            # Diagonals
            self[0][0]==0 and self[1][1]==0 and self[2][2]==0,
            self[0][2]==0 and self[1][1]==0 and self[2][0]==0
        ])
    
    def isFull(self):
        return all(cell is not None for row in self for cell in row)
    
    def isTie(self):
        if (self.xWin() or self.oWin()):
            return False
        elif (self.isFull()):
            return True
        else:
            return False
        
    def isEmpty(self):
        return all([self.isFree(i,j) for i in range(3) for j in range(3)])
        
    def onlyCenter(self):
        return all(self.isFree(i, j) for i, j in [(0,0),(0,1),(0,2),(2,0),(2,1),(2,2),(1,0),(1,2)]) and self.isOccupied(1,1)
    
    def amountOccupied(self):
        return 9 - (self.flatten().count(None))
    
    def oneOccupied(self):
        return self.amountOccupied() == 1
    
    def freeCells(self):
        return [(i,j) for i in range(3) for j in range(3) if self.isFree(i,j)]
    
    def getWinningLine(self):
        for r in range(3):
            if self[r][0] == self[r][1] == self[r][2] != None:
                return ((r, 0), (r, 1), (r, 2))
        for c in range(3):
            if self[0][c] == self[1][c] == self[2][c] != None:
                return ((0, c), (1, c), (2, c))
        if self[0][0] == self[1][1] == self[2][2] != None:
            return ((0, 0), (1, 1), (2, 2))
        if self[0][2] == self[1][1] == self[2][0] != None:
            return ((0, 2), (1, 1), (2, 0))
        
        return None



# -----------------------------------------------------------------------------------------------


class AI(object):
    def __init__(self, level=3):
        self.lvl = level
    
    def AIMove(self, board):
        if self.lvl == 1:
            return self.lvlOne(board)
        elif self.lvl == 2:
            return self.lvlTwo(board)
        elif self.lvl == 3:
            return self.lvlThree(board)
    
    def findLine(self, flat, player):
        
        # Rows
        if flat[0]==player and flat[1]==player and flat[2]==None: return (0,2)
        if flat[0]==player and flat[2]==player and flat[1]==None: return (0,1)
        if flat[1]==player and flat[2]==player and flat[0]==None: return (0,0)
    
        if flat[3]==player and flat[4]==player and flat[5]==None: return (1,2)
        if flat[3]==player and flat[5]==player and flat[4]==None: return (1,1)
        if flat[4]==player and flat[5]==player and flat[3]==None: return (1,0)
    
        if flat[6]==player and flat[7]==player and flat[8]==None: return (2,2)
        if flat[6]==player and flat[8]==player and flat[7]==None: return (2,1)
        if flat[7]==player and flat[8]==player and flat[6]==None: return (2,0)
    
        # Columns
        if flat[0]==player and flat[3]==player and flat[6]==None: return (2,0)
        if flat[0]==player and flat[6]==player and flat[3]==None: return (1,0)
        if flat[3]==player and flat[6]==player and flat[0]==None: return (0,0)
    
        if flat[1]==player and flat[4]==player and flat[7]==None: return (2,1)
        if flat[1]==player and flat[7]==player and flat[4]==None: return (1,1)
        if flat[4]==player and flat[7]==player and flat[1]==None: return (0,1)
    
        if flat[2]==player and flat[5]==player and flat[8]==None: return (2,2)
        if flat[2]==player and flat[8]==player and flat[5]==None: return (1,2)
        if flat[5]==player and flat[8]==player and flat[2]==None: return (0,2)
    
        # Diagonals
        if flat[0]==player and flat[4]==player and flat[8]==None: return (2,2)
        if flat[0]==player and flat[8]==player and flat[4]==None: return (1,1)
        if flat[4]==player and flat[8]==player and flat[0]==None: return (0,0)
    
        if flat[2]==player and flat[4]==player and flat[6]==None: return (2,0)
        if flat[2]==player and flat[6]==player and flat[4]==None: return (1,1)
        if flat[4]==player and flat[6]==player and flat[2]==None: return (0,2)
        
        return None
    
    def findWin(self, flat):
        return self.findLine(flat, 0)
    
    def findBlock(self, flat):
        return self.findLine(flat, 1)

    def minimax(self, board, ai_turn):
        if board.xWin():
            return -1 
        if board.oWin():
            return 1
        if board.isTie():
            return 0

        if ai_turn:
            best_score = -99999
            for i in range(3):
                for j in range(3):
                    if board.isFree(i, j):
                        board.enter(i, j, 0)
                        score = self.minimax(board, False)
                        board.enter(i, j, None)
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = 99999
            for i in range(3):
                for j in range(3):
                    if board.isFree(i, j):
                        board.enter(i, j, 1)
                        score = self.minimax(board, True)
                        board.enter(i, j, None)
                        best_score = min(best_score, score)
            return best_score

        
    def bestMove(self, board, player):
        move_scores = {} 

        for i in range(3):
            for j in range(3):
                if board.isFree(i, j):
                    board.enter(i, j, player)
                    score = self.minimax(board, False)
                    board.enter(i, j, None)
                    move_scores[(i, j)] = score
        
        max_score = max(move_scores.values())
        self.playing_for = max_score
        # print(board)
        # print(move_scores)
        best_moves = [move for (move, score) in move_scores.items() if score == max_score]
        return choice(best_moves)

    
    
    def lvlOne(self, board):
        free_cells = board.freeCells()
        return choice(free_cells)
    
    
    def lvlTwo(self, board):
        flat = board.flatten()
    
        move = self.findWin(flat) # find win
        if bool(move):
            return move
        
        move = self.findBlock(flat) # find block
        if bool(move):
            return move
        
        
    
        # Random
        free_cells = board.freeCells()
        return choice(free_cells)
    
    

    
    def lvlThree(self, board):
        flat = board.flatten()
        free_cells = board.freeCells()
        
        if board.isEmpty(): # saving time
            return choice(free_cells) 
        
        if board.oneOccupied(): # saving time
            if board.onlyCenter():
                return choice([(0,0), (0,2), (2,0), (2,2)])
            if any([board[0][0]==1, board[0][2]==1, board[2][0]==1, board[2][2]==1]):
                return (1, 1)
            else:
                return choice([(0,0), (0,2), (1, 1), (2,0), (2,2)])
        
        move = self.bestMove(board, 0) # minimax algorithm
        if bool(move):
            return move
                
        # Random (if all else fails)
        return choice(free_cells)




app = Game()
app.mainloop()
