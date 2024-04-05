import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
done = False
is_blue = True
x = 400
y = 400
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
           if y > 25: y -= 2
        if pressed[pygame.K_DOWN]: 
            if y < 775: y += 2
        if pressed[pygame.K_LEFT]: 
            if x > 25:
                x -= 2
        if pressed[pygame.K_RIGHT]:
            if x < 975:
                x += 2
        
        color = (255, 0, 0)
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (x, y), 25)
        

        pygame.display.flip()
        
        
