import pygame

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(500, 50, 50, 50)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)


class Board(object):
    level = [
        "WWWWWWWWWWWWWWW",
        "W             W",
        "W W W W W W W W",
        "W             W",
        "W W W W W W W W",
        "W             W",
        "W W W W W W W W",
        "W             W",
        "W W W W W W W W",
        "W             W",
        "W W W W W W W W",
        "W             W",
        "W W W W W W W W",
        "W             W",
        "WWWWWWWWWWWWWWW",
    ]

    def __init__(self):
        x = 450
        y = 0
        for row in self.level:
            for col in row:
                if col == "W":
                    Wall((x, y))
                x += 50
            y += 50
            x = 450


walls = []  # List to hold the walls


def Buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)

def main():

    x_button_exit, y_button_exit = 200,600
    x_button_menu, y_button_menu = 400,600

    # Initialise pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1200, 750))


    clock = pygame.time.Clock()
    player = Player()  # Create the player
    board = Board();

    varial = False

    running = True
    while running:

        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mouse = pygame.mouse.get_pos()
                if y_button_exit<= mouse[1] <= y_button_exit+50 and x_button_exit-100<=mouse[0]<=x_button_exit:
                    running = False
                if y_button_menu<= mouse[1] <= y_button_menu+50 and x_button_menu-100<=mouse[0]<=x_button_menu:
                    varial = True


        # Obsluga przyciskow
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)



        # Wyświetlenie tła, ścian, zawodnika
        screen.fill((255, 255, 255))
        for wall in walls:
            pygame.draw.rect(screen, (0, 0, 0), wall.rect)
            if(varial):
                pygame.draw.rect(screen, (255, 200, 0), player.rect)

        Image = Buttonify('exit.png', (x_button_exit,y_button_exit), screen)
        Imagelol = Buttonify('menu.png', (x_button_menu,y_button_menu), screen)



        pygame.display.flip()


if __name__ == "__main__":
    main()