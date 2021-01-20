from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    # auto_now_add: Establece la fecha del día correspondiente.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
