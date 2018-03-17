#!/usr/bin/python

import socket
import sys
import datetime
import dlib     # dlib for accurate face detection
import cv2      # opencv
import imutils  # helper functions from pyimagesearch.com
import argparse

NUM_WARM_UP_FRAMES = 2
IMAGE_DIR = "/var/www/html/images/"
PORT = 5055
CAMERA_PORT = 0


# Fancy box drawing function by Dan Masek
def draw_border(img, pt1, pt2, color, thickness, r, d):
    x1, y1 = pt1
    x2, y2 = pt2

    # Top left drawing
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right drawing
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left drawing
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right drawing
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)

def main(argv):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", PORT))

    print "Socket open"

    while True:
        data, addr = sock.recvfrom(1024)

        # Received a request to take a picture.
        # Create the file name based on date-time.
        timestamp = datetime.datetime.now().strftime("%Y%b%d_%H:%M:%S.%f")
        camera = cv2.VideoCapture(CAMERA_PORT)

        # Let the camera adjust to the lighting.
        image = None
        for i in xrange(NUM_WARM_UP_FRAMES):
            retval, image = camera.read()

        camera.release()

        # resize the frames to be smaller and switch to gray scale
        frame = imutils.resize(image, width=700)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Make copies of the frame for transparency processing
        overlay = frame.copy()
        output = frame.copy()
        
        # set transparency value
        alpha  = 0.5

        # Face detector
        detector = dlib.get_frontal_face_detector()

        # detect faces in the gray scale frame
        face_rects = detector(gray, 0)
        
        # loop over the face detections
        faceDetected = False
        for i, d in enumerate(face_rects):
            faceDetected = True
            x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()
        
            # draw a fancy border around the faces
            draw_border(overlay, (x1, y1), (x2, y2), (162, 255, 0), 4, 10, 10)
        
            # make semi-transparent bounding box
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

        fileName = IMAGE_DIR + timestamp + ".png"
        print "Saving image.  " + fileName
        cv2.imwrite(fileName, output)

        if faceDetected:
            sock.sendto("/images/" + timestamp + ".png", addr)
        else:
            sock.sendto("False alarm", addr)

# Entry point for the program.
if __name__ == "__main__":
    main(sys.argv[1:])
