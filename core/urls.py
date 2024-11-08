from django.urls import path
from . import views

# http://127.0.0.1:8000/            => index sayfası 
# http://127.0.0.1:8000/index       => index sayfası 
# http://127.0.0.1:8000/about       => about sayfası 
# http://127.0.0.1:8000/scoreboard  => score Board sayfası 


urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("about", views.about),
    path("scoreboard", views.scoreBoard),

]