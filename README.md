# Video Threat Detection

## Phase 1 – Environment Setup & Model Integration (Week 1)

## Phase 2 – Person Detection & Object Tracking (Week 2)

## Phase 3 – Motion & Direction Analysis (Week 3)

---

## 📅 Timeline

* **Assignment received:** 15 December 2025

* **Phase 1 completion:** 18 December 2025

* **Phase 2 completion:** 26 December 2025

* **Phase 3 completion:** 13 January 2026

* **Phase 1 time taken:** ~3 days

* **Phase 2 time taken:** ~8 days

* **Phase 3 time taken:** ~4 days

Phase-wise development was followed to ensure stability, clarity, and scalability of the system.

---

## 📌 Project Overview

The goal of this project is to build an **AI-powered video threat detection pipeline** that is capable of:

* Converting video input into individual frames
* Running person detection logic on each frame
* Assigning **persistent identities (track IDs)** to detected persons across frames
* Analyzing **motion, speed, and direction** of tracked persons
* Generating structured JSON outputs for higher-level threat analysis

The project is divided into phases:

* **Phase 1:** Detection and pipeline foundation
* **Phase 2:** Object tracking and identity persistence
* **Phase 3:** Temporal motion and direction analysis

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
* Required dependencies installed and verified
* Environment tested using multiple scripts

---

### 2️⃣ Vision-Language Model (VLM) Integration

**Status: ✅ Completed**

* Alternative VL SLM used as permitted by assignment
* Model loading and compatibility verified
* VLM interface kept model-agnostic

---

### 3️⃣ Video Frame Extraction Pipeline

**Status: ✅ Completed**

* Implemented using OpenCV
* Frames extracted and saved to disk
* Reliable frame indexing ensured

---

### 4️⃣ Bounding Box Parsing & Coordinate Normalization

**Status: ✅ Completed**

* Normalized coordinates converted to absolute pixels
* Verified using 1280×720 resolution

---

## ✅ Phase 2 – Week 2: Person Detection & Object Tracking

### 1️⃣ IoU-Based Tracker Implementation

**Status: ✅ Completed**

* `SimpleTracker` implemented using IoU matching
* Unique `track_id` assigned per detected person

---

### 2️⃣ Tracker Integration into Pipeline

**Status: ✅ Completed**

Pipeline flow:

Video → Frames → Detection → Tracking → JSON Output

---

### 3️⃣ Tracking Validation

**Status: ✅ Completed**

* Persistent identities maintained across frames
* Clean tracker state management
* Stable JSON output generated

---

## ✅ Phase 3 – Week 3: Motion & Direction Analysis

### 1️⃣ Direction & Motion Tracking Module

**Status: ✅ Completed**

* `DirectionTracker` class implemented
* Maintains temporal position history per `track_id`
* Computes frame-to-frame displacement

---

### 2️⃣ Speed Calculation

**Status: ✅ Completed**

* Speed calculated using pixel displacement over time
* FPS-based normalization applied
* Differentiates moving vs stationary objects

---

### 3️⃣ Direction Inference

**Status: ✅ Completed**

* Motion vectors converted to cardinal directions
* Supported directions: **N, S, E, W, STATIONARY**
* Handles noisy and intermittent detections robustly

---

### 4️⃣ Phase 3 Output Integration

**Status: ✅ Completed**

* Motion-ready tracking data stored in structured JSON
* Compatible with future threat detection logic
* No breaking changes to earlier phases

---

## 📌 Current Status

* **Phase 1 – Week 1: 100% Complete**
* **Phase 2 – Week 2: 100% Complete**
* **Phase 3 – Week 3: 100% Complete**

The system now supports **detection, tracking, and motion-level analysis**.

---

## 🚀 Future Scope (Next Phases)

* Relationship analysis (crowd, proximity, tailgating)
* Zone-based threat detection
* Trajectory prediction
* Real-time surveillance stream integration

---

## 🧠 Final Summary

This repository represents a **robust, phase-wise AI-powered video threat detection system**.

* Phase 1 established detection and pipeline foundations
* Phase 2 added reliable object tracking
* Phase 3 introduced temporal motion and direction intelligence

The system is now **ready for higher-level threat reasoning and analytics**.
