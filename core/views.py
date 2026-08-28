from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import MoodEntryForm, RegisterForm
from .models import MoodEntry
from .mood_messages import MOOD_MESSAGES
from .mood_feedback import get_mood_feedback
from django.db.models import Avg

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "core/register.html",
        {"form": form}
    )

@login_required
def get_form(requests):
    if requests.method == 'POST':
        my_form = MoodEntryForm(requests.POST)
        
        if my_form.is_valid():
            mood = my_form.save(commit=False)
            mood.user = requests.user
            mood.save()
            return redirect("success", mood_id=mood.id)
    else:
        my_form = MoodEntryForm()

    return render(
        requests,
        "core/entry_form.html",
        {"django_form": my_form}
    )
    
    

@login_required
def success(request, mood_id):
    
    mood = MoodEntry.objects.get(id=mood_id, user=request.user)
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
    

@login_required
def report(request):
    
    entries = MoodEntry.objects.filter(
        user=request.user
    )
   
    selected_date = request.GET.get("date")
    low_only = request.GET.get("low")
    high_energy = request.GET.get("high_energy")
    sort = request.GET.get("sort")
    
    if selected_date:
        entries = entries.filter(created_at__date=selected_date)
        
    if sort == "oldest":
        entries = entries.order_by("created_at")
        
    elif sort == "newest":
        entries = entries.order_by("-created_at")
        
    elif sort == "low_score":
        entries = entries.order_by("score")

    elif sort == "high_score":
        entries = entries.order_by("-score")
        
    if low_only:
        entries = entries.filter(score__lte=2)
        
    if high_energy:
        entries = entries.filter(energy_level__gte=3)
    
    avg_score = entries.aggregate(avg=Avg("score"))["avg"]
    
    return render(
        request,
        "core/report.html",
        {
            "entries": entries,
            "count": entries.count(),
            "selected_date": selected_date,
            "low_only": low_only,
            "high_energy": high_energy,
            "avg_score": avg_score,
            "sort":sort,
        }
    )
