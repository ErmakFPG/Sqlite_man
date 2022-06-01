from django.urls import path
from user import views as user_views
from article import views as article_views
from bank import views as bank_views


urlpatterns = [
    path('create_user/', user_views.create),
    path('edit_user/', user_views.edit),
    path('delete_user/', user_views.delete),
    path('create_article/', article_views.create),
    path('edit_article/', article_views.edit),
    path('delete_article/', article_views.delete),
    path('create_bank/', bank_views.create),
    path('edit_bank/', bank_views.edit),
    path('delete_bank/', bank_views.delete)
]
