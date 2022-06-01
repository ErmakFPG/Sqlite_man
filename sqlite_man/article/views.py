from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import Article


def create(request):
    name = request.GET.get('name', '')
    article = Article(name=name)
    article.save()
    output = f'<h2>Created!</h2><h3>id: {article.id}<br>name: {article.name}</h3>'
    return HttpResponse(output)


def edit(request):
    article_id = request.GET.get("id", 999)
    try:
        article = Article.objects.get(id=article_id)
        article.name = request.GET.get('name', '')
        article.save()
        output = f'<h2>Updated!</h2><h3>id: {article.id}<br>name: {article.name}</h3>'
        return HttpResponse(output)
    except Article.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")


def delete(request):
    article_id = request.GET.get("id", 999)
    try:
        article = Article.objects.get(id=article_id)
        output = f'<h2>Deleted!</h2><h3>id: {article.id}<br>name: {article.name}</h3>'
        article.delete()
        return HttpResponse(output)
    except Article.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")
