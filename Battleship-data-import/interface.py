import pygame
from config import *
from Engine import Game as game

def draw_center_labels(SCREEN, player1, player2, label_font, vs_font):
    name1_text = f"{player1.name}: {player1.strategy_name}"
    name2_text = f"{player2.name}: {player2.strategy_name}"
    name1_surf = label_font.render(name1_text, True, WHITE)
    name2_surf = label_font.render(name2_text, True, WHITE)
    vs_surf = vs_font.render("VS", True, RED)

    name1_rect = name1_surf.get_rect(center=((SQ_SIZE * 10) // 2, HEIGHT // 2))
    name2_rect = name2_surf.get_rect(center=(WIDTH - (SQ_SIZE * 10) // 2, HEIGHT // 2))
    vs_rect = vs_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    SCREEN.blit(name1_surf, name1_rect)
    SCREEN.blit(name2_surf, name2_rect)
    SCREEN.blit(vs_surf, vs_rect)

def draw_grid(SCREEN, player, left, top, search=False):
    
    for i in range(100):
        x = left + i % 10 * SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width=3)
        if search:
            center = (x + SQ_SIZE // 2, y + SQ_SIZE // 2)
            pygame.draw.circle(SCREEN, COLORS[player.search[i]], center, radius=SQ_SIZE // 4)

def draw_next_move(SCREEN, controller, game):
    index = controller.next_move
    if index is None: return

    col = index % 10
    row = index // 10

    left = 0 if game.player1_turn else (WIDTH - H_MARGIN) // 2 + H_MARGIN
    top = 0 if game.player1_turn else (HEIGHT - V_MARGIN) // 2 + V_MARGIN

    x = left + col * SQ_SIZE
    y = top + row * SQ_SIZE

    rect = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
    pygame.draw.rect(SCREEN, RED, rect, width=7)

def draw_ships(SCREEN, player, left=0, top=0):
    for ship in player.ships:
        x = left + ship.col * SQ_SIZE + INDENT
        y = top + ship.row * SQ_SIZE + INDENT
        w = (ship.size * SQ_SIZE - 2 * INDENT) if ship.orientation == "h" else SQ_SIZE - 2 * INDENT
        h = SQ_SIZE - 2 * INDENT if ship.orientation == "h" else (ship.size * SQ_SIZE - 2 * INDENT)
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(SCREEN, GREEN, rect, border_radius=15)
