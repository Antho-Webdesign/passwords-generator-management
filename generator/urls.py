from django.urls import path, include
from generator.views import home, listall, deleterecord, search

urlpatterns = [
    path('', home, name='home'),
    path('listall/', listall, name="listall"),
    path('delete/<int:id>', deleterecord, name="deleterecord"),
    path('search', search, name="search"),
]
