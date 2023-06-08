from django.urls import path
from .views import top_5_states

urlpatterns = [
    path('top-5-states/', top_5_states, name='top_5_states'),
]
