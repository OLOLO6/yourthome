from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'image',)



class ApartmentsTypeSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True)

    class Meta:
        model = Apartment
        fields = ('types',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('house_number', 'street', 'city', 'postcode', 'country', 'country_code')


class ApartmentSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    image = ImageSerializer(many=True)

    class Meta:
        model = Apartment
        fields = (
            'id', 'type', 'room', 'square', 'address', 'date_of_arrival', 'date_of_departure', 'price', 'description',
            'status', 'pub_date', 'image', 'owner', 'latitude', 'longitude')

class AnnouncementSerializer(serializers.ModelSerializer):
    address=AddressSerializer(many=False)
    class Meta:
        model = Apartment
        fields = ('type', 'room', 'address', 'square', 'date_of_arrival', 'date_of_departure', 'price', 'description',
            'status', 'pub_date', 'image', 'owner')
