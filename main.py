#pip install gradio
import gradio as gr
from PIL import Image

def greet(name):
    greeting = "Hello " + name
    return greeting

def getImage(image):
    return image

#demo = gr.Interface(fn= greet,
#             inputs= gr.Textbox(),
#             outputs=gr.Textbox(),
#             )

finalImage = None

imageGetter = gr.Image(show_fullscreen_button=False)
imageCropper = gr.ImageEditor(transforms="crop", interactive=True, eraser=False, brush=False, layers=False)
inputWindow = gr.Interface(fn=getImage, inputs= imageCropper, outputs=finalImage)

inputWindow.launch()

