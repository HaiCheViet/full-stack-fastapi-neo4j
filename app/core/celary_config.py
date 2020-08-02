from celery.schedules import crontab

CELERY_IMPORTS = 'app.core.task.update_index'
CELERY_TIMEZONE = 'UTC'

# CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'schedule_back_up_every_day': {
        'task': 'app.core.task.periodic_task.back_up',
        'schedule': crontab(minute=0, hour=0)
    }
}