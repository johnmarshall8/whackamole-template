import pygame
import random




GRID_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 16
SCREEN_WIDTH = GRID_WIDTH * GRID_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * GRID_SIZE


def main():
    try:
        pygame.init()


        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (GRID_SIZE, GRID_SIZE))


        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()


        mole_x, mole_y = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole is clicked
                    mouse_x, mouse_y = event.pos
                    if (mole_x <= mouse_x < mole_x + GRID_SIZE) and (mole_y <= mouse_y < mole_y + GRID_SIZE):
                        # Move the mole to a new random position in the grid
                        mole_x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
                        mole_y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE


            screen.fill("light green")


            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))


            screen.blit(mole_image, (mole_x, mole_y))


            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
