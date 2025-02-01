# NovaVista AI Football Analytics ⚽  

NovaVista is an AI-powered football analytics system designed for the Egyptian League.  
It automatically analyzes match videos, tracks players, generates heatmaps, detects tactical patterns, and reconstructs key moments in 3D.  

---

## 🚀 Features  
✅ **Player & Ball Detection** – YOLOv8-based object detection.  
✅ **Player Tracking** – DeepSORT for real-time tracking.  
✅ **Heatmaps & Stats** – AI-driven movement & pass network analysis.  
✅ **3D Match Visualization** – NeRF & SMPL for realistic replays.  
✅ **Web Dashboard** – Interactive analytics for teams & fans.  

---

## 📂 Project Structure  

```bash
novavista-ai-football
│── config/                 # Configuration files
│   │── requirements.txt        # Python dependencies
│── data/                   # Raw match videos & datasets
├── docker/                  # New folder for Docker-related files
│   ├── Dockerfile          # Main Dockerfile
│   ├── Dockerfile.gpu      # GPU variant if needed
│   └── .dockerignore       # Docker ignore file
│── models/                 # Trained AI models (YOLO, DeepSORT, NeRF, etc.)
│── notebooks/              # Jupyter notebooks for experiments
│── src/                    # Main source code
│   ├── processing/         # Video & data preprocessing
│   ├── detection/          # Player & ball detection
│   ├── tracking/           # Player tracking logic
│   ├── analytics/          # Heatmaps, pass networks, stats
│   ├── reconstruction/     # 3D reconstruction & visualization
│   ├── dashboard/          # Web interface (Flask/Streamlit)
│── scripts/                # Helper scripts (model training, dataset processing)
│── tests/                  # Unit tests
│── .gitignore              # Ignore large files (videos, models, etc.)
│── README.md               # Project documentation
│── docker-compose.yml      # Docker setup for easy deployment
│── app.py                  # Main entry point
```


``` mermaid 
flowchart TD
    %% Main project node
    A["novavista-ai-football"]
    style A fill:#2c3e50,stroke:#34495e,color:white,width:200px

    %% Level 1: Main Categories
    subgraph MainDirs ["Main Directories"]
        direction TB
        B["data\nRaw match videos"]
        C["models\nTrained AI models"]
        D["notebooks\nJupyter notebooks"]
    end
    
    %% Level 2: Source Code
    subgraph SourceCode ["Source Code"]
        direction TB
        E["src"]
        subgraph Components ["Components"]
            direction TB
            F["processing\nVideo preprocessing"]
            G["detection\nPlayer & ball"]
            H["tracking\nPlayer tracking"]
            I["analytics\nStats & heatmaps"]
            J["reconstruction\n3D visualization"]
            K["dashboard\nWeb interface"]
        end
    end
    
    %% Level 3: Support Files
    subgraph Support ["Support Files"]
        direction TB
        L["config\nConfiguration"]
        M["scripts\nHelper scripts"]
        N["tests\nUnit tests"]
    end
    
    %% Level 4: Root Files
    subgraph RootFiles ["Root Files"]
        direction TB
        O[".gitignore"]
        P["README.md"]
        Q["requirements.txt"]
        R["docker-compose.yml"]
        S["app.py"]
    end

    %% Styling
    style B fill:#3498db,stroke:#2980b9,color:white
    style C fill:#3498db,stroke:#2980b9,color:white
    style D fill:#3498db,stroke:#2980b9,color:white
    style E fill:#2ecc71,stroke:#27ae60,color:white
    style F fill:#1abc9c,stroke:#16a085,color:white
    style G fill:#1abc9c,stroke:#16a085,color:white
    style H fill:#1abc9c,stroke:#16a085,color:white
    style I fill:#1abc9c,stroke:#16a085,color:white
    style J fill:#1abc9c,stroke:#16a085,color:white
    style K fill:#1abc9c,stroke:#16a085,color:white
    style L fill:#9b59b6,stroke:#8e44ad,color:white
    style M fill:#9b59b6,stroke:#8e44ad,color:white
    style N fill:#9b59b6,stroke:#8e44ad,color:white
    style O fill:#e74c3c,stroke:#c0392b,color:white
    style P fill:#e74c3c,stroke:#c0392b,color:white
    style Q fill:#e74c3c,stroke:#c0392b,color:white
    style R fill:#e74c3c,stroke:#c0392b,color:white
    style S fill:#e74c3c,stroke:#c0392b,color:white

    %% Connections
    A --> MainDirs
    A --> SourceCode
    A --> Support
    A --> RootFiles
    E --> Components
    
    %% Define vertical relationships
    B --> C
    C --> D
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    L --> M
    M --> N
    O --> P
    P --> Q
    Q --> R
    R --> S
```

# 🚀 Step 1: Player & Ball Detection (YOLOv8 + DeepSORT)

## 🔹 Goal:
Detect players and the ball in match videos **frame by frame** using **YOLOv8** and track them in real time with **DeepSORT**.

## 🛠 First Tasks
✅ **1. Set Up the Environment**  
✅ **2. Download Pretrained YOLOv8 Model**  
✅ **3. Run YOLOv8 on a Sample Match Video**  
✅ **4. Integrate DeepSORT for Player Tracking**  
✅ **5. Save Detection Data (Player Positions, Ball Location, Time Stamps, etc.)**

## 🛠 Task 1: Set Up the Environment

### 📌 Install Dependencies
Inside your project folder, create a virtual environment and install required packages:

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install ultralytics opencv-python numpy pandas torch torchvision torchaudio
```

### 📌 Verify Installation
Test if **YOLOv8** is correctly installed:

```python
from ultralytics import YOLO

# Load a pretrained YOLOv8 model
model = YOLO("yolov8n.pt")
print(model)
```

If it prints the model details, **everything is working**! ✅

## 🛠 Task 2: Download a Sample Match Video
🎥 Get a **short Egyptian League match clip** (10-20 seconds) and place it inside the `data/` folder.

## 🛠 Task 3: Run YOLOv8 on the Video
Use YOLOv8 to detect players and the ball:

```python
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Run inference on the match video
results = model("data/match_clip.mp4", save=True)
```

This will generate a video with **bounding boxes** around players and the ball.

## 🎯 Next Steps (After Running YOLOv8)
After this, we'll **integrate DeepSORT** to track each player **across frames**. 🚀

Let me know when you finish this step, and I'll guide you through tracking! 🏆

---

# 🐳 Docker Setup for YOLOv8 + DeepSORT

## 📁 Required Files

### 1. Dockerfile
```dockerfile
# Use NVIDIA CUDA base image
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Set working directory
WORKDIR /app

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Command to run when starting the container
CMD ["python3", "app.py"]
```

### 2. requirements.txt
```text
ultralytics>=8.0.0
opencv-python-headless
numpy
pandas
torch
torchvision
torchaudio
```

### 3. docker-compose.yml
```yaml
version: '3.8'

services:
  novavista:
    build: .
    container_name: novavista-ai
    volumes:
      - ./:/app
      - ./data:/app/data
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    ports:
      - "8080:8080"  # If you need web interface
    command: python3 app.py
```

### 4. app.py
```python
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
```

### 5. .dockerignore
```text
data/*
venv/
__pycache__/
*.pyc
.git/
.env
```

## 🚀 Usage

### Build and Run with Docker Compose:
```bash
# Build and start the container
docker compose up --build

# Stop the container
docker compose down
```

### Process a Video:
```bash
# Copy your video to the data folder
cp your_match.mp4 data/

# Enter the container
docker exec -it novavista-ai bash

# Run detection (in Python)
python3
```

```python
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model("data/your_match.mp4", save=True)
```

## 🔧 Benefits of Docker Setup:

1. **Consistent Environment**: Same setup everywhere
2. **GPU Support**: NVIDIA CUDA ready
3. **No Local Setup**: Everything containerized
4. **Volume Mounting**: Easy data access
5. **Resource Management**: GPU and memory limits configurable

## 📝 Notes:
- Make sure you have Docker and NVIDIA Container Toolkit installed
- The data folder is mounted as a volume, so output videos will persist
- GPU support requires NVIDIA drivers and Docker GPU support
- You can modify resource limits in docker-compose.yml