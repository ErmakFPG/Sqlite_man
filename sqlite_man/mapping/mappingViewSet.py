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

    def get(self, request, id):
        try:
            return JsonResponse(model_to_dict(Mapping.objects.get(id=id)))
        except Mapping.DoesNotExist:
            return JsonResponse({'error': 'Mapping not found'}, status=404)

    def get_all(self, request):
        return JsonResponse([model_to_dict(x) for x in Mapping.objects.all()], safe=False)

    def edit(self, request, id):
        new_mapping_data = json.loads(request.body)
        try:
            mapping = Mapping.objects.get(id=id)
            mapping.name = new_mapping_data['name']
            mapping.key = new_mapping_data['key']
            mapping.value = new_mapping_data['value']
            mapping.save()
            return JsonResponse(model_to_dict(mapping))
        except Mapping.DoesNotExist:
            return JsonResponse({'error': 'Mapping not found'}, status=404)

    def delete(self, request, id):
        try:
            mapping = Mapping.objects.get(id=id)
            mapping.delete()
            return JsonResponse(model_to_dict(mapping))
        except Mapping.DoesNotExist:
            return JsonResponse({'error': 'Mapping not found'}, status=404)
