from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from parents.models import Parents
from parents.serializers import ParentsSerializers
from utils.ApiResponse import ApiResponse


# Create your views here.

class ParentsView(viewsets.ModelViewSet):
    queryset = Parents.objects.all()

    serializer_class = ParentsSerializers
    # pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        response = ApiResponse()
        data = list(Parents.objects.all().values())
        response.setStatusCode(status.HTTP_200_OK)
        response.setMessage("Found")
        response.setEntity(data)
        return Response(response.toDict(), status=response.status)

    def create(self, request, *args, **kwargs):
        response = ApiResponse()
        ParentsData = ParentsSerializers(data=request.data)

        if not ParentsData.is_valid():
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Please fill in the details correctly.", "status": status_code}, status_code)

        # Check if the email is already in use
        checkIdno = request.data.get("parentIdno")
        existingparent = Parents.objects.filter(parentIdno=checkIdno).first()

        if existingparent:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Parents  already exists.", "status": status_code}, status_code)

        # If email is not in use, save the new customer
        ParentsData.save()
        response.setStatusCode(status.HTTP_201_CREATED)
        response.setMessage("Parent created")
        response.setEntity(request.data)
        return Response(response.toDict(), status=response.status)

    def destroy(self, request, *args, **kwargs):

        regionData = Parents.objects.filter(id=kwargs['pk'])
        if regionData:
            regionData.delete()
            status_code = status.HTTP_200_OK
            return Response({"message": "Users deleted Successfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Users data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        users_details = Parents.objects.get(id=kwargs['pk'])
        users_serializer_data = ParentsSerializers(
            users_details, data=request.data, partial=True)
        if users_serializer_data.is_valid():
            users_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Users Update Successfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Users data Not found", "status": status_code})


