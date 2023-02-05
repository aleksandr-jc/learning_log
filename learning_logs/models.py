from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """Тема, яку вивчає користувач."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Повернути рядкове представлення моделі."""
        return self.text

class Entry(models.Model):
    """Якасть конкретна інформація до цієї теми."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Повертає представленя моделі у string."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return f"{self.text[:]}"

