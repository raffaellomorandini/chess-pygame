from pygame import Rect
from enum import Enum

class TipoPezzo(Enum):
    Regina = 1
    Re = 2
    Alfiere = 3
    Torre = 4
    Cavallo = 5
    Pedone = 6 

class Colore(Enum):
    Nero = 0
    Bianco = 1


class Pos():
    def __init__(self, y, x):
        self.x = x
        self.y = y

class Pezzo:
    def __init__(self, piece: Rect, pos : Pos, type: TipoPezzo, colore: Colore):
        self.piece : Rect = piece
        self.pos : Pos = pos
        self.type : TipoPezzo = type
        self.colore : Colore = colore
        self.possibili : Pos = []
        if(self.type.value == 6):
            self.has_moved : bool = False

class Scacchiera:
    def __init__(self, center_x, center_y, tile):
        self.center_x = center_x
        self.center_y = center_y
        self.tile = tile
        self.piece = int(tile*0.5)
        self.size = 8
        self.board = [[None]*self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = Rect(self.center_x-(self.tile*self.size/2+self.tile) + (j+1)*self.tile, self.center_y-(self.tile*self.size/2+self.tile) + (i+1)*self.tile, self.tile,self.tile)

        self.pieces = [[None]*self.size for _ in range(self.size)]

        self.pieces[0][0] = Pezzo(Rect(self.board[0][0].x+self.tile/2-self.piece/2, self.board[0][0].y+tile/2-self.piece/2, self.piece, self.piece), Pos(0,0), TipoPezzo.Torre, Colore.Nero)
        self.pieces[0][1] = Pezzo(Rect(self.board[0][1].x+self.tile/2-self.piece/2, self.board[0][1].y+tile/2-self.piece/2, self.piece, self.piece), Pos(0,1),TipoPezzo.Cavallo, Colore.Nero)
        self.pieces[0][2] = Pezzo(Rect(self.board[0][2].x+self.tile/2-self.piece/2, self.board[0][2].y+tile/2-self.piece/2, self.piece, self.piece), Pos(0,2), TipoPezzo.Alfiere, Colore.Nero)
        self.pieces[0][3] = Pezzo(Rect(self.board[0][3].x+self.tile/2-self.piece/2, self.board[0][3].y+tile/2-self.piece/2, self.piece, self.piece), Pos(0,3), TipoPezzo.Re, Colore.Nero)
        self.pieces[0][4] = Pezzo(Rect(self.board[0][4].x+self.tile/2-self.piece/2, self.board[0][4].y+tile/2-self.piece/2, self.piece, self.piece), Pos(0,4), TipoPezzo.Regina, Colore.Nero)
        self.pieces[0][5] = Pezzo(Rect(self.board[0][5].x+self.tile/2-self.piece/2, self.board[0][5].y+tile/2-self.piece/2, self.piece, self.piece), Pos(0,5), TipoPezzo.Alfiere, Colore.Nero)
        self.pieces[0][6] = Pezzo(Rect(self.board[0][6].x+self.tile/2-self.piece/2, self.board[0][6].y+tile/2-self.piece/2, self.piece, self.piece), Pos(0,6), TipoPezzo.Cavallo, Colore.Nero)
        self.pieces[0][7] = Pezzo(Rect(self.board[0][7].x+self.tile/2-self.piece/2, self.board[0][7].y+tile/2-self.piece/2, self.piece, self.piece), Pos(0,7), TipoPezzo.Torre, Colore.Nero)
        for i in range(self.size):
            self.pieces[1][i] = Pezzo(Rect(self.board[1][i].x+self.tile/2-self.piece/2, self.board[1][i].y+tile/2-self.piece/2, self.piece, self.piece), Pos(1,i), TipoPezzo.Pedone, Colore.Nero)

        self.pieces[7][0] = Pezzo(Rect(self.board[7][0].x+self.tile/2-self.piece/2, self.board[7][0].y+tile/2-self.piece/2, self.piece, self.piece), Pos(7,0), TipoPezzo.Torre, Colore.Bianco)
        self.pieces[7][1] = Pezzo(Rect(self.board[7][1].x+self.tile/2-self.piece/2, self.board[7][1].y+tile/2-self.piece/2, self.piece, self.piece), Pos(7,1), TipoPezzo.Cavallo, Colore.Bianco)
        self.pieces[7][2] = Pezzo(Rect(self.board[7][2].x+self.tile/2-self.piece/2, self.board[7][2].y+tile/2-self.piece/2, self.piece, self.piece), Pos(7,2), TipoPezzo.Alfiere, Colore.Bianco)
        self.pieces[7][3] = Pezzo(Rect(self.board[7][3].x+self.tile/2-self.piece/2, self.board[7][3].y+tile/2-self.piece/2, self.piece, self.piece), Pos(7,3), TipoPezzo.Re, Colore.Bianco)
        self.pieces[7][4] = Pezzo(Rect(self.board[7][4].x+self.tile/2-self.piece/2, self.board[7][4].y+tile/2-self.piece/2, self.piece, self.piece), Pos(7,4), TipoPezzo.Regina, Colore.Bianco)
        self.pieces[7][5] = Pezzo(Rect(self.board[7][5].x+self.tile/2-self.piece/2, self.board[7][5].y+tile/2-self.piece/2, self.piece, self.piece), Pos(7,5), TipoPezzo.Alfiere, Colore.Bianco)
        self.pieces[7][6] = Pezzo(Rect(self.board[7][6].x+self.tile/2-self.piece/2, self.board[7][6].y+tile/2-self.piece/2, self.piece, self.piece), Pos(7,6), TipoPezzo.Cavallo, Colore.Bianco)
        self.pieces[7][7] = Pezzo(Rect(self.board[7][7].x+self.tile/2-self.piece/2, self.board[7][7].y+tile/2-self.piece/2, self.piece, self.piece), Pos(7,7), TipoPezzo.Torre, Colore.Bianco)
        for i in range(self.size):
            self.pieces[6][i] = Pezzo(Rect(self.board[6][i].x+self.tile/2-self.piece/2, self.board[6][i].y+tile/2-self.piece/2, self.piece, self.piece), Pos(6,i), TipoPezzo.Pedone, Colore.Bianco)

    def possibili_pos(self, pezzo : Pezzo):
        pezzo.possibili = [] 
        possibile_posizione = None
        # PEDONE N/B
        if(pezzo.type.value == 6):
            dy = -1 if pezzo.colore.value == 0 else 1
            possibile_posizione = Pos(pezzo.pos.y-1*dy,pezzo.pos.x)
            if(self.pieces[possibile_posizione.y][possibile_posizione.x] == None and possibile_posizione.x >= 0 and possibile_posizione.x < self.size and possibile_posizione.y >= 0 and possibile_posizione.y < self.size):
                pezzo.possibili.append(possibile_posizione)
                if(not pezzo.has_moved):
                    possibile_posizione = Pos(pezzo.pos.y-2*dy,pezzo.pos.x)
                    if(self.pieces[possibile_posizione.y][possibile_posizione.x] == None and possibile_posizione.x >= 0 and possibile_posizione.x < self.size and possibile_posizione.y >= 0 and possibile_posizione.y < self.size):
                        pezzo.possibili.append(possibile_posizione)
            # Rivedere sta merda
            possibile_posizione = Pos(pezzo.pos.y -1*dy, pezzo.pos.x+1)
            if possibile_posizione.x >= 0 and possibile_posizione.x < self.size and possibile_posizione.y >= 0 and possibile_posizione.y < self.size:
                if(self.pieces[possibile_posizione.y][possibile_posizione.x] != None):
                    if self.pieces[possibile_posizione.y][possibile_posizione.x].colore != pezzo.colore:
                        pezzo.possibili.append(possibile_posizione)
            possibile_posizione = Pos(pezzo.pos.y -1*dy, pezzo.pos.x-1)
            if possibile_posizione.x >= 0 and possibile_posizione.x < self.size and possibile_posizione.y >= 0 and possibile_posizione.y < self.size:
                if(self.pieces[possibile_posizione.y][possibile_posizione.x] != None):
                    
                    if self.pieces[possibile_posizione.y][possibile_posizione.x].colore != pezzo.colore:
                        pezzo.possibili.append(possibile_posizione)
        # CAVALLO
        if(pezzo.type.value == 5):
            for i in range(2):
                for j in range(2):
                    mult_y = -1 if i % 2 == 0 else 1
                    mult_x = -1 if j % 2 == 0 else 1
                    possibile_posizione = Pos(pezzo.pos.y + 2*mult_y, pezzo.pos.x + 1*mult_x)
                    if possibile_posizione.x >= 0 and possibile_posizione.x < self.size and possibile_posizione.y >= 0 and possibile_posizione.y < self.size:
                        if self.pieces[possibile_posizione.y][possibile_posizione.x] != None:

                            if self.pieces[possibile_posizione.y][possibile_posizione.x].colore != pezzo.colore:
                                pezzo.possibili.append(possibile_posizione)
                        else:
                            pezzo.possibili.append(possibile_posizione)
                    possibile_posizione = Pos(pezzo.pos.y + 1*mult_y, pezzo.pos.x + 2*mult_x)
                    if possibile_posizione.x >= 0 and possibile_posizione.x < self.size and possibile_posizione.y >= 0 and possibile_posizione.y < self.size:
                        if self.pieces[possibile_posizione.y][possibile_posizione.x] != None:

                            if self.pieces[possibile_posizione.y][possibile_posizione.x].colore != pezzo.colore:
                                pezzo.possibili.append(possibile_posizione)
                        else:
                            pezzo.possibili.append(possibile_posizione)
        # TORRE
        if(pezzo.type.value == 4):
            for i in range(2):
                mult= -1 if i % 2 == 0 else 1
                conta = 0
                piece_encauntered = False
                while not piece_encauntered:
                    conta += 1
                    possibile_posizione = Pos(pezzo.pos.y + conta*mult, pezzo.pos.x)
                    if possibile_posizione.x >= 0 and possibile_posizione.x < self.size and possibile_posizione.y >= 0 and possibile_posizione.y < self.size:
                        if self.pieces[possibile_posizione.y][possibile_posizione.x] != None:
                            if self.pieces[possibile_posizione.y][possibile_posizione.x].colore != pezzo.colore:
                                pezzo.possibili.append(possibile_posizione)
                            piece_encauntered = True
                        else:
                            pezzo.possibili.append(possibile_posizione)

                    else: 
                        piece_encauntered = True
                    
               

                conta = 0
                piece_encauntered = False
                while not piece_encauntered:
                  
                    conta += 1
                    possibile_posizione = Pos(pezzo.pos.y, pezzo.pos.x + conta*mult)
                    if possibile_posizione.x >= 0 and possibile_posizione.x < self.size and possibile_posizione.y >= 0 and possibile_posizione.y < self.size:
                        if self.pieces[possibile_posizione.y][possibile_posizione.x] != None:
                            if self.pieces[possibile_posizione.y][possibile_posizione.x].colore != pezzo.colore:
                                pezzo.possibili.append(possibile_posizione)
                            piece_encauntered = True
                        else:
                            pezzo.possibili.append(possibile_posizione)

                    else: 
                        piece_encauntered = True
           

    def calcola_pos(self):
        for i in range(self.size):
            for j in range(self.size):
                if(self.pieces[i][j] != None):
                    self.possibili_pos(pezzo=self.pieces[i][j])






