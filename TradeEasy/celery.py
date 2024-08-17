# задать стандартный модуль настроек Django
# для программы 'celery'.
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TradeEasy.settings')
app = Celery('TradeEasy')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()