from . import views
from django.urls import  path


urlpatterns = [
    path('', views.win),
    path('root_privilege', views.root_privilege)
    ]