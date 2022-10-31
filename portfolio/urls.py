from django.urls import path

from portfolio.views import eco_demenagement, index, pizzeria, category_list, category_detail

urlpatterns = [
    path('', index, name='index_portfolio'),
    path('projet/eco_demenagement/', eco_demenagement, name="eco-demenagement"),
    path('projet/pizzeria/', pizzeria, name="pizzeria"),
    path('liste/category/', category_list, name="category_list"),
    path('liste/category/<slug:slug>/', category_list, name="project_category_list"),
    path('detail/category/<slug:slug>/', category_detail, name="project_category_detail"),

]
