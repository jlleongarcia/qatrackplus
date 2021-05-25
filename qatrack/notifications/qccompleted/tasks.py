from django.conf import settings

from qatrack.qa.models import TestListInstance
from qatrack.qatrack_core.email import send_email_to_users


def send_follow_up_email(*args, **kwargs):
    """Task to do the actual sending of the follow up emails"""

    test_list_instance_id = args[0] if args else None
    notification_id = args[1] if len(args) > 1 else None

    from qatrack.notifications.models import QCCompletedNotice

    tli = TestListInstance.objects.filter(pk=test_list_instance_id).first()
    sub = QCCompletedNotice.objects.filter(id=notification_id).first()
    if not (tli and sub):
        return

    recipients = sub.recipients.recipient_emails()
    context = {
        'notice_type': "follow_up",
        'test_list_instance': tli,
    }
    template = getattr(settings, "EMAIL_NOTIFICATION_TEMPLATE", "notification_email.html")
    subject_template = getattr(settings, "EMAIL_NOTIFICATION_SUBJECT_TEMPLATE", "notification_email_subject.txt")

    send_email_to_users(recipients, template, context, subject_template=subject_template)
