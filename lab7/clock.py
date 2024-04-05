import pygame
import datetime
import math

pygame.init()
screen = pygame.display.set_mode((1000, 800))
done = False
clock = pygame.time.Clock()

clock_image = pygame.image.load('C:/Users/Хима/labs/lab7/clockjpeg.jpg')
minutes_hand_image = pygame.image.load('C:/Users/Хима/labs/lab7/rightarm.png')
seconds_hand_image = pygame.image.load('C:/Users/Хима/labs/lab7/leftarm.png')


clock_rect = clock_image.get_rect(center=(500, 400))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    current_time = datetime.datetime.now().time()
    sec_angle = -(current_time.second * 6)
    min_angle = -((current_time.minute + current_time.second/60) * 6)
    
    screen.fill((255, 255, 255))
    
    screen.blit(clock_image, clock_rect)
    
    center_x, center_y = clock_rect.center
    seconds_hand_length = 250
    minutes_hand_length = 170
    
    sec_rotated = pygame.transform.rotate(seconds_hand_image, sec_angle)
    min_rotated = pygame.transform.rotate(minutes_hand_image, min_angle)
    
    sec_rect = sec_rotated.get_rect()
    min_rect = min_rotated.get_rect()
    
    sec_rect.center = (center_x, center_y)
    min_rect.center = (center_x, center_y)
    
    screen.blit(sec_rotated, sec_rect)
    screen.blit(min_rotated, min_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
