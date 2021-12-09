from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

# def applicationsList(request):
#     app_ids = Application.objects.all()
#     app_serializer = ApplicationSerializer(app_ids, many=True)
#     return JsonResponse(app_serializer.data, safe=False)


class ApplicationListView(APIView):
    '''Get List of applications and post also'''
    def get(self, request):
        '''Read application using DRF'''
        app_ids = Application.objects.all()
        app_serializer = ApplicationSerializer(app_ids, many=True)
        return Response(app_serializer.data)

    def post(self, request):
        '''Create application using DRF'''
        app_serializer = ApplicationSerializer(data=request.data)
        if app_serializer.is_valid():
            app_serializer.save()
            return Response(app_serializer.data, status=status.HTTP_201_CREATED)
        return Response(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationDetailsView(APIView):
    '''Perform action on a perticular record of application'''

    def get_application_obj(self, pk):
        '''Get single object of Application by primary key'''
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''Get single object of Application'''
        application = self.get_application_obj(pk)
        app_serializer = ApplicationSerializer(application)
        return Response(app_serializer.data)

    def delete(self, request, pk):
        '''Delete single object of Application'''
        application = self.get_application_obj(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        '''Update single object of Application'''
        application = self.get_application_obj(pk)
        app_serializer = ApplicationSerializer(application, data=request.data)
        if app_serializer.is_valid():
            app_serializer.save()
            return Response(app_serializer.data)
        return Response(app_serializer.errors ,status.HTTP_400_BAD_REQUEST)
