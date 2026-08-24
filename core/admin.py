from django.contrib import admin
from core.models import MoodEntry

@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ("score", "energy_level", "created_at")
    search_fields = ("reason",)
    list_filter = ("score",)