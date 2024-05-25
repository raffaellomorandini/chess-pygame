import pygame
from pezzi import Scacchiera
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
center_x = screen.get_width() / 2
center_y = screen.get_height() / 2

board_size = 8
tile = 50
piece = 20

board = [[None]*board_size for _ in range(board_size)]
for i in range(board_size):
    for j in range(board_size):
        board[i][j] = pygame.Rect(center_x-(tile*board_size/2+tile) + (j+1)*tile, center_y-(tile*board_size/2+tile) + (i+1)*tile, tile,tile)
        print(board[i][j])

pieces = [[None] * board_size for _ in range(board_size)]

for i in range(board_size):
    pieces[0][i] = pygame.Rect(board[0][i][0]+tile/2-piece/2, board[0][i][1]+tile/2-piece/2, piece, piece)

selected_piece = None
selected_piece_i = -1
selected_piece_j = -1
offset = pygame.Vector2(0,0)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(board_size):
                    for j in range(board_size):
                        if pieces[i][j] != None and pieces[i][j].collidepoint(event.pos):
                            selected_piece = pieces[i][j]
                            selected_piece_i = i
                            selected_piece_j = j
                            offset = pygame.Vector2(pieces[i][j].x - event.pos[0], pieces[i][j].y - event.pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and selected_piece:
                # i pezzi scompaiono
                print(selected_piece_i, selected_piece_j)
                if board[0][0].x > selected_piece.x:
                    selected_piece.x = board[selected_piece_i][selected_piece_j].x+tile/2-piece/2
                    selected_piece.y = board[selected_piece_i][selected_piece_j].y+tile/2-piece/2
                else: 
                    for i in range(board_size):
                        for j in range(board_size):
                            if(board[i][j].x <= selected_piece.x and board[i][j].x+tile > selected_piece.x and board[i][j].y <= selected_piece.y and board[i][j].y + tile  > selected_piece.y):
                                if not(i == selected_piece_i and j == selected_piece_j):
                                    pieces[i][j] = pieces[selected_piece_i][selected_piece_j]
                                    pieces[selected_piece_i][selected_piece_j] = None

                                selected_piece.x = board[i][j][0]+tile/2-piece/2
                                selected_piece.y = board[i][j][1]+tile/2-piece/2
                                    
                                print(pieces)
                selected_piece = None
            
        elif event.type == pygame.MOUSEMOTION:
            if selected_piece:
                selected_piece.x, selected_piece.y = event.pos[0] + offset.x, event.pos[1] + offset.y
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    # stampa scacchiera
    for i in range(board_size):
        for j in range(board_size):
            color = "black" if (i + j) % 2 == 0 else "white"
            pygame.draw.rect(screen, color, rect=board[i][j])
    # stampa pezzi
    for i in range(board_size):
        for j in range(board_size):
            if pieces[i][j] != None:
                pygame.draw.rect(screen, "red", rect=pieces[i][j])

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()