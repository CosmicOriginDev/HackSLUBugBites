import cv2
from PIL import Image

from ultralytics import YOLO
import Output

model = YOLO("runs\detect\\train\weights\\best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
#results = model.predict(source="0")
#results = model.predict(source="HorseflyTest.jpg", show=True)  # Display preds. Accepts all YOLO predict arguments

# from PIL
im1 = Image.open("datasets\\biteImages\\train\\images\\fire-ant-7_jpg.rf.43a379c21d29d98e5836b6f1497304c7.jpg")
result = model.predict(source=im1, save=True)  # save plotted images


#Print text if bug type:
#print(result)

setOfBugs = set()
if result[0].boxes and result[0].boxes.cls is not None:
    potentialBugs = result[0].boxes.cls
    outputString = ""
    for bugNumber in potentialBugs:
        bugNumber = int(bugNumber)
        setOfBugs.add(result[0].names[bugNumber])
for bug in setOfBugs:
    print(bug + " : " + Output.bite_info[bug] + "\n")
# from ndarray
#im2 = cv2.imread("bus.jpg")
#results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels

# from list of PIL/ndarray
#results = model.predict(source=[im1, im2])