
from django.urls import path

from .views import about,listing

urlpatterns = [
    # path("about",about.as_view(),name="about"),
    path('about/', about.as_view(), name='about'),
    path('',listing.as_view(),name='listing'),
    
    
    # path('about',about, name='about'),  # Corrected path for about
]
