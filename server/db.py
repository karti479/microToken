import redis
import json
from config import REDIS_HOST, REDIS_PORT

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def save_token_metadata(token_id, metadata):
    redis_client.set(token_id, json.dumps(metadata), ex=int(metadata["exp"] - metadata.get("start_time", 0)))

def get_token_metadata(token_id):
    metadata = redis_client.get(token_id)
    return json.loads(metadata) if metadata else None
