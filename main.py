import pygame
import os
import time

# инициализация Pygame
pygame.init()

# ждем 60 сек
time.sleep(2)

# скрываем все окна
os.system('powershell -command "(New-Object -ComObject Shell.Application).MinimizeAll()"')

# задаем название окна
pygame.display.set_caption("My Image with Sound")

# загружаем изображение и звуковой файл
image = pygame.image.load("image.jpg")
sound = pygame.mixer.Sound("sound.mp3")

# открываем окно с изображением
screen = pygame.display.set_mode(image.get_rect().size)
screen.blit(image, (0, 0))
pygame.display.flip()

# воспроизводим звук
sound.play()

# ждем, пока звук не закончится
while pygame.mixer.get_busy():
    pygame.time.wait(100)

time.sleep(5)

# закрываем Pygame
pygame.quit()