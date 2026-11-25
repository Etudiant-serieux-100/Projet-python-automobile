WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

CAR_ACCELERATION = 0.1
CAR_WIDTH = 30
CAR_HEIGHT = 50
STREER_SPEED_RATIO = 5  # Ratio de vitesse pour ajuster la vitesse de rotation en fonction de la vitesse de la voiture


class GameState:
    MENU = "menu"
    RACING = "racing"


# --- Couleurs UI ---
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)

# --- Terrains ---
"""Paramètres des terrains : 
 - vitesse de rotation (a quel vitesse l'angle de la voiture s'ajuste à l'angle de braquage)
 - adherence en derapage (a quel vitesse l'angle de la vitesse s'ajuste à l'angle de la voiture en derapage)
 - friction
 - seuil de drift
 """
BITUME = (0.99, 0.50, 0.98, 150)
TERRE = (0.80, 0.40, 0.975, 200)
GLACE = (0.98, 0.20, 0.20, 2)
HERBE = (0.98, 0.70, 0.98, 1)
VIDE = (0, 0, 0, 1, 4)
MUR = (0, 0, -10, 1, 5)