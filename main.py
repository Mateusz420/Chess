import pandas
import pygame
import pieces_class

pygame.init()
clock = pygame.time.Clock()

# Setting up the screen
screen = pygame.display.set_mode((840, 840))
chess_board = pygame.image.load("chess\\chess_board.png")

# Splitting the chess board into squares
board_x = 0
board_y = 0
all_tiles = []
tiles = []
rows = []

for i in range(9):
    for j in range(8):
        if j != 7:
            rect = pygame.Rect(board_x, board_y, 105, 105)
            board_x += 105
            all_tiles.append(rect)
        else:
            rect = pygame.Rect(board_x, board_y, 105, 105)
            board_x = 0
            board_y += 105
            all_tiles.append(rect)

for i in range(len(all_tiles)):
    if i % 8 == 0 and i != 0:
        tiles.append(rows)
        rows = [all_tiles[i]]
    else:
        rows.append(all_tiles[i])

icon = pygame.image.load("chess\\pieces\\black_pawn.png")
pygame.display.set_caption("Chess")
pygame.display.set_icon(icon)

pieces = pieces_class.Pieces()

# current piece and coords
global current_piece
current_piece = ""
# print(current_piece)
global current_x_coord
current_x_coord = ""
# print(current_x_coord)
global current_y_coord
current_y_coord = ""
# print(current_y_coord)


df = pandas.DataFrame(pieces_class.Pieces().starting_chess_board_data)
print("wybierz figure")
print(df)


def piece_move(x_coord, y_coord):
    # global init
    global current_piece
    global current_x_coord
    global current_y_coord

    if current_piece == "":
        current_piece = df.at[x_coord, y_coord]
        current_x_coord = x_coord
        current_y_coord = y_coord
        # print(current_piece)
        # print(current_x_coord)
        # print(current_y_coord)
        print("wybierz pole")

    # elif current_piece != "":

    # df.at[x_coord, y_coord] = current_piece

    # with contextlib.suppress(TypeError):
    # screen.blit((current_piece), (450, 450))
    # screen.blit((pieces_class.Pieces().blue_field), (200, 200))

    # pygame.display.update()
    # current_piece = ""
    # df.at[current_x_coord, current_y_coord] = "0"
    # print("wybierz figure")


# events
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[1] // 105
            # print(x_coord)
            y_coord = event.pos[0] // 105
            # print(y_coord)
            click_coords = [x_coord, y_coord]
            print(click_coords)
            piece_move(x_coord, y_coord)
            print(df)

        pieces.pieces_move(event, tiles)

        screen.blit(chess_board, (0, 0))
        pieces.pieces_draw(screen)
        pygame.display.update()
