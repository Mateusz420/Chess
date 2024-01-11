import pygame
import pieces_class
import pandas

pygame.init()
clock = pygame.time.Clock()

# Setting up the screen
screen = pygame.display.set_mode((840, 840))
chess_board = pygame.image.load("chess_board.png")

# Splitting the chess board into squares
board_x = 0
board_y = 735
all_tiles = []
tiles = []
x_coords = []

for i in range(9):
    for j in range(8):
        if j != 7:
            rect = pygame.Rect(board_x, board_y, 105, 105)
            board_x += 105
            all_tiles.append(rect)
        else:
            rect = pygame.Rect(board_x, board_y, 105, 105)
            board_x = 0
            board_y -= 105
            all_tiles.append(rect)

for i in range(len(all_tiles)):
    if i % 8 == 0 and i != 0:
        tiles.append(x_coords)
        x_coords = [all_tiles[i]]
    else:
        x_coords.append(all_tiles[i])

# test
for i in tiles:
    print(i)

icon = pygame.image.load("pieces\\black_pawn.png")
pygame.display.set_caption("Chess")
pygame.display.set_icon(icon)

pieces = pieces_class.Pieces()
screen.blit(chess_board, (0, 0))
pieces.pieces_draw(screen)
pygame.display.update()

global MOVE
MOVE ="SELECT_PIECE"
# current piece and coords
# global selected_piece
# selected_piece = ""
# global selected_field
# selected_field = ""
# print(selected_piece)
# global selected_x_coord
# selected_x_coord = ""
# print(selected_x_coord)
# global selected_y_coord
# selected_y_coord = ""
# print(selected_y_coord)



def piece_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    
    selected_piece = df.at[piece_x_coord, piece_y_coord]
    print("selected_piece")
    if (selected_piece == pieces_class.Pieces().white_pawn):
        print("white_pawn")
        white_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
    elif (selected_piece == pieces_class.Pieces().black_pawn):
        print("black_pawn")
        black_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
    elif (selected_piece == pieces_class.Pieces().white_knight):
        print("white_knight")
        white_knight_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
    elif (selected_piece == pieces_class.Pieces().black_knight):
        print("black_knight")
        black_knight_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
        
        
    elif (selected_piece == "0"):
        print("0")
        MOVE = "SELECT_PIECE"







def white_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    ### PION PO DOJŚCIU DO KOŃCA MOŻE PRZESKAKIWAĆ NA KOLEJNE KOLUMNY, BUG, KTÓRY PO DODANIU AWANSU PRZESTANIE DZIAŁAĆ
    ### BRAK EN PASSANT

    
    
    global MOVE
    MOVE="SELECT_PIECE"
    print("white_pawn_move")
        
    #bicie
    if piece_x_coord - field_x_coord == 1 and df.at[field_x_coord, field_y_coord] != "0" and piece_y_coord - field_y_coord == 1 or piece_y_coord - field_y_coord == -1 and df.at[field_x_coord, field_y_coord] != "0":
        print("white_pawn_bicie")
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_pawn
        df.at[piece_x_coord, piece_y_coord] = "0"
        print(df)
        MOVE="SELECT_PIECE"
        
    #ruch o 2 pola
    elif piece_y_coord == field_y_coord and piece_x_coord == 6 and field_x_coord == 4:
        print("white_pawn_rucho2")
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_pawn
        df.at[piece_x_coord, piece_y_coord] = "0"
        print(df)
        MOVE="SELECT_PIECE"
        
    #ruch o 1 pole
    elif piece_y_coord == field_y_coord and piece_x_coord - field_x_coord == 1:
        if(df.at[field_x_coord, field_y_coord]) == "0":
            df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_pawn
            df.at[piece_x_coord, piece_y_coord] = "0"
            print("white_pawn_rucho1")
            print(df)
            MOVE="SELECT_PIECE"
        else:
            MOVE="SELECT_PIECE"
            

def black_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    ### PION PO DOJŚCIU DO KOŃCA MOŻE PRZESKAKIWAĆ NA KOLEJNE KOLUMNY, BUG, KTÓRY PO DODANIU AWANSU PRZESTANIE DZIAŁAĆ
    ### BRAK EN PASSANT
    global MOVE
    MOVE="SELECT_PIECE"
    print("black_pawn_move")
        
    #bicie
    if piece_x_coord + field_x_coord == 1 and df.at[field_x_coord, field_y_coord] != "0" and piece_y_coord - field_y_coord == 1 or piece_y_coord - field_y_coord == -1 and df.at[field_x_coord, field_y_coord] != "0":
        print("black_pawn_bicie")
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_pawn
        df.at[piece_x_coord, piece_y_coord] = "0"
        print(df)
        MOVE="SELECT_PIECE"
        
    #ruch o 2 pola
    elif piece_y_coord == field_y_coord and piece_x_coord == 1 and field_x_coord == 3:
        print("black_pawn_rucho2")
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_pawn
        df.at[piece_x_coord, piece_y_coord] = "0"
        print(df)
        MOVE="SELECT_PIECE"
        
    #ruch o 1 pole
    elif piece_y_coord == field_y_coord and piece_x_coord - field_x_coord == -1:
        if(df.at[field_x_coord, field_y_coord]) == "0":
            df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_pawn
            df.at[piece_x_coord, piece_y_coord] = "0"
            print("black_pawn_rucho1")
            print(df)
            MOVE="SELECT_PIECE"
        else:
            MOVE="SELECT_PIECE"



def white_knight_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    MOVE="SELECT_PIECE"
    print("white_horse_move")
    
    #ruchy do przodu 2y+1x
    if piece_x_coord - 2 == field_x_coord and piece_y_coord - 1 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("white_knight_rucho1")
        print(df)
        MOVE="SELECT_PIECE"
    elif piece_x_coord - 2 == field_x_coord and piece_y_coord + 1 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("white_knight_rucho2")
        print(df)
        MOVE="SELECT_PIECE"
        
    #ruchy do tyłu -2y-1x
    elif piece_x_coord + 2 == field_x_coord and piece_y_coord + 1 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("white_knight_rucho3")
        print(df)
        MOVE="SELECT_PIECE"
    elif piece_x_coord + 2 == field_x_coord and piece_y_coord - 1 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("white_knight_rucho4")
        print(df)
        MOVE="SELECT_PIECE"
        
    #ruchy do przodu 1y+1x
    elif piece_x_coord + 1 == field_x_coord and piece_y_coord + 2 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("white_knight_rucho3")
        print(df)
        MOVE="SELECT_PIECE"
    elif piece_x_coord + 1 == field_x_coord and piece_y_coord - 2 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("white_knight_rucho4")
        print(df)
        MOVE="SELECT_PIECE"

        #ruchy do tyłu -1y-1x
    elif piece_x_coord - 1 == field_x_coord and piece_y_coord - 2 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("white_knight_rucho5")
        print(df)
        MOVE="SELECT_PIECE"
    elif piece_x_coord - 1 == field_x_coord and piece_y_coord + 2 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("white_knight_rucho6")
        print(df)
        MOVE="SELECT_PIECE"

    
    
    
def black_knight_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    MOVE="SELECT_PIECE"
    print("black_horse_move")
    
    #ruchy do przodu 2y+1x
    if piece_x_coord - 2 == field_x_coord and piece_y_coord - 1 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("black_knight_rucho1")
        print(df)
        MOVE="SELECT_PIECE"
    elif piece_x_coord - 2 == field_x_coord and piece_y_coord + 1 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("black_knight_rucho2")
        print(df)
        MOVE="SELECT_PIECE"
        
    #ruchy do tyłu -2y-1x
    elif piece_x_coord + 2 == field_x_coord and piece_y_coord + 1 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("black_knight_rucho3")
        print(df)
        MOVE="SELECT_PIECE"
    elif piece_x_coord + 2 == field_x_coord and piece_y_coord - 1 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("black_knight_rucho4")
        print(df)
        MOVE="SELECT_PIECE"
        
    #ruchy do przodu 1y+1x
    elif piece_x_coord + 1 == field_x_coord and piece_y_coord + 2 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("black_knight_rucho3")
        print(df)
        MOVE="SELECT_PIECE"
    elif piece_x_coord + 1 == field_x_coord and piece_y_coord - 2 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("black_knight_rucho4")
        print(df)
        MOVE="SELECT_PIECE"

        #ruchy do tyłu -1y-1x
    elif piece_x_coord - 1 == field_x_coord and piece_y_coord - 2 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("black_knight_rucho5")
        print(df)
        MOVE="SELECT_PIECE"
    elif piece_x_coord - 1 == field_x_coord and piece_y_coord + 2 == field_y_coord:
        df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_knight
        df.at[piece_x_coord, piece_y_coord] = "0"
        print("black_knight_rucho6")
        print(df)
        MOVE="SELECT_PIECE"



df = pandas.DataFrame(pieces_class.Pieces().starting_chess_board_data)
print("wybierz figure")
print(df)

    
    
 


# events
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if(MOVE == "SELECT_PIECE"):
                piece_x_coord = event.pos[1] // 105
                piece_y_coord = event.pos[0] // 105
                piece_coords = [piece_x_coord, piece_y_coord]
                print(f"piece cords {piece_coords}")
                
                MOVE = "SELECT_FIELD"
                
            elif(MOVE == "SELECT_FIELD"):
                field_x_coord = event.pos[1] // 105
                field_y_coord = event.pos[0] // 105
                field_coords = [field_x_coord, field_y_coord]
                print(f"field cords {field_coords}")
                piece_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
                
                
            
            
            
