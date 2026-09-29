import pygame as p
import chessengine

p.init()
WIDTH = 512
HEIGHT = 512
dimen = 8
sq_size = HEIGHT // dimen
maxfps = 15
IMAGES = {}


def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (sq_size, sq_size))


def drawPieces(screen, board):
    for r in range(dimen):
        for c in range(dimen):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


def drawBoard(screen):
    colors = [p.Color("white"), p.Color('gray')]
    for r in range(dimen):
        for c in range(dimen):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessengine.GameState()
    validMoves=gs.getValidMoves()
    print(gs.board)
    loadImages()
    running = True
    sqselected = ()
    playerclick = []
    moveMade=False #


    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // sq_size
                row = location[1] // sq_size
                if sqselected == (row, col):  
                    sqselected = ()
                    playerclick =[]
                else:                         
                    sqselected = (row, col)
                    playerclick.append(sqselected)
                if len(playerclick) == 2:
                    move = chessengine.Move(playerclick[0], playerclick[1], gs.board) 
                    print(move.getChessNotation()) 
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade=True
                    sqselected = ()          
                    playerclick = []
            elif e.type==p.KEYDOWN:
                if e.key==p.K_z:
                    gs.undomove
        if moveMade==True:
            validMoves=gs.getValidMoves()
            moveMade=False

        drawGameState(screen, gs)
        clock.tick(maxfps)
        p.display.flip()


if __name__ == "__main__":
    main()