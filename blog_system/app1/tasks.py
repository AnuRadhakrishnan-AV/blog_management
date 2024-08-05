# from celery import shared_task
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import Comment

# @shared_task
# def send_comment_notification_email(comment_id):
#     try:
#         comment = Comment.objects.get(id=comment_id)
#         post = comment.post
#         author_email = post.author.email
#         if author_email:
#             subject = 'New Comment on Your Post'
#             message = f'Hello,\n\nA new comment has been added to your post "{post.title}".\n\nComment:\n{comment.content}\n\nBest regards,\nYour Blog Team'
#             send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [author_email])
#     except Comment.DoesNotExist:
#         pass
