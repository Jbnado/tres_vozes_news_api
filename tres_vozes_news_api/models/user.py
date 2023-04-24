import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    admin = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, unique=True)
    password = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cpf

    class Meta:
        db_table = 'Users'
        ordering = ['created_at']
