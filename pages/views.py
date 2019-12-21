from django.shortcuts import render

def home(request):

    template = "pages/home.html"
    context = {}
    return render(request, template, context)

