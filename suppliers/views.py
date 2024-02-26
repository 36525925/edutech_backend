from rest_framework import viewsets, status
from rest_framework.response import Response
from suppliers.models import Suppliers
from suppliers.serializers import SuppliersSerializers
from utils.ApiResponse import ApiResponse

class SuppliersView(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializers

    def list(self, request, *args, **kwargs):
        response = ApiResponse()
        suppliers_data = Suppliers.objects.all().values()
        response.setStatusCode(status.HTTP_200_OK)
        response.setMessage("Found")
        response.setEntity(list(suppliers_data))
        return Response(response.toDict(), status=response.status)

    def create(self, request, *args, **kwargs):
        response = ApiResponse()
        suppliers_data = SuppliersSerializers(data=request.data)
        if suppliers_data.is_valid():
            check_id = request.data.get("supplierId")
            existing_supplier = Suppliers.objects.filter(id=check_id).first()
            if existing_supplier:
                status_code = status.HTTP_400_BAD_REQUEST
                return Response({"message": "Supplier already exists.", "status": status_code}, status_code)
            suppliers_data.save()
            response.setStatusCode(status.HTTP_201_CREATED)
            response.setMessage("Supplier created")
            response.setEntity(request.data)
            return Response(response.toDict(), status=response.status)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Please fill in the details correctly.", "status": status_code}, status_code)

    def destroy(self, request, *args, **kwargs):
        supplier_data = Suppliers.objects.filter(id=kwargs['pk'])
        if supplier_data:
            supplier_data.delete()
            status_code = status.HTTP_200_OK
            return Response({"message": "Supplier deleted successfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Supplier data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        supplier_details = Suppliers.objects.filter(id=kwargs['pk']).first()
        if supplier_details:
            suppliers_serializer_data = SuppliersSerializers(
                supplier_details, data=request.data, partial=True)
            if suppliers_serializer_data.is_valid():
                suppliers_serializer_data.save()
                status_code = status.HTTP_201_CREATED
                return Response({"message": "Supplier updated successfully", "status": status_code})
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                return Response({"message": "Supplier data not found", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Supplier data not found", "status": status_code})
