from db import redis_client

def propagate_revocation(token_id, reason):
    redis_client.publish("token-revocation", f"Token {token_id} revoked: {reason}")
