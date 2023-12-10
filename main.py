import pygame
import pieces_class


def main():
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
                board_y -= 105
                all_tiles.append(rect)

    for i in range(len(all_tiles)):
        if i % 8 == 0 and i != 0:
            tiles.append(rows)
            rows = [all_tiles[i]]
        else:
            rows.append(all_tiles[i])

    # test
    for i in tiles:
        print(i)

    icon = pygame.image.load("pieces\\black_pawn.png")
    pygame.display.set_caption("Chess")
    pygame.display.set_icon(icon)

    pieces = pieces_class.Pieces()

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(chess_board, (0, 0))
        pieces.pieces_draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
