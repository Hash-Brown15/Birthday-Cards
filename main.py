import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img = pygame.image.load("birthday card.jpeg")
image = pygame.transform.scale(img, (WIDTH,HEIGHT))

while(True):
    font = pygame.font.SysFont("Arial",36)
    text = font.render("Happy",True,(0,0,0))
    text2 = font.render("Birthday",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text,(210,180))
    screen.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)

    img1 = pygame.image.load("cat.jpeg")

    font1 = pygame.font.SysFont("Arial",36)
    text3 = font.render("I'm so glad that you",True,(0,0,0))
    text4 = font.render("lived another year of your life",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text3,(210,180))
    screen.blit(text4,(180,264))
    pygame.display.update()
    time.sleep(3)

    img3 = pygame.image.load("cake.jpeg")

    font3 = pygame.font.SysFont("Ariel",36)
    text5 = font.render("eat food",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text5,(210,180))
    pygame.display.update()
    time.sleep(3)

    img4 = pygame.image.load("present.png")

    font4 = pygame.font.SysFont("Arial",36)
    text6 = font.render("Dream Big Dreams",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text6,(210,180))
    pygame.display.update()
    time.sleep(3)