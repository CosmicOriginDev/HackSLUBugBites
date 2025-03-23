from ultralytics import YOLO


def main():
    # Load YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(data="datasets/biteImages/data.yaml", epochs=1, batch=8, imgsz=640)

    # Validate the model
    model.val()

    # Export to ONNX format
    model.export(format="ONNX")
    print("Training and export completed successfully.")


if __name__ == "__main__":
    main()
