from pydantic import BaseModel

class TokenRequest(BaseModel):
    user_id: str
    action: str
    resource: str
    tier: str  # 'free' or 'premium'
    # metadata: user provides request-specific data (e.g. iam_token, geolocation)
    metadata: dict = {}
