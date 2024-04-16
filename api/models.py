from django.db import models
import random
# Create your models here.


class UsersBot(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.PositiveBigIntegerField()
    created = models.CharField(max_length=100)


class Qism(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bolim(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mavzu(models.Model):
    qism = models.ForeignKey(Qism, on_delete=models.CASCADE, related_name='qism')
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, related_name='bolim')
    savol = models.TextField()
    javob = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    savol_id = models.PositiveIntegerField(default=random.randint(10000, 99999), unique=True)

    def __str__(self):
        return self.savol
