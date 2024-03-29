from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread
import cv2

class PiVideoStream:
    def __init__(self, resolution=(640, 360), framerate = 32):
        # initialize the camera and stream
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self/camera, size = resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture, format = "bgr", use_video_port=True)

        # initalize the frame and variable used to indicate
        # if the thread should be stopped
        self.frame = None
        self.stopped = False
