from ultralytics import YOLO

# Load YOLOv8 model (you can use 'yolov8n.pt', 'yolov8s.pt', etc.)
model = YOLO("yolov8n.pt")  

# Train the model
results = model.train(data="datasets/biteImages/data.yaml", epochs=50, batch=8, imgsz=640)
metrics = model.val()
results.show()
model.export(format="onnx")  # Export to ONNX format