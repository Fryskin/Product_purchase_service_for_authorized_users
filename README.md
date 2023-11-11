# Product purchase service for authorized users

How to use:
1. Perform 'venv/Scripts/activate'
2. Perform 'uvicorn src.main:app --reload' 
3. Run redis-server.exe using 'start redis/redis-server.exe'
4. Run celery and flower 'celery -A src.tasks.tasks:celery worker --loglevel=INFO --pool=solo' and 'celery -A src.tasks.tasks:celery flower'
5. Go to the http://127.0.0.1:8000/docs/