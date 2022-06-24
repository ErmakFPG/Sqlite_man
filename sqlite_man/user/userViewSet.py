import json
from django.http import JsonResponse
from .models import User
from django.forms.models import model_to_dict
from rest_framework import viewsets


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        new_user_data = json.loads(request.body)
        user = User(name=new_user_data['name'])
        user.save()
        return JsonResponse(model_to_dict(user))

    def get(self, request, id):
        try:
            return JsonResponse(model_to_dict(User.objects.get(id=id)))
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    def get_all(self, request):
        return JsonResponse([model_to_dict(x) for x in User.objects.all()], safe=False)

    def edit(self, request, id):
        new_user_data = json.loads(request.body)
        try:
            user = User.objects.get(id=id)
            user.name = new_user_data['name']
            user.save()
            return JsonResponse(model_to_dict(user))
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse(model_to_dict(user))
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
