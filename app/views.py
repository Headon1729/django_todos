from django.core.serializers import serialize
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Todo
from rest_framework import generics
from .serializer import TodoSerializer


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def hello(request):
    return HttpResponse('Ok')


def _handle_get_todo(id=None) -> Response:
    if id == None:
        return Response([])
    return Response({})


def _handle_create_todo(todo: dict) -> Response:
    return Response({'message': 'success'}, status=201)


def _handle_update_todo(id: str) -> Response:
    return Response({})


def _handle_delete_todo(id) -> Response:
    item = Todo.objects.get(id)
    item.delete()
    return Response("deleted")


@api_view()
def todos(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def todo(request, id):
    if request.method == 'GET':
        return _handle_get_todo(id)
    elif request.method == 'POST':
        return _handle_create_todo(request.data)
    elif request.method == 'PUT':
        return _handle_update_todo(id)
    elif request.method == 'DELETE':
        return _handle_delete_todo(id)
    return Response('OKAY')
