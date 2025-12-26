# Video Threat Detection

## Phase 1 – Environment Setup & Model Integration (Week 1)  
## Phase 2 – Person Detection & Object Tracking (Week 2)

---

## 📅 Timeline

* **Assignment received:** 15 December 2025  
* **Phase 1 completion:** 18 December 2025  
* **Phase 2 completion:** 26 December 2025  

* **Phase 1 time taken:** ~3 days  
* **Phase 2 time taken:** ~8 days  

Phase-wise development was followed to ensure stability, clarity, and scalability of the system.

---

## 📌 Project Overview

The goal of this project is to build an **AI-powered video threat detection pipeline** that is capable of:

* Converting video input into individual frames  
* Running person detection logic on each frame  
* Assigning **persistent identities (track IDs)** to detected persons across frames  
* Generating structured JSON outputs for further analysis  

The project is divided into phases:

* **Phase 1:** Build a strong detection and pipeline foundation  
* **Phase 2:** Extend the pipeline with object tracking and identity persistence  

---

## 📁 Project Structure

video-threat-detection/
│
├── DATA/
│ ├── videos/
│ │ └── sample.mp4
│ ├── frames/
│ │ ├── frame_0.jpg
│ │ ├── frame_1.jpg
│ │ └── ...
│ └── output_detections.json
│
├── src/
│ └── detection/
│ ├── frame_extractor.py
│ ├── image_loader.py
│ ├── bbox_utils.py
│ ├── vlm_detector.py
│ ├── tracker.py
│ ├── vlm_model_load.py
│ └── run_video_detection.py
│
├── main.py
├── .gitignore
└── README.md


---

## ✅ Phase 1 – Week 1: Work Completed

### 1️⃣ Python Environment Setup

**Status: ✅ Completed**

* Python virtual environment created  
* Required dependencies installed and verified:
  * `torch`
  * `transformers`
  * `opencv-python`
  * `numpy`
* Environment tested using multiple scripts  

Early environment-related issues were resolved to avoid future blockers.

---

### 2️⃣ Vision-Language Model (VLM) Integration

**Status: ✅ Completed (Using Alternative VL SLM)**

Assignment requirement mentioned:

> *Ollama with Qwen2.5-VL model (or alternative VL SLM)*

* **Florence-2 (HuggingFace Transformers)** was used as a valid alternative  
* Model loading and compatibility tested successfully  
* VLM interface designed to be model-agnostic  

**Important Note:**  
Stub-based inference was used in Phase 1 to validate pipeline structure.  
Real prompt-based VLM inference was finalized in Phase 2.

---

### 3️⃣ Video Frame Extraction Pipeline

**Status: ✅ Completed**

* Implemented using OpenCV (`frame_extractor.py`)  
* Video input taken from `DATA/videos/`  
* Frames extracted at fixed intervals  
* Frames saved to `DATA/frames/`  

This module forms the backbone of the entire video processing pipeline.

---

### 4️⃣ VLM Inference Wrapper (Phase 1 Scope)

**Status: ✅ Completed**

* Implemented in `vlm_detector.py`  
* Stub-based inference used to avoid early-stage model mismatch issues  
* Final output JSON structure defined early  
* Designed to be easily replaceable in later phases  

---

### 5️⃣ Bounding Box Parsing & Coordinate Normalization

**Status: ✅ Completed**

* Implemented in `bbox_utils.py`  
* Normalized bounding boxes converted into absolute pixel coordinates  

Formula used:

x_pixel = x_normalized × image_width  
y_pixel = y_normalized × image_height



* Verified using a 1280×720 frame resolution  

---

### 6️⃣ End-to-End Phase 1 Deliverable

**Status: ✅ Completed**

✔️ Video → frame extraction pipeline working  
✔️ Frame-wise detection pipeline working  
✔️ Structured JSON output generated  
✔️ Absolute pixel bounding boxes verified  

---

## ✅ Phase 2 – Week 2: Person Detection & Object Tracking

### 1️⃣ Tracker Foundation

**Status: ✅ Completed**

* `tracker.py` implemented  
* Intersection over Union (IoU) calculation added  
* `SimpleTracker` class created  
* Unique `track_id` generation logic implemented  

---

### 2️⃣ Tracker Integration into Pipeline

**Status: ✅ Completed**

* Tracker imported into `run_video_detection.py`  
* Tracker initialized **once outside the frame loop**  
* Frame-wise detections passed to tracker  
* Pipeline updated to:

### Pipeline Flow

Video -> Frames -> Detection -> Tracking -> JSON Output


---

### 3️⃣ Tracking Validation

**Status: ✅ Completed**

* Same person retains the same `track_id` across frames  
* New persons receive new unique IDs  
* IoU threshold prevents unnecessary ID duplication  
* Tracker state updated cleanly per frame  

---

### 4️⃣ Robust VLM Handling (Phase 2 Improvements)

**Status: ✅ Completed**

* Prompt-based person detection implemented  
* Strict JSON-only output parsing enforced  
* Retry logic added for Ollama timeouts  
* Full-frame garbage detections filtered  
* Near-duplicate bounding boxes deduplicated  

---

### 5️⃣ Phase 2 Output Format

**Sample Output:**

```json
{
  "image": "DATA/frames/frame_12.jpg",
  "detections": [
    {
      "x_min": 538,
      "y_min": 690,
      "x_max": 871,
      "y_max": 700,
      "track_id": 7
    }
  ]
}
```

Each detected person now has a **persistent identity across frames** using a unique `track_id`.

---

## 📌 Current Status

* **Phase 1 – Week 1: 100% Complete**
* **Phase 2 – Week 2: 100% Complete**

The system now performs **end-to-end video processing, person detection, and object tracking**, producing stable and structured JSON outputs.

---

## 🚀 Future Scope (Next Phases)

* Motion-based threat analysis  
* Temporal behavior modeling  
* Trajectory and speed estimation  
* Multi-camera identity association  
* Real-time video stream processing  

---

## 🧠 Final Summary

This repository represents a **fully functional, multi-phase video threat detection system**.

* Phase 1 established a strong, scalable detection foundation  
* Phase 2 added IoU-based object tracking with persistent identities  
* The codebase is modular, clean, and ready for higher-level threat intelligence  

The system is now prepared for advanced analytics without major refactoring.

