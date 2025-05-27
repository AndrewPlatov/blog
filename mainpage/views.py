from django.shortcuts import render

def main(request):
    return render(
        request,               # так будет всегда
        'mainpage/main.html',  # путь к шаблону
        # здесь будут данные!
    )

def summary(request):
    return render(
        request,               # так будет всегда
        'mainpage/summary.html',  # путь к шаблону
        # здесь будут данные!
    )
    
from datetime import datetime
from . import models
def get_my_blog_posts(request):
    context = {  # Это словарь контекста, он целиком передается в страницу-шаблон
        'posts': models.Article.objects.filter(
            dt__lt=datetime(2025, 5, 21)
        )
    }
    return render(
        request,
        'article/page.html',
        context
    )