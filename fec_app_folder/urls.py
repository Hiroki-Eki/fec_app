from django.urls import path
from . import views

app_name = 'fec_app_folder'
urlpatterns = [
    path('top_page/', views.top_page, name='top_page')
]