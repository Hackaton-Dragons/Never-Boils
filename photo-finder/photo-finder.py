
import pygame.camera
import pygame.image

def main():
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[1])
    cam.start()
    img = cam.get_image()
    pygame.image.save(img, "photo.bmp")
    pygame.camera.quit()