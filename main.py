#pip install gradio
#pip install pillow

import gradio as gr
from PIL import Image
from ultralytics import YOLO
import io
import Output

model = YOLO("runs\detect\\train\weights\\best.pt")
currentBug = None


def getImageInfo(imageParam):
    image = Image.open(imageParam['layers'][0]).convert("RGB")
    #Change bug type according to yolo...?:

    jpeg_buffer = io.BytesIO()
    image.save(jpeg_buffer, format="JPEG")
    jpeg_buffer.seek(0)  # Rewind to start of buffer

    # Reload image from buffer (still a PIL Image, now "JPEG-like")
    image = Image.open(jpeg_buffer)
    image.show()


    result = model.predict(source=image, save=True)

    #Print text if bug type:
    print(result[0].boxes.cls)
    
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




imageCropper = gr.ImageEditor(transforms="crop", interactive=True, eraser=False, brush=False, layers=False, type='filepath')
textBox = gr.Textbox(label = "Bug Info:", interactive=False)

inputWindow = gr.Interface(fn=getImageInfo, inputs= [imageCropper], outputs=[textBox], live=True).launch(debug=True)#, share=True)

