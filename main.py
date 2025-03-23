#pip install gradio
#pip install pillow

import gradio as gr
from PIL import Image
from ultralytics import YOLO
import io
import Output

model = YOLO("runs\\detect\\train\\weights\\best.pt")
currentBug = None

def getImageInfo(imageParam):
   
    # Ensure the image is correctly formatted before YOLO
    result = model.predict(source=imageParam, save=True)
    
    setOfBugs = set()
    
    if result[0].boxes and result[0].boxes.cls is not None and imageParam != None:
        bugNumsTensor = result[0].boxes.cls
        outputString = ""
        listOfBugNums= list()
        setOfBugNums= set()
        for bugNumber in bugNumsTensor:
            setOfBugNums.add(int(bugNumber))
            listOfBugNums.append(int(bugNumber))
        setOfBugCount = list()
        setOfBugNames = list()
        for bugNumber in setOfBugNums:
            setOfBugCount.append(listOfBugNums.count(bugNumber))
            setOfBugNames.append(result[0].names[int(bugNumber)])
        largestBugName = setOfBugNames[setOfBugCount.index(max(setOfBugCount))]
        print(largestBugName + " : " + Output.bite_info[largestBugName] + "\n")
        outputString += largestBugName + " : " + Output.bite_info[largestBugName]
        return outputString
    else:
        return "No bug bite detected."




imageCropper = gr.Image(type="pil",format="jpg")
textBox = gr.Textbox(label = "Bug Info:", interactive=False)

inputWindow = gr.Interface(fn=getImageInfo, inputs= [imageCropper], outputs=[textBox], live=True).launch(debug=True)#, share=True)

