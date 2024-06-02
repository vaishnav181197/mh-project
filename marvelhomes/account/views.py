from django.shortcuts import render
from django.views.generic import CreateView,FormView,TemplateView
# Create your views here.
from django.views import View


def mainpage(request):
    return render(request, 'mainpage.html')




class about(View):
    def get(self,request):
        # print('about view called')
       
        return render (request,"about.html")
  

class listing(View):
    def get(self,request):
        # print('about view called')
       
        return render (request,"listing.html")