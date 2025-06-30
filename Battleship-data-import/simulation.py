import pygame
from Engine import Game, PlayerController
from config import *
from interface import draw_center_labels, draw_grid, draw_next_move, draw_ships

def game_simulation(mostrar_tela, SCREEN=None, fonts=None):
    game = Game()
    controller = PlayerController(game)
    last_move_time = pygame.time.get_ticks()

    if mostrar_tela:
        font, label_font, vs_font = fonts

    print(f"Player 1: {game.player1.name} usando estratégia {game.player1.strategy_name}")
    print(f"Player 2: {game.player2.name} usando estratégia {game.player2.strategy_name}")

    while not game.over:
        now = pygame.time.get_ticks()
        if mostrar_tela:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        if controller.next_move is None:
            controller.player_turn()

        if now - last_move_time >= (50 if mostrar_tela else 1):
            if controller.next_move is not None:
                game.make_move(controller.next_move)
                controller.next_move = None
                last_move_time = now

        if mostrar_tela:
            SCREEN.fill(GREY)
            draw_center_labels(SCREEN, game.player1, game.player2, label_font, vs_font)
            draw_next_move(SCREEN, controller, game)
            # Search grid
            draw_grid(SCREEN, game.player1, 0, 0, search=True)
            draw_grid(SCREEN, game.player2, ((WIDTH - H_MARGIN) // 2 + H_MARGIN), ((HEIGHT - V_MARGIN) // 2 + V_MARGIN), search=True)
            # Game grid
            draw_grid(SCREEN, game.player1, 0, ((HEIGHT - V_MARGIN) // 2 + V_MARGIN))
            draw_grid(SCREEN, game.player2, ((WIDTH - H_MARGIN) // 2 + H_MARGIN), 0)
            # Ships
            draw_ships(SCREEN, game.player1, top=((HEIGHT - V_MARGIN) // 2 + V_MARGIN))
            draw_ships(SCREEN, game.player2, left=((WIDTH - H_MARGIN) // 2 + H_MARGIN))

            if game.over:
                msg = f"{game.result} wins!"
                txt = font.render(msg, False, GREY, WHITE)
                SCREEN.blit(txt, (WIDTH // 2 - 230, HEIGHT // 2 - 50))
            pygame.display.flip()
        else:
            pygame.time.wait(1)

    vencedor = game.result
    print(f"{vencedor} ganhou!")
    return game.player1.strategy_name if vencedor == game.player1.name else (
           game.player2.strategy_name if vencedor == game.player2.name else "Desconhecida")

def simulation(n, mostrar_tela, SCREEN=None, fonts=None):
    resultados = {}
    for i in range(n):
        print(f"Simulação {i+1}")
        estrategia = game_simulation(mostrar_tela, SCREEN, fonts)
        resultados[estrategia] = resultados.get(estrategia, 0) + 1
        if mostrar_tela:
            pygame.time.wait(1000)
    return resultados
