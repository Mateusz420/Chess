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

    starting_chess_board_data = {"g": [black_rook, black_pawn, "0", "0", "0", "0", white_pawn, white_rook],
                                 1: [black_knight, black_pawn, "0", "0", "0", "0", white_pawn, white_knight],
                                 2: [black_bishop, black_pawn, "0", "0", "0", "0", white_pawn, white_bishop],
                                 3: [black_king, black_pawn, "0", "0", "0", "0", white_pawn, white_king],
                                 4: [black_queen, black_pawn, "0", "0", "0", "0", white_pawn, white_queen],
                                 5: [black_bishop, black_pawn, "0", "0", "0", "0", white_pawn, white_bishop],
                                 6: [black_knight, black_pawn, "0", "0", "0", "0", white_pawn, white_knight],
                                 7: [black_rook, black_pawn, "0", "0", "0", "0", white_pawn, white_rook]}

    def pieces_draw(self, screen):
        for i in range(8):
            screen.blit(self.white_pawn, ((0 + (i * 105)), 630))
            screen.blit(self.black_pawn, ((0 + (i * 105)), 105))

        for i in range(2):
            screen.blit(self.white_rook, ((0 + (i * (105 * 7))), 735))
            screen.blit(self.black_rook, ((0 + (i * (105 * 7))), 0))

        for i in range(2):
            screen.blit(self.white_knight, ((105 + (i * (105 * 5))), 735))
            screen.blit(self.black_knight, ((105 + (i * (105 * 5))), 0))

        for i in range(2):
            screen.blit(self.white_bishop, ((210 + (i * (105 * 3))), 735))
            screen.blit(self.black_bishop, ((210 + (i * (105 * 3))), 0))

        screen.blit(self.white_queen, (315, 735))
        screen.blit(self.black_queen, (315, 0))
        screen.blit(self.white_king, (420, 735))
        screen.blit(self.black_king, (420, 0))

    # white = [[white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn],
    # [white_rook, white_knight, white_bishop, white_king, white_queen, white_bishop, white_knight, white_rook]]
    # black = [[black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],
    # [black_rook, black_knight, black_bishop, black_king, black_queen, black_bishop, black_knight, black_rook]]
