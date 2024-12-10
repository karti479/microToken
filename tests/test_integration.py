import requests

def test_issue_and_validate_token():
    # Adjust URL to wherever the server is running
    resp = requests.post("http://localhost:8000/issue-token", json={
        "user_id": "test_user",
        "action": "read",
        "resource": "/data",
        "tier": "free",
        "metadata": {"geolocation": "US"}
    })
    assert resp.status_code == 200
    token_data = resp.json()
    assert "token" in token_data

    headers = {"Authorization": f"Bearer {token_data['token']}"}
    val_resp = requests.post("http://localhost:8000/validate-token", headers=headers)
    assert val_resp.status_code == 200
