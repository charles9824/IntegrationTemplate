from django.shortcuts import render

from website.models import BlogArticles


# Create your views here.
def index_website(request):
    post = BlogArticles.objects.all()
    return render(request, 'index.html', context={'post':post})

def about(request):
    return render(request, 'about.html')

def readmore(request, id):
    article =BlogArticles.objects.filter(id=id)

    return render(request, 'readmore.html', context={'article':article})
