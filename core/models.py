from django.db import models

class MoodEntry(models.Model):
    score = models.IntegerField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField()
    energy_level = models.IntegerField()
    
    def __str__(self):
        return f"{self.score} - {self.created_at}"