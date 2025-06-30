import tkinter as tk
from tkinter import messagebox, simpledialog
import pygame
from config import *
from simulation import simulation

# Ask for game mode
root = tk.Tk()
root.withdraw()
mostrar_tela = messagebox.askquestion("Modo de Simulação", "Deseja exibir visualmente a simulação?") == 'yes'
num_simulacoes = simpledialog.askinteger("Número de Simulações", "Quantas simulações deseja rodar?", minvalue=1)
if num_simulacoes is None:
    exit()
# Pygame setup
fonts = None
SCREEN = None
if mostrar_tela:
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Battleship")
    font = pygame.font.SysFont("fresansttf", 70)
    label_font = pygame.font.SysFont("fresansttf", 36)
    vs_font = pygame.font.SysFont("fresansttf", 60)
    fonts = (font, label_font, vs_font)

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


estatisticas = simulation(num_simulacoes, mostrar_tela, SCREEN, fonts)

# Mostra resultados
print("\nEstatísticas de estratégias:")
for estrategia, vitorias in estatisticas.items():
    print(f"{estrategia}: {vitorias} vitórias")

if mostrar_tela:
    pygame.quit()
