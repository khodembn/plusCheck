from django.db import models
from django.contrib.auth.models import User
class MoodEntry(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="mood_entries")
    score = models.IntegerField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100)
    energy_level = models.IntegerField()

    
    def __str__(self):
        return f"{self.score} - {self.created_at}"