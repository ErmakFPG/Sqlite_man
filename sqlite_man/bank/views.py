from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import Bank


def create(request):
    name = request.GET.get('name', '')
    bank = Bank(name=name)
    bank.save()
    output = f'<h2>Created!</h2><h3>id: {bank.id}<br>name: {bank.name}</h3>'
    return HttpResponse(output)


def edit(request):
    bank_id = request.GET.get("id", 999)
    try:
        bank = Bank.objects.get(id=bank_id)
        bank.name = request.GET.get('name', '')
        bank.save()
        output = f'<h2>Updated!</h2><h3>id: {bank.id}<br>name: {bank.name}</h3>'
        return HttpResponse(output)
    except Bank.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")


def delete(request):
    bank_id = request.GET.get("id", 999)
    try:
        bank = Bank.objects.get(id=bank_id)
        output = f'<h2>Deleted!</h2><h3>id: {bank.id}<br>name: {bank.name}</h3>'
        bank.delete()
        return HttpResponse(output)
    except Bank.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")
