from jose import jwt
import time
from db import save_token_metadata
from ai_engine import evaluate_request
from auth import verify_iam_token
from config import SECRET_KEY, ALGORITHM, FREE_TIER_EXPIRATION, PREMIUM_TIER_EXPIRATION

async def issue_token(request):
    # Validate mandatory fields
    if not request.user_id or not request.action or not request.resource or not request.tier:
        return {"error": "Missing required token request fields"}

    iam_token = request.metadata.get("iam_token")
    iam_provider = request.metadata.get("iam_provider")
    if iam_provider and not verify_iam_token(iam_token, iam_provider):
        return {"error": "IAM authentication failed"}

    expiration = PREMIUM_TIER_EXPIRATION if request.tier == "premium" else FREE_TIER_EXPIRATION
    token_payload = {
        "sub": request.user_id,
        "action": request.action,
        "resource": request.resource,
        "exp": time.time() + expiration,
        "start_time": time.time(),
        "tier": request.tier,
        "metadata": request.metadata
    }
    token = jwt.encode(token_payload, SECRET_KEY, algorithm=ALGORITHM)
    save_token_metadata(token, token_payload)
    return {"token": token, "expires_in": expiration}

async def validate_token(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return {"is_valid": False, "message": "Missing or invalid token"}

    token = auth_header.split(" ")[1]
    from jose import JWTError
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        is_valid, message = evaluate_request(payload)
        if not is_valid:
            return {"is_valid": False, "message": message}
        return {"is_valid": True, "payload": payload}
    except JWTError as e:
        return {"is_valid": False, "message": f"Token decoding error: {e}"}
