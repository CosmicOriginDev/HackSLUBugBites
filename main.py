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
    if result[0].boxes and result[0].boxes.cls is not None:
        potentialBugs = result[0].boxes.cls
        outputString = ""
        for bugNumber in potentialBugs:
            bugNumber = int(bugNumber)
            setOfBugs.add(result[0].names[bugNumber])
        for bug in setOfBugs:
            outputString += bug + " : " + Output.bite_info[bug] + "\n"
            return outputString
    else:
        return "No bug bite detected."




imageCropper = gr.Image(type="pil",format="jpg")
textBox = gr.Textbox(label = "Bug Info:", interactive=False)

inputWindow = gr.Interface(fn=getImageInfo, inputs= [imageCropper], outputs=[textBox], live=True).launch(debug=True)#, share=True)

