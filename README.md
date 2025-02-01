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