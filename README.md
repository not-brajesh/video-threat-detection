
---

# Video Threat Detection System

## 📌 Project Overview

This project implements a **phase-wise AI-powered video threat detection pipeline**.
The system processes a video input and progressively performs:

1. Person detection
2. Identity tracking
3. Motion & direction analysis
4. Relationship analysis
5. Rule-based threat detection

All outputs are generated in a **structured JSON format**, making the system suitable for further analytics, visualization, or real-time extensions.

---

## 🧩 Pipeline Summary

```
Video
  ↓
Frame Extraction
  ↓
Person Detection
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

* **Assignment received:** 15 December 2025
* **Phase 1 completed:** 18 December 2025
* **Phase 2 completed:** 26 December 2025
* **Phase 3 completed:** 13 January 2026
* **Phase 4 completed:** 21 January 2026
* **Phase 5 completed:** 25 January 2026

---

## 📁 Project Structure

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

## ✅ Phase 1 – Environment Setup & Detection Foundation

**Status: Completed**

* Python virtual environment setup
* Dependencies installed and verified
* Video frame extraction implemented using OpenCV
* Vision-Language Model (VLM) interface integrated
* Detection pipeline skeleton finalized

---

## ✅ Phase 2 – Person Detection & Object Tracking

**Status: Completed**

* Person-only detection filtering implemented
* IoU-based `SimpleTracker` developed
* Persistent `track_id` assigned across frames
* Stable detection + tracking JSON output generated

---

## ✅ Phase 3 – Motion & Direction Analysis

**Status: Completed**

* `DirectionTracker` implemented
* Frame-to-frame displacement calculation
* Speed estimation using pixel motion
* Direction inference (`N, S, E, W, STATIONARY`)
* Motion data attached to each tracked person

---

## ✅ Phase 4 – Relationship Analysis

**Status: Completed**

* Proximity-based relationship analyzer implemented
* Detects spatial relationships between tracked persons
* Relationship data stored alongside detections
* Designed for crowd & interaction analysis

---

## ✅ Phase 5 – Threat Detection

**Status: Completed**

* Rule-based `ThreatDetector` implemented
* Uses motion + tracking data for reasoning
* Example threat detected:

  * **RUNNING person based on speed threshold**
* Threat metadata includes:

  * `threat_type`
  * `severity`
  * `description`
  * `involved_ids`
  * `frame`
  * `timestamp`

Threats are stored directly in the output JSON.

---

## 📄 Sample Output (Simplified)

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

---

## 🧪 Testing

* Unit tests written using `pytest`
* Covered modules:

  * Person detection cleanup
  * Direction tracking
  * Threat detection logic
* All tests passing successfully

---

## 🚀 Current Status

✔ Phase 1 – Completed
✔ Phase 2 – Completed
✔ Phase 3 – Completed
✔ Phase 4 – Completed
✔ Phase 5 – Completed

The system is now **end-to-end functional** and ready for extension.
---
## ⚙️ Setup Instructions

~~~
git clone <repo_url>
cd video-threat-detection
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~

Run Detection Pipeline

~~~
python src/detection/run_video_detection.py
~~~


---

## 🔮 Future Scope

* Zone-based threat detection
* Crowd density analysis
* Trajectory prediction
* Real-time video stream integration
* Alerting & visualization dashboards

---

## 🧠 Final Note

This project demonstrates a **clean, modular, phase-wise approach** to building an intelligent video threat detection system.
The architecture is scalable, testable, and ready for real-world extensions.

---

