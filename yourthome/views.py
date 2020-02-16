from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import *
from rest_framework import status

class TypeView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAdminUser,)


class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        file_serializer = ImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AnnouncementView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Apartment.objects.all()
    permission_classes = (permissions.AllowAny,)


class ApartmentView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)



class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class ApartmentsTypeView(generics.RetrieveAPIView):
    model = Type
    queryset = Type.objects.all()
    permission_classes = (permissions.AllowAny,)
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        types = Apartment.objects.filter(type_id=instance.id)
        serializer = ApartmentSerializer(types, many=True)
        return Response(serializer.data)


class AddressView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

