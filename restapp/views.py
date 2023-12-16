from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializer import *

# Create your views here.




# ---------------------API view------------------------
#  rest framework provides an API view class
# it allows us to define functions that match standard http
# methods like get,post,put and delete





class todosview(APIView):
    def post(self,request):
        a=todoserializer(data=request.data)
        if a.is_valid():
            a.save()
        return Response(a.data)
    def get(self,request):
        qs=todos.objects.all()
        a=todoserializer(qs,many=True)
        return Response(a.data)


#
#
# class moviesview(APIView):
#     def post(self,request):
#         a=movieserializer(data=request.data)
#         if a.is_valid():
#             a.save()
#         return Response(a.data)
#     def get(self,request):
#         qs=movies.objects.all()
#         a=movieserializer(qs,many=True)
#         return Response(a.data)
#
#
#






# with using ID---------------------------
#

class tododetails(APIView):
    def get(self,request,**kwargs):
        todo=todos.objects.get(id=kwargs.get('pk'))
        a=todoserializer(todo)
        return Response(a.data)

    #update-----------------
    def put(self,request,**kwargs):
        todo=todos.objects.get(id=kwargs.get('pk'))
        a=todoserializer(instance=todo,data=request.data)
        if a.is_valid():
            a.save()
        return Response(a.data)



    def delete(self,request,**kwargs):
        todo=todos.objects.get(id=kwargs.get('pk'))
        todo.delete()
        return Response({'msg':'deleted'})












