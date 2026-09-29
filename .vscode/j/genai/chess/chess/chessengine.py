class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "bP", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"], ]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"           
        self.board[move.endRow][move.endCol] = move.pieceMoved    
        self.moveLog.append(move)                                  
        self.whiteToMove = not self.whiteToMove   
     
    def undomove(self):
        if len(self.movelog) !=0:
           move=self.moveLog.pop()
           self.board[move.startRow][move.startCol]=move.piecemoved
           self.board[move.endRow][move.endCol]=move.pieceCaptured
           self.whiteToMove =not self.whiteToMove
         
    def getValidMoves(self):
        return self.getAllPossibleMoves()
    
    #all mmoves no check
    def getAllPossibleMoves(self):
        moves=[]
        for r in range(len(self.board)): #row
            for i in range(len(self.board[r])): #column
                turn=self.board[r][i][0]
                if (turn=="w" and  self.whiteToMove) or (turn=="b" and not self.whiteToMove):
                    piece=self.board[r][i][1]
                    if piece=="P":
                        self.getPawnMoves(r,i,moves)
                    elif piece=="R":
                        self.getRookMoves(r,i,moves)
        return moves

    def getPawnMoves(self,r,i,moves):
        if self.whiteToMove:
            if self.board[r-1][i]=="--":
                moves.append(Move((r,i),(r-1,i),self.board))
                if r==6 and self.board[r-2][i]=="--":
                    moves.append(Move((r,i),(r-2,i),self.board))
            if i-1>=0:
                if self.board[r-1][i-1][0]=="b":
                    moves.append(Move((r-1,i-1),(r-1,i-1),self.board))
            if i+1<=7:
                 if self.board[r-1][i+1][0]=="b":
                        moves.append(Move((r-1,i+1),(r-1,i+1),self.board))
                    
    def getRookMoves(self,r,i,moves):
        pass
    









class Move():
    ranksToRows = {'1': 7, '2': 6, '3': 5, '4': 4,
                   '5': 3,'6': 2, '7': 1, '8': 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                   'e': 4, 'f': 5, 'g': 6, 'h': 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]  
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID=self.startRow*1000 +self.startCol*100+self.endRow*10+self.endCol
    def __eq__(self, other):
        if isinstance(other,Move):
            return self.moveID==other.moveID
        return False

    def getChessNotation(self):
        return self.colsToFiles[self.startCol] + self.rowsToRanks[self.startRow] + \
               self.colsToFiles[self.endCol] + self.rowsToRanks[self.endRow]