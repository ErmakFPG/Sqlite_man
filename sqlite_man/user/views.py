from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import User


def create(request):
    name = request.GET.get('name', '')
    user = User(name=name)
    user.save()
    output = f'<h2>Created!</h2><h3>id: {user.id}<br>name: {user.name}</h3>'
    return HttpResponse(output)


def edit(request):
    user_id = request.GET.get("id", 999)
    try:
        user = User.objects.get(id=user_id)
        user.name = request.GET.get('name', '')
        user.save()
        output = f'<h2>Updated!</h2><h3>id: {user.id}<br>name: {user.name}</h3>'
        return HttpResponse(output)
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")


def delete(request):
    user_id = request.GET.get("id", 999)
    try:
        user = User.objects.get(id=user_id)
        output = f'<h2>Deleted!</h2><h3>id: {user.id}<br>name: {user.name}</h3>'
        user.delete()
        return HttpResponse(output)
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")
