from django.urls import path
from hw_19.views import index1, index2

urlpatterns = [
    path('index1', index1, name='index1'),
    path('index2', index2, name='index2'),
]
