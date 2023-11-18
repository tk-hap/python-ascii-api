import redis
from ..config import settings

try:
    r = redis.Redis(host=settings.db_host, port=settings.db_port, decode_responses=True)

except redis.ConnectionError:
    print(f"Database connection failed for {settings.db_host}:{settings.db_port}")
    exit()

