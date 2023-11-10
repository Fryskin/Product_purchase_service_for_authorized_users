# Product purchase service for authorized users

How to use:
1. Perform 'uvicorn src.main:app --reload' 
2. Run redis-server.exe from https://github.com/tporadowski/redis/releases (Redis-x64-5.0.14.1.zip)
3. Run celery and flower 'celery -A src.tasks.tasks:celery worker --loglevel=INFO --pool=solo' and 'celery -A src.tasks.tasks:celery flower'
4. Go to the http://127.0.0.1:8000/docs/