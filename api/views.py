from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import UsersBot, Mavzu
from .serializers import BotUserSerializer, CreateDataForSearchSerializer, CreateDataSerializer


# Create your views here.


class CreateDataView(GenericAPIView):
    serializer_class = CreateDataSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=200)


class DataListView(APIView):
    serializer_class = CreateDataSerializer

    def get(self, request):
        data = Mavzu.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class BotUserView(GenericAPIView):
    serializer_class = BotUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=200)


class BotUserListView(APIView):
    serializer_class = BotUserSerializer

    def get(self, request):
        queryset = UsersBot.objects.values_list('user_id', flat=True)
        return Response(queryset)


class UserListView(APIView):
    serializer_class = BotUserSerializer

    def get(self, request):
        data = UsersBot.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class SearchView(ListAPIView):
    queryset = Mavzu.objects.all()
    serializer_class = CreateDataForSearchSerializer
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('savol',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('savol', None)
        if query is not None:
            queryset = queryset.filter(savol__icontains=query)
        return queryset


class GetDataView(APIView):
    serializer_class = CreateDataForSearchSerializer

    def get(self, request, savol_id):
        try:
            queryset = Mavzu.objects.get(savol_id=savol_id)
            data = self.serializer_class(queryset)
            return Response(data.data)
        except:
            return Response(status=400)
