
from django.shortcuts import render
from django.views.generic import TemplateView
from . models import Python_Video
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'python_playlist/python.html'



 


def python_list(request):
    # item=get_object_or_404(Item,pk=item_id)
    videos=Python_Video.objects.all()
    return render(request,'python_playlist/python.html',{'videos':videos}) 

def python_notes_page(request):
     video=input()
     
     return render(request,f'python_playlist/{video}.html')