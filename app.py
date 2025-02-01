from ultralytics import YOLO
import cv2
import torch

def main():
    # Print system info
    print("🚀 Starting NovaVista AI Football Analysis")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA device: {torch.cuda.get_device_name(0)}")
    
    # Load YOLOv8 model
    model = YOLO("yolov8n.pt")
    print("✅ Model loaded successfully!")

if __name__ == "__main__":
    main()