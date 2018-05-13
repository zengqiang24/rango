from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse
from rango.models import Page
from rango.forms import CategoryForm


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    category_views_list = Category.objects.order_by('-views')[:5]
    context_dict['category_views_list'] = category_views_list
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {"about": "this is qiang blogs"}
    return render(request, 'rango/about.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        page = Page.objects.filter(category=category)
        context_dict['pages'] = page
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


def add_category(request):

    if request.method=='POST':
        form=CategoryForm(request.POST)
        #have we been provided with a valid form?
        if form.is_valid():
            #save the new category to the database
            category=form.save(commit=True)
            print(category)
            return index(request)
        else:
            print(form.errors)

    else:
        form=CategoryForm()


    return render(request,'rango/add_category.html',{'form':form})
