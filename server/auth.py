import requests
from config import AWS_STS_ENDPOINT, AZURE_GRAPH_ENDPOINT, GCP_IAM_ENDPOINT

def verify_iam_token(iam_token, provider):
    if not iam_token:
        return False

    if provider == "aws":
        # Simplified example for demonstration
        response = requests.get(f"{AWS_STS_ENDPOINT}?Action=GetCallerIdentity&Token={iam_token}")
        return response.status_code == 200
    elif provider == "azure":
        response = requests.get(AZURE_GRAPH_ENDPOINT, headers={"Authorization": f"Bearer {iam_token}"})
        return response.status_code == 200
    elif provider == "gcp":
        response = requests.get(f"{GCP_IAM_ENDPOINT}{iam_token}")
        return response.status_code == 200

    return False
