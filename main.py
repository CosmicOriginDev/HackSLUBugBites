#pip install gradio
#pip install pillow

import gradio as gr
from PIL import Image

def getImage(image):
    return image

def startCrop():


finalImage = None

imageGetter = gr.Image(show_fullscreen_button=False)
imageCropper = gr.ImageEditor(transforms="crop", interactive=True, eraser=False, brush=False, layers=False, crop_size=)
inputWindow = gr.Interface(fn=getImage, inputs= imageCropper, outputs=finalImage)

imageCropper.input()

inputWindow.launch(share=True)

