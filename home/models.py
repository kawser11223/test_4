from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)  # User points
    referred_count = models.PositiveIntegerField(default=0) 
    referral_code = models.CharField(max_length=50, unique=True, null=True, blank=True)  
    

    def save(self, *args, **kwargs):
        
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4()).replace('-', '')[:10]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    title = models.CharField(max_length=255)  
    secret_code = models.CharField(max_length=50)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.task.title}"

class User_Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    w_amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.TextField(default="")


    def __str__(self):
        return f"{self.user.username} - {self.w_amount}"