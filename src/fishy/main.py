#!/usr/bin/env python3
import random
import sys

import pygame


def get_rgb_color(color_str: str) -> tuple[int, int, int]:
    if color_str == "white":
        return (255, 255, 255)
    elif color_str == "black":
        return (0, 0, 0)
    elif color_str == "red":
        return (255, 0, 0)
    else:
        raise Exception("Unknown color!")


class User:
    def __init__(self, x: int, y: int, lives: int) -> None:
        self.x = x
        self.y = y
        self.size = 20
        self.lives = lives

    def move_left(self) -> None:
        self.x = self.x - 3

    def move_right(self) -> None:
        self.x = self.x + 3

    def move_up(self) -> None:
        self.y = self.y - 3

    def move_down(self) -> None:
        self.y = self.y + 3

    def grow(self) -> None:
        self.size = self.size * 1.1

    def die(self):
        self.size = 20
        self.lives = self.lives - 1
        self.x = 500
        self.y = 500


class Dinner:
    def __init__(self, width: int, height: int) -> None:
        self.y = random.randint(0, height)
        self.size = random.randint(4, 70)
        if random.randint(0, 1) == 1:
            self.speed = random.randint(3, 7)
            self.x = 0
        else:
            self.speed = random.randint(3, 7) * -1
            self.x = width

    def move(self) -> None:
        self.x = self.x + self.speed

    def reset(self, width: int, height: int) -> None:
        print("I need to add code here to reset")


def is_colliding(*, x1: int, y1: int, size1: int, x2: int, y2: int, size2: int) -> bool:
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if distance > size1 + size2:
        return False
    else:
        return True


def play_game(screen, width: int, height: int) -> None:
    # Initialize variables used in game
    keepGoing = True

    user_fish = User(width // 2, height // 2, 3)
    other_fishes = [Dinner(width, height)]

    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        # Get user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            user_fish.move_up()

        # Move characters

        # Check for collisions

        # Draw fish/food in proper position

        screen.fill(get_rgb_color("black"))
        pygame.draw.circle(screen, get_rgb_color("white"), (user_fish.x, user_fish.y), user_fish.size)

        pygame.draw.circle(screen, get_rgb_color("red"), (other_fishes[0].x, other_fishes[0].y), other_fishes[0].size)

        pygame.display.flip()
        pygame.time.delay(10)

    ## The game loop ends here.
    pygame.quit()
    sys.exit()


# Main "hook"
if __name__ == "__main__":
    print("Welcome to fishy!!! Let's get started!")
    pygame.init()

    # Set up the game window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Fishy")

    play_game(screen, width, height)
