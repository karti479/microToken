import os

SECRET_KEY = os.environ.get("MICROTOKENAI_SECRET_KEY", "default-secret-key")
ALGORITHM = "HS256"

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))

AWS_STS_ENDPOINT = os.environ.get("AWS_STS_ENDPOINT", "https://sts.amazonaws.com")
AZURE_GRAPH_ENDPOINT = os.environ.get("AZURE_GRAPH_ENDPOINT", "https://graph.microsoft.com/v1.0/me")
GCP_IAM_ENDPOINT = os.environ.get("GCP_IAM_ENDPOINT", "https://iam.googleapis.com/v1/projects/-/serviceAccounts/")

FREE_TIER_EXPIRATION = int(os.environ.get("FREE_TIER_EXPIRATION", 30))
PREMIUM_TIER_EXPIRATION = int(os.environ.get("PREMIUM_TIER_EXPIRATION", 60))

FREE_TIER_ANOMALY_RATE = float(os.environ.get("FREE_TIER_ANOMALY_RATE", 0.1))
PREMIUM_TIER_ANOMALY_RATE = float(os.environ.get("PREMIUM_TIER_ANOMALY_RATE", 0.02))
ALLOWED_GEOLOCATIONS_FREE = os.environ.get("ALLOWED_GEOLOCATIONS_FREE", "US,EU").split(",")
