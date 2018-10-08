import cv2

class WebCam:
    def __init__(self, image_file):
        self.image_file = image_file


    def start(self):
        pass

    def stop(self):
        pass

    def get_image(self):
        print("taking picture")

        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FPS, 10)

        ret, frame = self.cam.read()
        cv2.imwrite(self.image_file, frame)

        self.cam.release()
