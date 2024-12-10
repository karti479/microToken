from prometheus_client import Counter

anomalies_detected = Counter("anomalies_detected", "Number of detected anomalies")

def record_anomaly():
    anomalies_detected.inc()
