from django.shortcuts import render, redirect
from rango.models import Category
from django.http import HttpResponse
from rango.models import Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm


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
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # have we been provided with a valid form?
        if form.is_valid():
            # save the new category to the database
            category = form.save(commit=True)
            print(category)
            return index(request)
        else:
            print(form.errors)

    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except  Category.DoesNotExist:
        cat = None

    print('cat'+cat.__str__())
    if request.method == 'POST':
        form = PageForm(request.POST)
        if (form.is_valid()):
            page = form.save(commit=False)
            page.category = cat
            page.views = 0
            page.save()
            ##redirect to new page
            return redirect('category', category_name_slug)
        else:
            print(form.errors)

    else:
        form= PageForm()
    context_dict={'form':form,'category':cat}
    return render(request,'rango/add_page.html',context_dict)

def register(request):
    registered=False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
          user=  user_form.save()
          user.set_password=(user.password)
          user.save()

          profile=profile_form.save(commit=False)
          profile.user=user

          if  'picture' in request.FILES :
              profile.picture=request.FILES['picture']

              profile.save()
              registered=True


        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'rango/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
