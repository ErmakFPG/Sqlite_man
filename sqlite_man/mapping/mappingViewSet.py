import json
from django.http import JsonResponse
from .models import Mapping
from django.forms.models import model_to_dict
from rest_framework import viewsets


class MappingViewSet(viewsets.ViewSet):
    def create(self, request):
        new_mapping_data = json.loads(request.body)
        mapping = Mapping(name=new_mapping_data['name'], key=new_mapping_data['key'], value=new_mapping_data['value'])
        mapping.save()
        return JsonResponse(model_to_dict(mapping))

    def get(self, request, name, key):
        try:
            return JsonResponse({'value': model_to_dict(Mapping.objects.get(name=name, key=key))['value']})
        except Mapping.DoesNotExist:
            return JsonResponse({'error': 'Mapping not found'}, status=404)

    def get_map(self, request, name):
        result = {}
        for el in Mapping.objects.filter(name=name):
            result[el.key] = el.value
        return JsonResponse(result)

    def get_all(self, request):
        result = {}
        for el in Mapping.objects.all():
            if el.name in result:
                result[el.name][el.key] = el.value
            else:
                result[el.name] = {el.key: el.value}
        return JsonResponse(result)

    def edit(self, request, name, key):
        new_mapping_data = json.loads(request.body)
        try:
            mapping = Mapping.objects.get(name=name, key=key)
            mapping.value = new_mapping_data['value']
            mapping.save()
            return JsonResponse(model_to_dict(mapping))
        except Mapping.DoesNotExist:
            return JsonResponse({'error': 'Mapping not found'}, status=404)

    def delete(self, request, name, key):
        try:
            mapping = Mapping.objects.get(name=name, key=key)
            mapping.delete()
            return JsonResponse(model_to_dict(mapping))
        except Mapping.DoesNotExist:
            return JsonResponse({'error': 'Mapping not found'}, status=404)
