from src.threat_detection.threat_detector import ThreatDetector

def test_running_person_detected():
    detector = ThreatDetector(running_speed_threshold=10.0)

    detections = [
        {
            "track_id": 1,
            "motion": {
                "speed": 25.0
            }
        }
    ]

    threats = detector.detect(
        detections=detections,
        relationships=[],
        frame_path="frame_001.jpg"
    )

    assert len(threats) == 1
    assert threats[0].threat_type == "RUNNING"
