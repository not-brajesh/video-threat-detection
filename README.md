# 🎥 Video Threat Detection System

AI-Powered Surveillance Analytics Pipeline using Vision-Language Model (LLaVA-7B via Ollama)

---

## 📌 Project Overview

This project implements a **phase-wise AI-powered video threat detection pipeline**.

The system processes a video input and progressively performs:

1. Person Detection
2. Identity Tracking
3. Motion & Direction Analysis
4. Relationship Analysis
5. Rule-Based Threat Detection

All outputs are generated in a **structured JSON format**, making the system suitable for analytics, visualization, API integration, and real-time extensions.

---

## 🧩 Pipeline Architecture

```
Video
  ↓
Frame Extraction
  ↓
Person Detection (VLM - LLaVA 7B)
  ↓
Object Tracking (Track IDs)
  ↓
Motion & Direction Analysis
  ↓
Relationship Analysis
  ↓
Threat Detection
  ↓
JSON Output
```

---

## 📅 Development Timeline

* Assignment Received: 15 December 2025
* Phase 1 Completed: 18 December 2025
* Phase 2 Completed: 26 December 2025
* Phase 3 Completed: 13 January 2026
* Phase 4 Completed: 21 January 2026
* Phase 5 Completed: 25 January 2026

---

# 📁 Project Structure

```
video-threat-detection/
│
├── DATA/
│   ├── videos/
│   │   └── sample.mp4
│   ├── frames/
│   │   └── frame_*.jpg
│   └── output_detections.json
│
├── src/
│   ├── detection/
│   │   ├── frame_extractor.py
│   │   ├── vlm_detector.py
│   │   ├── person_detector.py
│   │   ├── tracker.py
│   │   └── run_video_detection.py
│   │
│   ├── tracking/
│   │   └── direction_tracker.py
│   │
│   ├── analysis/
│   │   └── relationship_analyzer.py
│   │
│   └── threat_detection/
│       └── threat_detector.py
│
├── tests/
│   ├── test_person_detector.py
│   ├── test_direction_tracker.py
│   └── test_threat_detector.py
│
├── README.md
└── main.py

```

---

# ✅ Implementation Status

✔ Phase 1 – Environment Setup & Detection Foundation
✔ Phase 2 – Person Detection & Tracking
✔ Phase 3 – Motion & Direction Analysis
✔ Phase 4 – Relationship Analysis
✔ Phase 5 – Threat Detection Engine

The system is **fully end-to-end functional**.


# ⚙️ Setup Instructions

## 1️⃣ Prerequisites

* Python 3.10+
* Git
* Ollama installed

---

## 2️⃣ Clone the Repository

```bash
git clone <repo_url>
cd video-threat-detection
```

---

## 3️⃣ Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure Torch, torchvision, and torchaudio versions match as defined.

---

## 5️⃣ Install & Setup Ollama

Download Ollama:

https://ollama.ai/download

Verify installation:

```bash
ollama --version
```

Pull required model:

```bash
ollama pull llava:7b
```

Verify model installation:

```bash
ollama list
```

Make sure `llava:7b` appears in the list.

---

# ▶️ Run the Detection Pipeline

Before running, clear old generated data to avoid stale results.

## 🧹 Step 1 – Clean Previous Output

### macOS / Linux

```
rm -rf DATA/frames/*
rm -f DATA/output_detections.json
```

## Windows (PowerShell)
```
Remove-Item DATA\frames\* -Force
Remove-Item DATA\output_detections.json -Force
```

## 🚀 Step 2 – Run the Pipeline

## Option 1 (Recommended)

```bash
python main.py
```

## Option 2 (Direct Module Execution)

```bash
python src/detection/run_video_detection.py
```


---

# 📂 Output

After successful execution:

* Frames extracted to `DATA/frames/`
* Final results saved in:

```
DATA/output_detections.json
```

---

# 📄 Sample Output (Simplified)

```json
{
  "image": "DATA/frames/frame_9.jpg",
  "detections": [
    {
      "track_id": 41,
      "motion": {
        "speed": 25.0,
        "direction": "E"
      }
    }
  ],
  "relationships": [],
  "threats": [
    {
      "threat_type": "RUNNING",
      "severity": 2,
      "description": "Person running with speed 25.00"
    }
  ]
}
```

Always clean previous frames before running a new video to ensure consistent results.

---

# 🧪 Testing

Run unit tests:

```bash
pytest
```

Covered Modules:

* Person detection filtering
* Direction tracking
* Threat detection logic

All tests passing.

---

# 🔮 Future Enhancements

* Zone-based threat detection
* Crowd density analysis
* Trajectory prediction
* Real-time video stream processing
* REST API & dashboard integration

---

# 🧠 Final Note

This project demonstrates a **clean, modular, and scalable architecture** for intelligent video threat detection.

The system is fully functional, testable, and production-extensible.


