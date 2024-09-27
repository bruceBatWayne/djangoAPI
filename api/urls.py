from django.urls import path
from .views import  *
urlpatterns = [
    path('<int:pk>',profileView.as_view()),
    path('',profileView.as_view())

    
]
