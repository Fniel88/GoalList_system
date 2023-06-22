# Here I defined which urls are related to goals
from django.urls import path
from .views import list_goals, create_goals, delete_goals
urlpatterns = [
    # Which funtion its gonna execute, it has a black since
    # the default url gonna be list_goals
    path('', list_goals),
    path('new/', create_goals, name='create_goal'),
    path('delete_goal/<int:goal_id>/', delete_goals, name='delete_goal')
]