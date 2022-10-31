from django.shortcuts import render

from portfolio.models import Project


# Index
def index(request):
    return render(request, 'portfolio/index.html')


def project_category(request):
    return render(request, 'portfolio/projets/category/project_category.html')


# Eco
def eco_demenagement(request):
    return render(request, 'portfolio/projets/eco-demenagement.html')


def pizzeria(request):
    return render(request, 'portfolio/projets/pizzeria.html')


def category_list(request):
    queryset = Project.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'portfolio/projets/category/list_category.html', context)


def category_detail(request, slug):
    queryset = Project.objects.filter(slug=slug)
    context = {
        'project_list': queryset
    }
    return render(request, 'portfolio/projets/category/project_category.html', context)
