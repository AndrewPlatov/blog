from django.shortcuts import render

def main(request):
    return render(
        request,               # так будет всегда
        'mainpage/article.html',  # путь к шаблону
        # здесь будут данные!
    )
