from django.shortcuts import render, redirect
from .models import Goals

# This function create to a render where its gonna call a template (templates)
def list_goals(request):
    goals = Goals.objects.all()
    return render(request, 'list_goals.html', {'goals': goals})

def create_goals(request):
    # This for saving info in the database calling the class in models
    goal = Goals(title=request.POST['title'], description=request.POST['description'])
    goal.save()
    return redirect('/goals/')

def delete_goals(request, goal_id):
    goal = Goals.objects.get(id=goal_id)
    goal.delete()
    return redirect('/goals/')

