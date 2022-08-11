from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('show-all-candidate/',views.showall, name='show-all-candidate'),
    path('candidate-info/<str:pk>/',views.candidate_info, name='candidate-info'),
    path('react/',views.react, name='react'),
    path('read/',views.readfile, name='read'),
    path('accept_or_reject/<str:pk>/',views.accept_or_reject, name='accept_or_reject'),
]

