import datetime
import os
import time
from google.cloud import vision
from google.cloud.vision import types

def current_time():
    """ Get current time in seconds from epoch
    """
    return time.time()

class FaceChecker:
    """ Checks if there is a face in an image
    Fields:
        - client (GAPI Face Client)
        - last_request_time (int): Last time request was made to GAPI so we 
                                   don't spend to much money
        - image_file (String): Path to image file
        - request_delay (int): Number of second between each GAPI request
    """
    def __init__(self, image_file, old_image_file, request_delay=15):
        self.client = vision.ImageAnnotatorClient()
        self.last_request_time = None
        self.image_file = image_file
        self.old_image_file = old_image_file
        self.request_delay = request_delay

    def check(self):
        """ Checks if there is a face in the image_file
        Returns:
            - bool: Indicates if there is a face in the image

        Raises:
            - ValueError: If it has been not been enough time since the last
                          GAPI request
        """
        # Check if it has been enough time since  the last GAPI request so we 
        # don't spend too much money
        if self.last_request_time is not None:
            now = current_time()
            dt = now - self.last_request_time
            
            if dt < self.request_delay:
                raise ValueError("It has not been enough time since the last "+
                                 "GAPI request, not try'in spend too much money")

        self.last_request_time = current_time()

        # Read image file
        resp = None
        with open(self.image_file, 'rb') as file:
            content = file.read()
            image = types.Image(content=content)

            # Make GAPI request
            return False
            resp = self.client.face_detection(image=image)

        # Delete file
        try:
            os.remove(self.old_image_file)
        except FileNotFoundError:
            print("old file not found")

        os.rename(self.image_file, self.old_image_file)

        if resp is None or resp.face_annotations is None:
            return False

        faces = resp.face_annotations

        # Check if eyes are present
        for face in faces:
            landmark = face.Landmark

            t = landmark.Type
            desc = t.DESCRIPTOR

            for (k, v) in desc.values_by_name.items():
                if k.find('FACE'):
                    return True

        return False

# Run if not included
if __name__ == '__main__':
    checker = FaceChecker("images/test_face.jpg")

    result = checker.check()
    print(result)
