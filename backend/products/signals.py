from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=User)
def notify_user_created(sender, instance, created, **kwargs):
    if created:
        print("📢 User создан через Postman!")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": {
                    "text": f"Создан новый пользователь: {instance.username}"
                }
            }
        )

