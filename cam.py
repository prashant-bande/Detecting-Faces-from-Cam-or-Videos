
from facedetector.facedetector import FaceDetector
from facedetector import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="path to where the cascade resides")
ap.add_argument("-v", "--video", help="path to where image file resides")
args = vars(ap.parse_args())

fd = FaceDetector(args["face"])

if not  args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])
    
while True:
    (ok, frame) = camera.read()
    if not ok:
        break
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50,50))
    frameClone = frame.copy()
    
    for (x, y, w, h) in faceRects:
        cv2.rectangle(frameClone, (x, y), (x+w, y+h), (0, 255,0), 2)
    
    cv2.imshow("face", frameClone)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()