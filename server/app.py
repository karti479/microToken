from fastapi import FastAPI, HTTPException, Request
from middleware import enforce_tiers
from services import issue_token, validate_token
from revocation import propagate_revocation
from metrics import record_anomaly
from models import TokenRequest
from prometheus_client import make_asgi_app
from fastapi.responses import JSONResponse

app = FastAPI()

app.middleware("http")(enforce_tiers)

@app.post("/issue-token")
async def issue_token_endpoint(request: TokenRequest):
    response = await issue_token(request)
    if "error" in response:
        return JSONResponse(status_code=400, content=response)
    return response

@app.post("/validate-token")
async def validate_token_endpoint(request: Request):
    status = await validate_token(request)
    if not status["is_valid"]:
        record_anomaly()
        return JSONResponse(status_code=403, content={"error": status["message"]})
    return status

@app.post("/revoke-token")
async def revoke_token_endpoint(token_id: str):
    propagate_revocation(token_id, reason="Revoked by admin")
    return {"status": "revoked"}

# Prometheus metrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
