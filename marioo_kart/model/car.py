import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE, STREER_SPEED_RATIO
)


class Car:

    def __init__(self, start_col: int, start_row: int, start_angle: float, terrain):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.drift = 0
        self.speed_angle = start_angle
        self.angle = start_angle
        self.streering_angle: int = 0
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.terrain = terrain
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        self.speed += CAR_ACCELERATION * self.terrain[2]

    def brake(self) -> None:
        self.speed -= (CAR_ACCELERATION * self.terrain[2] * 1.5) if self.speed > 0 else CAR_ACCELERATION * self.terrain[2]  # Freinage plus efficace que l'accélération

    def turn_left(self) -> None:
        self.streering_angle = self.terrain[0] * 10

    def turn_right(self) -> None:
        self.streering_angle = -10 * self.terrain[0]

    def update_position(self) -> None:
        self.angle -= self.streering_angle * (self.speed / STREER_SPEED_RATIO)  # Ajuster la vitesse de rotation en fonction de la vitesse
        # self.speed_angle += (-1 + math.exp(abs(self.angle - self.speed_angle))) * (1 if self.speed_angle < self.angle else -1)
        #self.speed_angle += math.log(1 + abs(self.angle - self.speed_angle)) * (1 if self.speed_angle < self.angle else -1)
        
        if (self.drift > 0):
            self.speed_angle = (self.speed_angle + (50/self.drift) * self.terrain[1] * (self.angle - self.speed_angle)) # Ajuster la différence d'angle pour simuler le drift
        else:
            self.speed_angle = self.angle  

        self.x += self.speed * math.cos(math.radians(self.speed_angle))
        self.y += self.speed * math.sin(math.radians(self.speed_angle))
        
        self.speed *= self.terrain[2]  # La voiture ralentit naturellement avec le temps (friction)
        
        #self.angle %= 360  # L'angle reste dans la plage [0, 360), pour qu'il ne monte pas à l'infini
        #self.speed_angle %= 360  # L'angle reste dans la plage [0, 360), pour qu'il ne monte pas à l'infini
        
        self.streering_angle = 0  # Réinitialiser l'angle de braquage après chaque mise à jour
        self.drift = -300 + self.speed * self.terrain[3]  # Déterminer du degré de drift en fonction de la vitesse et du seuil de drift du terrain

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
