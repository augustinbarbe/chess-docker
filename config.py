DEBUG = False

# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

# Redis configuration for pubsub notifications
REDIS_URL = "redis://localhost:6379/2"
