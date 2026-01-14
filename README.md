# Video Threat Detection

## Phase-wise Development Overview
- **Phase 1 – Environment Setup & Model Integration (Week 1)**
- **Phase 2 – Person Detection & Object Tracking (Week 2)**
- **Phase 3 – Motion & Direction Analysis (Week 3)**
- **Phase 4 – Relationship Analysis & Final Pipeline (Week 4)**

---

## 📅 Timeline

- **Assignment received:** 15 December 2025  
- **Phase 1 completed:** 18 December 2025  
- **Phase 2 completed:** 26 December 2025  
- **Phase 3 completed:** 13 January 2026  
- **Phase 4 completed:** 14 January 2026  

**Time Taken**
- Phase 1: ~3 days  
- Phase 2: ~8 days  
- Phase 3: ~4 days  
- Phase 4: ~2 days  

Phase-wise development was followed to ensure clarity, stability, and scalability.

---

## 📌 Project Overview

This project implements an **AI-powered video threat detection pipeline** capable of:

- Converting video input into individual frames  
- Detecting persons in each frame using a Vision-Language Model (VLM)  
- Assigning **persistent identities (`track_id`)** to detected persons  
- Analyzing **motion, speed, and direction** over time  
- Performing **relationship analysis** between multiple persons  
- Producing structured **JSON output** for higher-level threat reasoning  

### Phase Breakdown
- **Phase 1:** Detection pipeline & environment foundation  
- **Phase 2:** IoU-based object tracking with persistent IDs  
- **Phase 3:** Temporal motion, speed, and direction analysis  
- **Phase 4:** Proximity-based relationship analysis and full pipeline integration  

---

## 📁 Project Structure


video-threat-detection/
│
├── DATA/
│   ├── videos/
│   │   └── sample.mp4
│   ├── frames/                 
│   └── output_detections.json
│
├── src/
│   ├── detection/
│   │   ├── frame_extractor.py
│   │   ├── image_loader.py
│   │   ├── bbox_utils.py
│   │   ├── vlm_detector.py
│   │   ├── tracker.py
│   │   ├── vlm_model_load.py
│   │   └── run_video_detection.py
│   │
│   ├── tracking/
│   │   └── direction_tracker.py
│   │
│   └── analysis/
│       └── relationship_analyzer.py
│
├── main.py
├── .gitignore
└── README.md


---

## ✅ Phase 1 – Environment & Model Integration

**Status: Completed**

- Python virtual environment created  
- Required dependencies installed (`torch`, `transformers`, `opencv-python`, `numpy`)  
- Vision-Language Model interface designed to be model-agnostic  
- Alternative VL model used as permitted by assignment  
- Stub-based inference used initially to validate pipeline structure  

---

## ✅ Phase 2 – Person Detection & Object Tracking

**Status: Completed**

### Key Features
- IoU-based `SimpleTracker` implemented  
- Unique `track_id` assigned per person  
- Tracker initialized **once outside frame loop**  
- Stable identity persistence across frames  

### Pipeline Flow

Video → Frames → Detection → Tracking → JSON


---

## ✅ Phase 3 – Motion & Direction Analysis

**Status: Completed**

### Implemented Capabilities
- Frame-to-frame displacement calculation  
- Speed estimation using temporal deltas  
- Direction inference (N, S, E, W, STATIONARY)  
- Robust handling of missing / noisy detections  

Each tracked object now includes motion metadata:
```json
"motion": {
  "dx": 12.4,
  "dy": -3.1,
  "speed": 12.8,
  "direction": "E"
}
```

## ✅ Phase 4 – Relationship Analysis & Final Pipeline

**Status: Completed**

### Added Capabilities
- Proximity-based relationship detection between tracked persons
- Temporal consistency using minimum frame thresholds
- Relationship analyzer integrated cleanly without breaking earlier phases

### Final Pipeline

Video
 → Frames
 → Detection
 → Tracking
 → Motion Analysis
 → Relationship Analysis
 → JSON Output
 
---

python -m src.detection.run_video_detection

---

## 📄 Output

### File: DATA/output_detections.json
  
### Contains per-frame:
- Bounding boxes (absolute pixels)
- track_id
- Motion data
- Relationship data (if detected)

## 🚀 Future Scope

- Zone-based threat detection
- Crowd & tailgating analysis
- Trajectory prediction
- Real-time CCTV / stream integration
- Multi-camera identity association

## 🧠 Final Summary

### This repository represents a complete, phase-wise AI video threat detection system.
- Phase 1 laid the foundation
- Phase 2 added reliable tracking
- Phase 3 introduced motion intelligence
- Phase 4 completed relational reasoning

### The system is stable, modular, and ready for evaluation or extension.


---


