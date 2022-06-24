import json
from django.http import JsonResponse
from django.db import IntegrityError
from .models import MoneyCell
from django.forms.models import model_to_dict
from rest_framework import viewsets


class MoneyCellViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            new_money_cell_data = json.loads(request.body)
            money_cell = MoneyCell(user_id=new_money_cell_data['user_id'],
                                   name=new_money_cell_data['name'])
            money_cell.save()
            return JsonResponse(model_to_dict(money_cell))
        except IntegrityError:
            return JsonResponse({'error': 'Owner not found'}, status=404)

    def get(self, request, id):
        try:
            return JsonResponse(model_to_dict(MoneyCell.objects.get(id=id)))
        except MoneyCell.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    def get_all(self, request):
        return JsonResponse([model_to_dict(x) for x in MoneyCell.objects.all()], safe=False)

    def edit(self, request, id):
        new_money_cell_data = json.loads(request.body)
        try:
            money_cell = MoneyCell.objects.get(id=id)
            money_cell.name = new_money_cell_data['name']
            money_cell.save()
            return JsonResponse(model_to_dict(money_cell))
        except MoneyCell.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    def delete(self, request, id):
        try:
            money_cell = MoneyCell.objects.get(id=id)
            money_cell.delete()
            return JsonResponse(model_to_dict(money_cell))
        except MoneyCell.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
