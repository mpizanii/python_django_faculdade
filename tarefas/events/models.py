from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def clean(self):
        if self.date is None:
            raise ValidationError('O campo de data é obrigatório.')
        if self.date < timezone.now():
            raise ValidationError('A data e hora do evento não podem estar no passado.')

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)