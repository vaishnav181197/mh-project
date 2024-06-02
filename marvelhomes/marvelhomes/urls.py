from django.contrib import admin
from django.urls import path,include
from account.views import mainpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainpage, name=''),
    path('account/',include('account.urls')),
    
]
