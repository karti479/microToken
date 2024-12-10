import random
from config import FREE_TIER_ANOMALY_RATE, PREMIUM_TIER_ANOMALY_RATE, ALLOWED_GEOLOCATIONS_FREE

def evaluate_request(payload):
    tier = payload["tier"]
    metadata = payload.get("metadata", {})
    geolocation = metadata.get("geolocation")

    if tier == "free":
        if geolocation not in ALLOWED_GEOLOCATIONS_FREE:
            return False, f"Free-tier access restricted to {ALLOWED_GEOLOCATIONS_FREE}"
        if random.random() < FREE_TIER_ANOMALY_RATE:
            return False, "Suspicious activity detected (free tier)"
    elif tier == "premium":
        if random.random() < PREMIUM_TIER_ANOMALY_RATE:
            return False, "Anomaly detected (premium tier)"

    return True, "Request validated successfully"
