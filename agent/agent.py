import requests

class MicroTokenAIAgent:
    def __init__(self, server_url):
        self.server_url = server_url

    def request_token(self, user_id, action, resource, tier, metadata=None):
        if metadata is None:
            metadata = {}
        response = requests.post(
            f"{self.server_url}/issue-token",
            json={"user_id": user_id, "action": action, "resource": resource, "tier": tier, "metadata": metadata},
        )
        return response.json()

    def validate_token(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(f"{self.server_url}/validate-token", headers=headers)
        return response.json()

if __name__ == "__main__":
    # Example usage
    agent = MicroTokenAIAgent("http://microtokenai-server:8000")
    token_response = agent.request_token("test_user", "read", "/data", "free", {"geolocation": "US"})
    if "token" in token_response:
        print("Token issued:", token_response["token"])
        val_response = agent.validate_token(token_response["token"])
        print("Validation:", val_response)
    else:
        print("Error issuing token:", token_response)
