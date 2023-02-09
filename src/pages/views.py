from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123456,
        "my_list": [123, 'name', 20.9],
        "my_html": "<h1>hello woorld</h1>"
    }
    return render(request, "about.html", my_context)
