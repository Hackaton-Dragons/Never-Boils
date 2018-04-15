import pygame.camera
import pygame.image

class Camera:
    def __init__(self, image_file="images/photo.png"):
        pygame.camera.init()
        self.image_file = image_file
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[1])
        self.start()

    def start(self):
        self.cam.start()

    def stop(self):
        pygame.camera.quit()

    def get_image():
        img = cam.get_image()
        pygame.image.save(img, self.image_file)
