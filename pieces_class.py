import pandas
import pygame


class Pieces:
    black_pawn = pygame.image.load("chess\\pieces\\black_pawn.png")
    black_rook = pygame.image.load("chess\\pieces\\black_rook.png")
    black_knight = pygame.image.load("chess\\pieces\\black_knight.png")
    black_bishop = pygame.image.load("chess\\pieces\\black_bishop.png")
    black_king = pygame.image.load("chess\\pieces\\black_king.png")
    black_queen = pygame.image.load("chess\\pieces\\black_queen.png")
    white_pawn = pygame.image.load("chess\\pieces\\white_pawn.png")
    white_rook = pygame.image.load("chess\\pieces\\white_rook.png")
    white_knight = pygame.image.load("chess\\pieces\\white_knight.png")
    white_bishop = pygame.image.load("chess\\pieces\\white_bishop.png")
    white_king = pygame.image.load("chess\\pieces\\white_king.png")
    white_queen = pygame.image.load("chess\\pieces\\white_queen.png")
    # Used to change the pieces coordinates
    held_piece = None
    piece_type = None
    piece_color = None

    white = [[(0, 630), (105, 630), (210, 630), (315, 630), (420, 630), (525, 630), (630, 630), (735, 630)],
             [(0, 735), (105, 735), (210, 735), (315, 735), (420, 735), (525, 735), (630, 735), (735, 735)]]
    black = [[(0, 105), (105, 105), (210, 105), (315, 105), (420, 105), (525, 105), (630, 105), (735, 105)],
             [(0, 0), (105, 0), (210, 0), (315, 0), (420, 0), (525, 0), (630, 0), (735, 0)]]

    starting_chess_board_data = {0: [white_rook, white_pawn, "0", "0", "0", "0", black_pawn, black_rook],
                                 1: [white_knight, white_pawn, "0", "0", "0", "0", black_pawn, black_knight],
                                 2: [white_bishop, white_pawn, "0", "0", "0", "0", black_pawn, black_bishop],
                                 3: [white_king, white_pawn, "0", "0", "0", "0", black_pawn, black_king],
                                 4: [white_queen, white_pawn, "0", "0", "0", "0", black_pawn, black_queen],
                                 5: [white_bishop, white_pawn, "0", "0", "0", "0", black_pawn, black_bishop],
                                 6: [white_knight, white_pawn, "0", "0", "0", "0", black_pawn, black_knight],
                                 7: [white_rook, white_pawn, "0", "0", "0", "0", black_pawn, black_rook]}

    def pieces_draw(self, screen):
        for i in range(8):
            screen.blit(self.white_pawn, self.white[0][i])
            screen.blit(self.black_pawn, self.black[0][i])

        for i in range(0, 8, 7):
            screen.blit(self.white_rook, self.white[1][i])
            screen.blit(self.black_rook, self.black[1][i])

        for i in range(1, 7, 5):
            screen.blit(self.white_knight, self.white[1][i])
            screen.blit(self.black_knight, self.black[1][i])

        for i in range(2, 6, 3):
            screen.blit(self.white_bishop, self.white[1][i])
            screen.blit(self.black_bishop, self.black[1][i])

        screen.blit(self.white_queen, self.white[1][3])
        screen.blit(self.white_king, self.white[1][4])
        screen.blit(self.black_queen, self.black[1][3])
        screen.blit(self.black_king, self.black[1][4])

    def piece_type_check(self, i, j):
        if i == 0:
            self.piece_type = "pawn"
        elif j == 0 or j == 7:
            self.piece_type = "rook"
        elif j == 1 or j == 6:
            self.piece_type = "knight"
        elif j == 2 or j == 5:
            self.piece_type = "bishop"
        elif j == 3:
            self.piece_type = "queen"
        elif j == 4:
            self.piece_type = "king"

    # Defines pieces movements and (if the move is valid) changes the piece's position
    def pieces_movement_restrictions(self, clicked_tile, tiles, i, j):
        if self.piece_type == "pawn":
            if self.piece_color == "white":
                # Capturing pieces
                if clicked_tile in self.black[:][0] or clicked_tile in self.black[:][1]:
                    for x in range(2):
                        for y in range(8):
                            if self.held_piece[1] - 105 == self.black[x][y] and clicked_tile[0] == self.held_piece[0] + 105 or clicked_tile[0] == self.held_piece[0] - 105:
                                # self.black[x][y] = (1000, 1000)
                                self.white[i][j] = clicked_tile
                            elif self.held_piece[1] - 105 == self.black[x][y]:
                                break

                # Restriction of movement
                elif self.held_piece[1] == 630 and (self.held_piece[1] >= clicked_tile[1] >= (self.held_piece[1] - 210)) and (clicked_tile[0] == self.held_piece[0]):
                    self.white[i][j] = clicked_tile
                elif self.held_piece[1] >= clicked_tile[1] >= (self.held_piece[1] - 105) and (clicked_tile[0] == self.held_piece[0]):
                    self.white[i][j] = clicked_tile

            elif self.piece_color == "black":
                # Restriction of movement
                if self.held_piece[1] == 105 and (clicked_tile[1] <= self.held_piece[1] + 210) and (clicked_tile[0] == self.held_piece[0]):
                    self.black[i][j] = clicked_tile
                elif clicked_tile[1] <= self.held_piece[1] + 105 and (clicked_tile[0] == self.held_piece[0]):
                    self.black[i][j] = clicked_tile

        # Placeholder
        else:
            if self.piece_color == "white":
                self.white[i][j] = clicked_tile
            elif self.piece_color == "black":
                self.black[i][j] = clicked_tile

    def collision_check(self, clicked_tile):
        for i in self.white:
            for j in range(8):
                if (self.piece_color == "white") and (clicked_tile == i[j]):
                    return 1
        for i in self.black:
            for j in range(8):
                if (self.piece_color == "black") and (clicked_tile == i[j]):
                    return 1

    def pieces_move(self, event, tiles):
        # Gets the event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_pos, y_pos = pygame.mouse.get_pos()
            clicked_tile = (x_pos, y_pos)

            # Finds the location of the square that the user has clicked on
            for i in range(8):
                for j in range(8):
                    if j != 7 and i != 7:
                        if (tiles[i][j].x <= x_pos <= tiles[i][j + 1].x) and (
                                tiles[i][j].y <= y_pos <= tiles[i + 1][j].y):
                            x_pos = tiles[i][j].x
                            y_pos = tiles[i][j].y
                            clicked_tile = (x_pos, y_pos)
                    elif j == 7 and i != 7:
                        if (tiles[i][j].x <= x_pos) and (tiles[i][j].y <= y_pos <= tiles[i + 1][j].y):
                            x_pos = tiles[i][j].x
                            y_pos = tiles[i][j].y
                            clicked_tile = (x_pos, y_pos)
                    elif i == 7 and j != 7:
                        if (tiles[i][j].x <= x_pos <= tiles[i][j + 1].x) and (tiles[i][j].y <= y_pos):
                            x_pos = tiles[i][j].x
                            y_pos = tiles[i][j].y
                            clicked_tile = (x_pos, y_pos)
                    elif i == 7 and j == 7:
                        if (tiles[i][j].x <= x_pos) and (tiles[i][j].y <= y_pos):
                            x_pos = tiles[i][j].x
                            y_pos = tiles[i][j].y
                            clicked_tile = (x_pos, y_pos)

            # Checks if the user is currently holding a piece and what piece is it
            if self.held_piece is None:
                for i in range(2):
                    for j in range(8):
                        if clicked_tile == self.white[i][j]:
                            self.held_piece = self.white[i][j]
                            self.piece_color = "white"
                            self.piece_type_check(i, j)
                for i in range(2):
                    for j in range(8):
                        if clicked_tile == self.black[i][j]:
                            self.held_piece = self.black[i][j]
                            self.piece_color = "black"
                            self.piece_type_check(i, j)

            elif self.held_piece is not None:
                if self.piece_color == "white":
                    for i in range(2):
                        for j in range(8):
                            if self.held_piece == self.white[i][j]:
                                if self.collision_check(clicked_tile) == 1:
                                    break
                                self.pieces_movement_restrictions(clicked_tile, tiles, i, j)

                elif self.piece_color == "black":
                    for i in range(2):
                        for j in range(8):
                            if self.held_piece == self.black[i][j]:
                                if self.collision_check(clicked_tile) == 1:
                                    break
                                self.pieces_movement_restrictions(clicked_tile, tiles, i, j)
                self.held_piece = None
                self.piece_type = None
                self.piece_color = None



