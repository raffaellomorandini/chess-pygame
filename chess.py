import pygame
from pezzi import Scacchiera, Pos
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
center_x = screen.get_width() / 2
center_y = screen.get_height() / 2

tile = 50
scacchiera = Scacchiera(center_x=center_x, center_y=center_y, tile=tile)
scacchiera.calcola_pos()


selected_piece = None
selected_piece_i = -1
selected_piece_j = -1
offset = pygame.Vector2(0,0)
hasMoved = False
tempPos = None


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(scacchiera.size):
                    for j in range(scacchiera.size):
                        if scacchiera.pieces[i][j] != None and scacchiera.pieces[i][j].piece.collidepoint(event.pos):
                            selected_piece = scacchiera.pieces[i][j].piece
                            selected_piece_i = i
                            selected_piece_j = j
                            offset = pygame.Vector2(scacchiera.pieces[i][j].piece.x - event.pos[0], scacchiera.pieces[i][j].piece.y - event.pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and selected_piece:
                if(scacchiera.board[0][0].x > selected_piece.x or
                   scacchiera.board[0][0].y > selected_piece.y or
                   scacchiera.board[scacchiera.size-1][scacchiera.size-1].x+scacchiera.tile < selected_piece.x or
                   scacchiera.board[scacchiera.size-1][scacchiera.size-1].y+scacchiera.tile < selected_piece.y):
                    selected_piece.x = scacchiera.board[selected_piece_i][selected_piece_j][0]+tile/2-scacchiera.piece/2
                    selected_piece.y = scacchiera.board[selected_piece_i][selected_piece_j][1]+tile/2-scacchiera.piece/2
                else:
                    for i in range(scacchiera.size):
                        for j in range(scacchiera.size):
                            if(scacchiera.board[i][j].x <= selected_piece.x and scacchiera.board[i][j].x+tile > selected_piece.x and scacchiera.board[i][j].y <= selected_piece.y and scacchiera.board[i][j].y + tile  > selected_piece.y):
                                hasMoved = False
                                for posizione in scacchiera.pieces[selected_piece_i][selected_piece_j].possibili:
                                    if posizione.x == j and posizione.y == i:
                                        
                                        scacchiera.pieces[i][j] = scacchiera.pieces[selected_piece_i][selected_piece_j]
                                        scacchiera.pieces[i][j].pos.x = j
                                        scacchiera.pieces[i][j].pos.y = i
                                        if scacchiera.pieces[i][j].type.value == 6:
                                            scacchiera.pieces[i][j].has_moved = True

                                        scacchiera.pieces[selected_piece_i][selected_piece_j] = None

                                        selected_piece.x = scacchiera.board[i][j][0]+tile/2-scacchiera.piece/2
                                        selected_piece.y = scacchiera.board[i][j][1]+tile/2-scacchiera.piece/2

                                        scacchiera.calcola_pos()
                                        hasMoved = True
                                
                                if not hasMoved: 
                                    selected_piece.x = scacchiera.board[selected_piece_i][selected_piece_j][0]+tile/2-scacchiera.piece/2
                                    selected_piece.y = scacchiera.board[selected_piece_i][selected_piece_i][1]+tile/2-scacchiera.piece/2
                                
                 
                selected_piece = None
            
        elif event.type == pygame.MOUSEMOTION:
            if selected_piece:
                selected_piece.x, selected_piece.y = event.pos[0] + offset.x, event.pos[1] + offset.y
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    # stampa scacchiera
    for i in range(scacchiera.size):
        for j in range(scacchiera.size):
            color = "black" if (i + j) % 2 == 0 else "white"
            pygame.draw.rect(screen, color, rect=scacchiera.board[i][j])
    # stampa pezzi
    for i in range(scacchiera.size):
        for j in range(scacchiera.size):
            if scacchiera.pieces[i][j] != None:
                pygame.draw.rect(screen, "red", rect=scacchiera.pieces[i][j].piece)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()