from django.core.mail import send_mail
from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


def send_email(subject, content, from_, to_):
    send_mail(subject, content, from_, [to_])


@task(name="send_email")
def send_email_async(subject, content, from_, to_):
    logger.info("Sent email")
    send_email(subject, content, from_, to_)
