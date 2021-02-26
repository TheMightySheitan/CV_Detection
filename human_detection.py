# Machine learning
import cv2
# Image processing
import imutils
# Use for scientific computing; The image will be stored in a numpy array
import numpy as np
# Used to give input in command line
import argparse

# HOG = Histogram of Oriented Gradient
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

"""
detect(frame) lists containing coordinates of bounding box of person through the function detectMultiScale()
Coordinates are x, y, w, h, where x,y are the starting coordinates of the box, w,h are the width and height of the given box 
"""


def detect(frame):
    bounding_box_coordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    person = 1
    for x, y, w, h in bounding_box_coordinates:
        cv2.rectangle(frame, (x, y), (x + y + w + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 1)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('output', frame)

    return frame


def humanDetector(args):
    image_path = args["image"]
    video_path = args['video']
    if str(args["camera"]):
        camera = True
    else:
        camera = False

    writer = None
    if args['output'] is not None and image_path is None:
        writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MPJG'), 10, (600, 600))

    if camera:
        print('[INFO] Opening camera')


def detectByCamera(writer):
    video = cv2.VideoCapture(0)