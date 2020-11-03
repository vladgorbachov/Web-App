from django.urls import path
from publications import views

app_name = 'publications'

urlpatterns = [

    path('add/', views.add_publication),
    path('show/', views.publication_show),
    path('show/<slug>', views.get_publication),
    path('edit/<slug>', views.edit_publication)]