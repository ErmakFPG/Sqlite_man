from django.urls import path
from user import views


urlpatterns = [
    path('create_user/', views.create),
    path('edit_user/', views.edit),
    path('delete_user/', views.delete)
]
