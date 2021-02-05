from django.urls import path
from . import views

urlpatterns = [
	path('',views.check,name='check'),
	path('agecheck',views.agecheck,name='agecheck'),
	path('y',views.young,name='young'),
	path('o',views.old,name='old'),


]