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
        detectByCamera(output_path, writer)
    elif video_path is not None:
        print('[INFO] Opening video from path')
        detectByPathVideo(video_path, writer)
    elif image_path is not None:
        print('[INFO] Opening image from path')
        detectByPathImage(image_path, args['output'])


def detectByCamera(writer):
    video = cv2.VideoCapture(0)
    """
    VideoCapture(0) : uses the default camera on the running device
    """
    print('Detecting people...')

    while True:
        check, frame = video.read()

        frame = detect(frame)
        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def detectByPathVideo(path, writer):
    video = cv2.VideoCapture(path)
    check, frame = video.read()
    if not check:
        print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
        return
    print('Detecting people...')
    while video.isOpened():
        # check is True if reading was successful
        check, frame = video.read()
        if check:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]))
            frame = detect(frame)

            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()


"""
this method is used if a person needs to be detected from an image
"""


def detectByPathImage(path, output_path):
    image = cv2.imread(path)
    image = imutils.resize(image, width=min(800, image.shape[1]))
    result_image = detect(image)
    if output_path is not None:
        cv2.imwrite(output_path, result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-v", "--video", default=None, help="path to Video File ")
    arg_parse.add_argument("-i", "--image", default=None, help="path to Image File ")
    arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
    arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
    args = vars(arg_parse.parse_args())
    return args


if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    args = argsParser()
    humanDetector(args)
