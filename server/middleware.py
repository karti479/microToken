from fastapi import Request, HTTPException
from jose import jwt
from config import SECRET_KEY, ALGORITHM

async def enforce_tiers(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload["tier"] == "free" and request.url.path == "/premium-feature":
            raise HTTPException(status_code=403, detail="Upgrade to premium for this feature")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return await call_next(request)
