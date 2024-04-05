import pygame
pygame.mixer.init()

pygame.init()
screen = pygame.display.set_mode((480, 248))

songs = ["TV Girl - Cigarettes out the Window.mp3","TV Girl - lover's rock.mp3","TV Girl - Not Allowed.mp3"]
current_music = 0
pygame.mixer.music.load(songs[current_music])
pygame.mixer.music.play()
background = pygame.image.load("player.png")
background_rect = background.get_rect()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(songs)
                pygame.mixer.music.load(songs[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(songs)
                pygame.mixer.music.load(songs[current_music])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    pygame.display.flip()
pygame.quit()