 
from django.urls import path,include
from . import views

urlpatterns = [
     
    # path('', views.HomePageView.as_view(), name='python'),
    # path('/<>',views.python_playlist,name='pvideo'),
    path('',views.python_list,name='python'),
    path('/launch',views.python_notes_page,name='launch')

]