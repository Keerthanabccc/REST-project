from django.urls import path
from .views import *

urlpatterns=[
    path('first/',todosview.as_view()),
    path('sell/',tododetails),
    path('second/',moviesview.as_view())

]
