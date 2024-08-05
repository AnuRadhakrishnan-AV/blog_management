from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
# from .tasks import send_comment_notification_email

from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Comment)
def send_comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        author_email = post.author.email
        if author_email:
            subject = 'New Comment on Your Post'
            message = f'Hello,\n\nA new comment has been added to your post "{post.title}".\n\nComment:\n{instance.content}\n\nBest regards,\nYour Blog Team'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [author_email])




