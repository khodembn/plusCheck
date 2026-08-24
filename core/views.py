from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import MoodEntryForm
from .models import MoodEntry
from .mood_messages import MOOD_MESSAGES
from .mood_feedback import get_mood_feedback

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def get_form(requests):
    if requests.method == 'POST':
        my_form = MoodEntryForm(requests.POST)
        
        if my_form.is_valid():
            mood = my_form.save()
            return redirect("success", mood_id=mood.id)
    else:
        my_form = MoodEntryForm()

    return render(
        requests,
        "core/entry_form.html",
        {"django_form": my_form}
    )
    
    

def success(request, mood_id):
    
    mood = MoodEntry.objects.get(id=mood_id)
    message = MOOD_MESSAGES.get(mood.score)
    feedback = get_mood_feedback(mood.score)
    
    return render(
        request,
        "core/success.html",
        {
            "mood": mood,
            "message": message, 
            "feedback": feedback, 
        }
        
    )