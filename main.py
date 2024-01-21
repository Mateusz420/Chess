import pygame
import pieces_class
import pandas

pygame.init()
clock = pygame.time.Clock()

# Setting up the screen
screen = pygame.display.set_mode((840, 840))
chess_board = pygame.image.load("chess\\chess_board.png")

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

icon = pygame.image.load("chess\\pieces\\black_pawn.png")
pygame.display.set_caption("Chess")
pygame.display.set_icon(icon)

pieces = pieces_class.Pieces()

global MOVE
MOVE ="SELECT_PIECE"
global TURN
TURN = "white"
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
    global TURN
    
    selected_piece = df.at[piece_x_coord, piece_y_coord]
    print("selected_piece")
    
    if (selected_piece == pieces_class.Pieces().white_pawn):
        print("white_pawn")
        white_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
    elif (selected_piece == pieces_class.Pieces().black_pawn):
            print("black_pawn")
            black_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
            
    elif (selected_piece == pieces_class.Pieces().white_knight or selected_piece == pieces_class.Pieces().black_knight):
        print("knight")
        knight_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
        
    
    elif (selected_piece == pieces_class.Pieces().white_rook or selected_piece == pieces_class.Pieces().black_rook):
        print("rook")
        rook_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
    
    # elif (selected_piece == "0"):
    #     print("0")
    #     MOVE = "SELECT_PIECE"
        
    elif (selected_piece == pieces_class.Pieces().white_king or selected_piece == pieces_class.Pieces().black_king):
        print("knight")
        king_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)
    
    
    else:
        print("0")
        MOVE = "SELECT_PIECE"


def white_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    ### PION PO DOJŚCIU DO KOŃCA MOŻE PRZESKAKIWAĆ NA KOLEJNE KOLUMNY, BUG, KTÓRY PO DODANIU AWANSU PRZESTANIE DZIAŁAĆ
    ### BRAK EN PASSANT
    
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    pawn_color = TURN+"_pawn"
    
    print("white_pawn_move")
    print(pawn_color)
    
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), pawn_color):
        if (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]:
            #bicie
            if piece_x_coord - field_x_coord == 1 and df.at[field_x_coord, field_y_coord] != "0" and piece_y_coord - field_y_coord == 1 or piece_y_coord - field_y_coord == -1 and df.at[field_x_coord, field_y_coord] != "0":
                print("white_pawn_bicie")
                df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_pawn
                df.at[piece_x_coord, piece_y_coord] = "0"
                print(df)
                MOVE="SELECT_PIECE"
                TURN="black"
            #ruch o 2 pola
            elif piece_y_coord == field_y_coord and piece_x_coord == 6 and field_x_coord == 4:
                print("white_pawn_rucho2")
                df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_pawn
                df.at[piece_x_coord, piece_y_coord] = "0"
                print(df)
                MOVE="SELECT_PIECE"
                TURN="black"
                
            #ruch o 1 pole
            elif piece_y_coord == field_y_coord and piece_x_coord - field_x_coord == 1:
                if(df.at[field_x_coord, field_y_coord]) == "0":
                    df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().white_pawn
                    df.at[piece_x_coord, piece_y_coord] = "0"
                    print("white_pawn_rucho1")
                    print(df)
                    MOVE="SELECT_PIECE"
                    TURN="black"
                else:
                    MOVE="SELECT_PIECE"
        else:
            MOVE="SELECT_PIECE"
            

def black_pawn_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    ### PION PO DOJŚCIU DO KOŃCA MOŻE PRZESKAKIWAĆ NA KOLEJNE KOLUMNY, BUG, KTÓRY PO DODANIU AWANSU PRZESTANIE DZIAŁAĆ
    ### BRAK EN PASSANT
    
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    pawn_color = TURN+"_pawn"
    
    print("black_pawn_move")
    print(pawn_color)
    
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), pawn_color):
        if (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]:
            #bicie
            if piece_x_coord + field_x_coord == 1 and df.at[field_x_coord, field_y_coord] != "0" and piece_y_coord - field_y_coord == 1 or piece_y_coord - field_y_coord == -1 and df.at[field_x_coord, field_y_coord] != "0":
                print("black_pawn_bicie")
                df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_pawn
                df.at[piece_x_coord, piece_y_coord] = "0"
                print(df)
                MOVE="SELECT_PIECE"
                TURN="white"
                
            #ruch o 2 pola
            elif piece_y_coord == field_y_coord and piece_x_coord == 1 and field_x_coord == 3:
                print("black_pawn_rucho2")
                df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_pawn
                df.at[piece_x_coord, piece_y_coord] = "0"
                print(df)
                MOVE="SELECT_PIECE"
                TURN="white"
                
            #ruch o 1 pole
            elif piece_y_coord == field_y_coord and piece_x_coord - field_x_coord == -1:
                if(df.at[field_x_coord, field_y_coord]) == "0":
                    df.at[field_x_coord, field_y_coord] = pieces_class.Pieces().black_pawn
                    df.at[piece_x_coord, piece_y_coord] = "0"
                    print("black_pawn_rucho1")
                    print(df)
                    MOVE="SELECT_PIECE"
                    TURN="white"
                else:
                    MOVE="SELECT_PIECE"
        else:
            MOVE="SELECT_PIECE"


def knight_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    knight_color = TURN+"_knight"
    
    print("horse_move")
    print(knight_color)
    
    # next turn
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"
    
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), knight_color):
        if (TURN == "white" and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]) or (
            TURN == "black" and  (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]):
            #ruchy do przodu 2y+1x
            if piece_x_coord - 2 == field_x_coord and piece_y_coord - 1 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print("knight_rucho1")
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn
            elif piece_x_coord - 2 == field_x_coord and piece_y_coord + 1 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print("knight_rucho2")
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn
            #ruchy do tyłu -2y-1x
            elif piece_x_coord + 2 == field_x_coord and piece_y_coord + 1 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print("knight_rucho3")
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn
            elif piece_x_coord + 2 == field_x_coord and piece_y_coord - 1 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print("knight_rucho4")
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn
                
            #ruchy do przodu 1y+1x
            elif piece_x_coord + 1 == field_x_coord and piece_y_coord + 2 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print("knight_rucho3")
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn
            elif piece_x_coord + 1 == field_x_coord and piece_y_coord - 2 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print("knight_rucho4")
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn

                #ruchy do tyłu -1y-1x
            elif piece_x_coord - 1 == field_x_coord and piece_y_coord - 2 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print("knight_rucho5")
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn
    
            elif piece_x_coord - 1 == field_x_coord and piece_y_coord + 2 == field_y_coord:
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print("knight_rucho6")
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn
    
    else:
        MOVE="SELECT_PIECE"

def king_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    MOVE="SELECT_PIECE"
    king_color = TURN+"_king"
    
    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"
    
    print("king_move")
    print(king_color)
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), king_color):
        if (TURN == "white" and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]) or (
            TURN == "black" and  (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]):
            if (piece_x_coord - field_x_coord == 1 or piece_x_coord - field_x_coord == -1 or piece_y_coord - field_y_coord == 1 or piece_y_coord - field_y_coord == -1) and (-1 <= piece_x_coord - field_x_coord <= 1 and -1 <= piece_y_coord - field_y_coord <= 1):
                df.at[field_x_coord, field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                df.at[piece_x_coord, piece_y_coord] = "0"
                print(df)
                MOVE="SELECT_PIECE"
                TURN = next_turn

def rook_move(piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
    global MOVE
    global TURN
    
    
    mf = pandas.DataFrame(pieces_class.Pieces().move_chess_board_data)
    mf = mf.replace("1", "0")
    MOVE = "SELECT_PIECE"
    rook_color = TURN + "_rook"

    if TURN == "white":
        next_turn = "black"
    elif TURN == "black":
        next_turn = "white"


    print("rook")
    if df.at[piece_x_coord, piece_y_coord] == getattr(pieces_class.Pieces(), rook_color):
        if (TURN == "white" and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.white[1]) or (
            TURN == "black" and  (field_y_coord * 105, field_x_coord * 105) not in pieces.black[0] and (field_y_coord * 105, field_x_coord * 105) not in pieces.black[1]):
            for i in range(4):
                print("i in range 4")
                next_move = True
                calculated_x = 0
                calculated_y = 0
                x_variable = 1
                y_variable = 1
                x = 0
                y = 0
                if i == 0:  # prawo
                    print("i0")
                    x = 0
                    y = 1
                    y_variable = 1
                    xy= "y"
                elif i == 1:  # lewo
                    print("i1")
                    x = 0
                    y = -1
                    y_variable = -1
                    xy = "y"
                elif i == 2:  # dół
                    print("i2")
                    x = 1
                    y = 0
                    x_variable = 1
                    xy = "x"
                elif i == 3:
                    print("i3")  # góra
                    x = -1
                    y = 0
                    x_variable = -1
                    xy = "x"
                print("path")
                calculated_x = piece_x_coord + x
                calculated_y = piece_y_coord + y

                print(calculated_x)
                print(calculated_y)
                if calculated_y in range(0, 8) and calculated_x in range(0, 8):
                    if df.at[calculated_x, calculated_y] == "0" or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                        print("movelist")

                        while next_move:
                            # print("while")
                            if y!=0:
                                print("y!=0")
                                
                                if df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                    mf.at[calculated_x, calculated_y] = "1"
                                    print("HMMMMMMMMMM")
                                    break
                                
                                
                                if (calculated_y + y_variable) in range(0,8):
                                    print("www")
                                    if calculated_y + y_variable in range(0, 8) and df.at[calculated_x, calculated_y + y_variable] == "0":

                                        if df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                            print("princik1")
                                        if df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn"):
                                            print("princik1")
                                        mf.at[calculated_x, calculated_y] = "1"
                                        mf.at[calculated_x, calculated_y + y_variable] = "1"
                                        print("movelist0x")
                                        print(mf)
                                        
                                        if (calculated_y + y_variable) > piece_y_coord and df.at[calculated_x, calculated_y + y_variable] == "0":
                                            y_variable+=1
                                            print("y1")
                                            
                                        elif (calculated_y + y_variable) < piece_y_coord and df.at[calculated_x, calculated_y + y_variable] == "0":
                                            y_variable -= 1
                                            print("y1.5")
                                        if (calculated_y + y_variable) not in range(0, 8):
                                            
                                            print("www1xx")
                                            calculated_x = 0
                                            calculated_y = 0
                                            break
                                        # break
                                    # break
                                    
                                    elif df.at[calculated_x, calculated_y] == "0":
                                        print("znaleziony1")
                                        mf.at[calculated_x, calculated_y] == "9"
                                        break
                                    
                                    
                                    #bez y variable
                                    elif calculated_y in range(0, 8) and df.at[calculated_x, calculated_y] == "0":
                                        mf.at[calculated_x, calculated_y] = "1"
                                        # print('HHHe muje')
                                        print("movelist0x")
                                        print(mf)
                                        


                                        if (calculated_y + y_variable) > piece_y_coord:
                                            print("lllllllll")
                                            if (calculated_y + y_variable) in range(0,8):
                                                if df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                                    print("CCCC")
                                                elif df.at[calculated_x, calculated_y + y_variable] == "0":
                                                    print("CCCC22")
                                                    break
                                            y_variable+=1
                                        elif (calculated_y + y_variable) < piece_y_coord:
                                            print("llll")
                                            
                                            if (calculated_y + y_variable) in range(0,8):
                                                if df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x, calculated_y + y_variable] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                                    print("CCCC3")
                                                elif df.at[calculated_x, calculated_y + y_variable] == "0":
                                                    print("CCCC223")
                                                    break
                                            y_variable -= 1
                                        if (calculated_y + y_variable) not in range(0, 8):
                                            
                                            print("www123")
                                            calculated_x = 0
                                            calculated_y = 0
                                            break
                                    # else:
                                    #     break
                                    elif (calculated_y + y_variable)in range(0, 8):            
                                        if df.at[calculated_x, calculated_y + y_variable] == "0":
                                            print("znaleziony69")
                                            mf.at[calculated_x, calculated_y + y_variable] == "9"
                                            break
                                        
                                    
                                elif calculated_y == 0:
                                    print("elif")
                                    print(calculated_x, calculated_y)
                                    mf.at[calculated_x, calculated_y] = "1"
                                    break
                                else:
                                    break
                                
                                
                            elif x!=0: 
                                print("x!=0")
                                if df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                    mf.at[calculated_x, calculated_y] = "1"
                                    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                                    break


                                if (calculated_x + x_variable) in range(0,8) :
                                    print("hhhhhhhhh")      
                                    if df.at[calculated_x + x_variable, calculated_y] == "0":
                                        mf.at[calculated_x, calculated_y] = "1"
                                        if df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                            print("princik")
                                        mf.at[calculated_x + x_variable, calculated_y] = "1"
                                        print("movelist1x")
                                        print(mf)
                                        if (calculated_x + x_variable) > piece_x_coord and df.at[calculated_x + x_variable, calculated_y] == "0":
                                            x_variable+=1
                                            print("fff")
                                            if (calculated_x + x_variable) in range(0,8):
                                                if df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                                    print("DDDD")
                                                elif df.at[calculated_x + x_variable, calculated_y] == "0":
                                                    print("DDDD22")
                                                    break
                                        elif (calculated_x + x_variable) < piece_x_coord and df.at[calculated_x + x_variable, calculated_y] == "0":
                                            x_variable -= 1
                                            print("ffff") 
                                        if (calculated_x + x_variable) not in range(0, 8):                                      
                                            print("www2")
                                            calculated_x = 0
                                            calculated_y = 0
                                            break


                                    elif df.at[calculated_x, calculated_y] == "0" and calculated_x in range(0, 8):
                                        if df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                            print("znaleziony99")
                                        print("mmmmmmmm")
                                        mf.at[calculated_x, calculated_y] = "1"
                                        # print('HHHe muje2')
                                        print("movelist0x")
                                        print(mf)
                                        if calculated_x in range(0,8):
                                            print("kkkkkkkkk")
                                            print(calculated_x, calculated_y)
                                        if (calculated_x + x_variable) > piece_x_coord:
                                            print("ggg")
                                            if (calculated_x + x_variable) in range(0,8):
                                                if df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                                    print("HHH")
                                                    mf.at[calculated_x + x_variable, calculated_y] = "1"
                                                elif df.at[calculated_x + x_variable, calculated_y] == "0":
                                                    print("HHH22")
                                                    break
                                            x_variable+=1
                                            
                                            
                                        elif (calculated_x + x_variable) < piece_x_coord:
                                            print(calculated_x + x_variable, calculated_y)
                                            if (calculated_x + x_variable) in range(0,8):
                                                print(calculated_x + x_variable, calculated_y)
                                                if df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                                    print("HHHkkk")
                                                    mf.at[calculated_x + x_variable, calculated_y] = "1"
                                                elif df.at[calculated_x + x_variable, calculated_y] == "0":
                                                    print("HHH22")
                                                    break
                                            print("gggg")
                                            x_variable -= 1
                                            if (calculated_x + x_variable) in range(0,8):
                                                print(calculated_x + x_variable, calculated_y)
                                                if df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_pawn") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_rook") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_knight") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_bishop") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_king") or df.at[calculated_x + x_variable, calculated_y] == getattr(pieces_class.Pieces(), f"{next_turn}_queen"):
                                                    mf.at[calculated_x + x_variable, calculated_y] = "1"
                                                    print("HHH")
                                                elif df.at[calculated_x + x_variable, calculated_y] == "0":
                                                    print("HHH222")
                                                    mf.at[calculated_x + x_variable, calculated_y] == "1"
                                                    break
                                            
                
                                        if (calculated_x + x_variable) not in range(0, 8):
                                            next_move
                                            print("www156")
                                            calculated_x = 0
                                            calculated_y = 0
                                            break    
                                        
                                        
                                    elif (calculated_x + x_variable)in range(0, 8):
                                        if df.at[calculated_x + x_variable, calculated_y] == "0":
                                            print("znaleziony2137")
                                            mf.at[calculated_x + x_variable, calculated_y] == "9"
                                            break
                                        
                                        
                                elif calculated_x == 0:
                                    print("elifffff")
                                    print(calculated_x, calculated_y)
                                    mf.at[calculated_x, calculated_y] = "1"
                                    break
                                else:
                                    break
                                
                        print(mf)
                        print("movelist2")
                    else:
                        print("movelist3")
                        print(mf)

                print(" NIE DZIALA if calculated_y in range(0, 8) and calculated_x in range(0, 8):")
                if i==3:
                    print(mf)
                    if mf.at[field_x_coord,field_y_coord] == "1":
                        df.at[field_x_coord,field_y_coord] = df.at[piece_x_coord, piece_y_coord]
                        df.at[piece_x_coord, piece_y_coord] = "0"
                        print("rooki")
                        print(mf)
                        print(df)
                        
                        MOVE="SELECT_PIECE"
                        TURN = next_turn

    
    
df = pandas.DataFrame(pieces_class.Pieces().starting_chess_board_data)
mf = pandas.DataFrame(pieces_class.Pieces().move_chess_board_data)
print("wybierz figure")
print(df)


# game loop
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
                pieces.pieces_location(df, TURN, piece_x_coord, piece_y_coord, field_x_coord, field_y_coord)  
        
    screen.blit(chess_board, (0, 0))
    pieces.pieces_draw(screen)
    pygame.display.update()