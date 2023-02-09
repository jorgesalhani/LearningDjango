from django.shortcuts import render
from .models import Product
from .forms import ProductCreateForm
from .forms import RawProductForm

# Create your views here.


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "products/product_create.html", context)


# Render with pure FORM
###
# def product_create_view(request):
#     print(request.POST)
#     context = {}
#     return render(request, 'products/product_create.html', context)

# Render with Django
###
# def product_create_view(request):
#     form = ProductCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductCreateForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
