from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.db import IntegrityError
from .models import MoneyCell
from user.models import User


def create(request):
    owner_id = request.GET.get('user_id', 1)
    money_cell_name = request.GET.get('name', '')
    try:
        money_cell = MoneyCell(name=money_cell_name, user_id=owner_id)
        money_cell.save()
        owner = User.objects.get(id=owner_id)
        output = f'<h2>Created!</h2><h3>id: {money_cell.id}<br>name: {money_cell.name}<br>' \
                 f'owner name: {owner.name}</h3>'
        return HttpResponse(output)
    except IntegrityError:
        return HttpResponseNotFound("<h2>Owner not found</h2>")


def edit(request):
    money_cell_id = request.GET.get("id", 999)
    try:
        money_cell = MoneyCell.objects.get(id=money_cell_id)
        money_cell.name = request.GET.get('name', '')
        money_cell.save()
        output = f'<h2>Updated!</h2><h3>id: {money_cell.id}<br>name: {money_cell.name}</h3>'
        return HttpResponse(output)
    except MoneyCell.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")


def delete(request):
    money_cell_id = request.GET.get("id", 999)
    try:
        money_cell = MoneyCell.objects.get(id=money_cell_id)
        output = f'<h2>Deleted!</h2><h3>id: {money_cell.id}<br>name: {money_cell.name}</h3>'
        money_cell.delete()
        return HttpResponse(output)
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")
