import uuid
from django.db import models


class Topic(models.Model):
    id = models.AutoField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'Topics'
        ordering = ['created_at']
