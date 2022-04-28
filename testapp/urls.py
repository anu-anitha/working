
from django.urls import path
from . import views

app_name = 'testpp'
urlpatterns = [
    
    # path('get',views.GetView),
    # path('post',views.PostView),
    path('final',views.ApiView),
]