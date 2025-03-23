from ultralytics import YOLO
import torch


def main():
    # torch.cuda.set_device(1)
    # Load YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(data="datasets/biteImages/data.yaml", epochs=300, batch=-1, imgsz=1280)
    model.to('cuda')
    # Validate the model
    model.val()

    # Export to ONNX format
    model.export(format="openvino",device=0)
    print("Training and export completed successfully.")


if __name__ == "__main__":
    main()
