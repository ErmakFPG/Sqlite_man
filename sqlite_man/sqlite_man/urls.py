from django.urls import path
from django.urls import re_path
from user.userViewSet import UserViewSet


urlpatterns = [
    path('user/', UserViewSet.as_view({'get': 'get_all',
                                       'post': 'create'})),
    re_path('^user/(?P<id>\d+)$', UserViewSet.as_view({'get': 'get',
                                                       'put': 'edit',
                                                       'delete': 'delete'}))
]
