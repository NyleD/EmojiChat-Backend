
from .utils import validate_message_content
import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils import timezone


class User(AbstractUser):

    last_read_date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False
    )
    online = models.BooleanField(null=False, blank=False, default=False)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def read(self):
        self.last_read_date = timezone.now()
        self.save()

    def unread_messages(self):
        return Message.objects.filter(created_at__gt=self.last_read_date).count()

class Message(models.Model):

    id = models.UUIDField(
        primary_key=True,
        null=False,
        default=uuid.uuid4,
        editable=False
    )
    author = models.ForeignKey(
        'User',
        blank=False,
        null=False,
        related_name='author_messages',
        on_delete=models.CASCADE
    )
    content = models.TextField(validators=[validate_message_content])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def last_50_messages():
        return Message.objects.order_by('-created_at').all()[:50]

