from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
from datetime import  datetime

@shared_task
def horario():
    print("->>>>> Horário: ", datetime.now())



@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="celery_test",
    ignore_result=True
)
def teste():
    print("-----------------------")