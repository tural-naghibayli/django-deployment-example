from django.urls import path,include
from basic_app_tn import views
# or from .  basic_app_tn import views

#Template Tagging
app_name = 'basic_app_tn'


urlpatterns =[
    path('relative/',views.relative, name='relative'),
    path('other/',views.other, name='other')
]
