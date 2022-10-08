from django.shortcuts import render, redirect
from api.models import Api
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def registration(req):
    data1 = req.data
    Api(name = data1['name'], password = data1['password'], email = data1['email']).save()  #here the ['name'],['email'],.. refers to the names used in forms for accessing data
    return Response("Registered")

@api_view(['GET'])
def display(req):
    a = Api.objects.all()
    b = [{'id': i.id, 'name': i.name, 'password': i.password, 'email': i.email}for i in a]
    return Response(b)

@api_view(['DELETE'])
def delete(req, id):
    Api.objects.get(id = id).delete()
    return Response("Deleted")
