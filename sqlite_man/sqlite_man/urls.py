from django.urls import path
from django.urls import re_path
from user.userViewSet import UserViewSet
from money_cell.moneyCellViewSet import MoneyCellViewSet


urlpatterns = [
    path('user/', UserViewSet.as_view({'get': 'get_all',
                                       'post': 'create'})),
    re_path('^user/(?P<id>\d+)$', UserViewSet.as_view({'get': 'get',
                                                       'put': 'edit',
                                                       'delete': 'delete'})),
    path('money_cell/', MoneyCellViewSet.as_view({'get': 'get_all',
                                                  'post': 'create'})),
    re_path('^money_cell/(?P<id>\d+)$', MoneyCellViewSet.as_view({'get': 'get',
                                                                  'put': 'edit',
                                                                  'delete': 'delete'}))
]
