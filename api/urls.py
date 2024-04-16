from django.urls import path

from .views import CreateDataView, BotUserView, BotUserListView, DataListView, SearchView, GetDataView, UserListView

urlpatterns = [
    path('createdata', CreateDataView.as_view(), name='createdata'),
    path('botuser', BotUserView.as_view(), name='botuser'),
    path('botuserlist', BotUserListView.as_view(), name='botuserlist'),
    path('users', UserListView.as_view(), name='users'),
    path('datalist', DataListView.as_view(), name='datalist'),
    path('search', SearchView.as_view(), name='search'),
    path('getdata/<int:savol_id>', GetDataView.as_view(), name='getdata'),
]
