#pip install gradio
#pip install pillow

import gradio as gr
from PIL import Image

def getImage(image):
    return image

def getImageInfo(image):
    #Change bug type according to yolo...?:

    #Print text if bug type:
    if (currentBug == None):
        return ""
    elif (currentBug == "mosquito"):
        return "mosquito bites are itchy"
    else:
        return "Invalid bug type"


currentBug = "mosquito"

imageCropper = gr.ImageEditor(transforms="crop", interactive=True, eraser=False, brush=False, layers=False)
textBox = gr.Textbox(label = "Bug Info:", interactive=False)

inputWindow = gr.Interface(fn=getImageInfo, inputs= imageCropper, outputs=textBox, live=True)

inputWindow.launch(share=True)

