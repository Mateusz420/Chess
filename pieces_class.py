import pandas
import pygame


class Pieces:
    black_pawn = pygame.image.load("pieces\\black_pawn.png")
    black_rook = pygame.image.load("pieces\\black_rook.png")
    black_knight = pygame.image.load("pieces\\black_knight.png")
    black_bishop = pygame.image.load("pieces\\black_bishop.png")
    black_king = pygame.image.load("pieces\\black_king.png")
    black_queen = pygame.image.load("pieces\\black_queen.png")
    white_pawn = pygame.image.load("pieces\\white_pawn.png")
    white_rook = pygame.image.load("pieces\\white_rook.png")
    white_knight = pygame.image.load("pieces\\white_knight.png")
    white_bishop = pygame.image.load("pieces\\white_bishop.png")
    white_king = pygame.image.load("pieces\\white_king.png")
    white_queen = pygame.image.load("pieces\\white_queen.png")
    
    white = [[(0, 630), (105, 630), (210, 630), (315, 630), (420, 630), (525, 630), (630, 630), (735, 630)],
             [(0, 735), (105, 735), (210, 735), (315, 735), (420, 735), (525, 735), (630, 735), (735, 735)]]
    black = [[(0, 105), (105, 105), (210, 105), (315, 105), (420, 105), (525, 105), (630, 105), (735, 105)],
             [(0, 0), (105, 0), (210, 0), (315, 0), (420, 0), (525, 0), (630, 0), (735, 0)]]
    promoted_white = []
    promoted_black = []

    starting_chess_board_data = {0: [black_rook, black_pawn, "0", "0", "0", "0", white_pawn, white_rook],
                                 1: [black_knight, black_pawn, "0", "0", "0", "0", white_pawn, white_knight],
                                 2: [black_bishop, black_pawn, "0", "0", "0", "0", white_pawn, white_bishop],
                                 3: [black_queen, black_pawn, "0", "0", "0", "0", white_pawn, white_queen],
                                 4: [black_king, black_pawn, "0", "0", "0", "0", white_pawn, white_king],
                                 5: [black_bishop, black_pawn, "0", "0", "0", "0", white_pawn, white_bishop],
                                 6: [black_knight, black_pawn, "0", "0", "0", "0", white_pawn, white_knight],
                                 7: [black_rook, black_pawn, "0", "0", "0", "0", white_pawn, white_rook]}
    
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

        if len(self.promoted_white) != 0:
            for i in range(len(self.promoted_white)):
                screen.blit(self.white_queen, self.promoted_white[i])
        if len(self.promoted_black) != 0:
            for i in range(len(self.promoted_black)):
                screen.blit(self.black_queen, self.promoted_black[i])

    def pieces_location(self, df, TURN, piece_x_coord, piece_y_coord, field_x_coord, field_y_coord):
        
        # White Pieces
        if df.at[piece_x_coord, piece_y_coord] == "0":
            for i in range(2):
                for j in range(8):
                    if (piece_y_coord * 105, piece_x_coord * 105) == self.white[i][j] and ((field_y_coord * 105, field_x_coord * 105) in self.black[0] or (field_y_coord * 105, field_x_coord * 105) in self.black[1]):
                        for x in range(2):
                            for y in range(8):
                                if (field_y_coord * 105, field_x_coord * 105) == self.black[x][y]:
                                    self.black[x][y] = (1000, 1000)
                                    self.white[i][j] = (field_y_coord * 105, field_x_coord * 105)
                    elif (piece_y_coord * 105, piece_x_coord * 105) == self.white[i][j] and df.at[field_x_coord, field_y_coord] != "0" and (field_y_coord * 105, field_x_coord * 105) not in self.white[0] and (field_y_coord * 105, field_x_coord * 105) not in self.white[1]:
                        self.white[i][j] = (field_y_coord * 105, field_x_coord * 105)
        
        # Black Pieces
        if df.at[piece_x_coord, piece_y_coord] == "0":
            for i in range(2):
                for j in range(8):
                    if (piece_y_coord * 105, piece_x_coord * 105) == self.black[i][j] and ((field_y_coord * 105, field_x_coord * 105) in self.white[0] or (field_y_coord * 105, field_x_coord * 105) in self.white[1]):
                        for x in range(2):
                            for y in range(8):
                                if (field_y_coord * 105, field_x_coord * 105) == self.white[x][y]:
                                    self.white[x][y] = (1000, 1000)
                                    self.black[i][j] = (field_y_coord * 105, field_x_coord * 105)
                    elif (piece_y_coord * 105, piece_x_coord * 105) == self.black[i][j] and df.at[field_x_coord, field_y_coord] != "0" and (field_y_coord * 105, field_x_coord * 105) not in self.black[0] and (field_y_coord * 105, field_x_coord * 105) not in self.black[1]:
                        self.black[i][j] = (field_y_coord * 105, field_x_coord * 105)
