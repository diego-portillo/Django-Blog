from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list(request):
    # la funcion render imprime la info recibida en request usando la plantilla de django, con la url blog/post_list.html
    return render(request, 'blog/post_list.html', {})
