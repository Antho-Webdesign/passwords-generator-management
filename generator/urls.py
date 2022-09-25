from django.urls import path, include
from generator.views import home, listall, deleterecord, search, home_test

urlpatterns = [
    path('', home, name="home"),
    path('listall/', listall, name="listall"),
    path('delete/<int:id>', deleterecord, name="deleterecord"),
    path('search', search, name="search"),
    # path('home-test/', home_test, name="home_test"),
]
