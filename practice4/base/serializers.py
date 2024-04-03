from rest_framework import serializers
from .models import student

## Validator

def start_with_h(value):
    if value[0].lower() != 'h':
        raise serializers.ValidationError('Name should be start with H')

class StudentSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=100, validators= [start_with_h])   ## If you want to validate the name field this is how you can do
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100, default='Unknown')

    def create(self, validated_data):
        return student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.roll= validated_data.get('roll', instance.roll)
        instance.city= validated_data.get('city', instance.city)
        instance.save()
        return instance

    ## Field Level Validation
    def validate_roll(self, value):
        if value >= 201:
            raise serializers.ValidationError('Seat Full')
        return value
    
    ## Object Level Validation
    def validate(self, data):  ## Here data is a python dictionary of fields value
        city= data.get('city')   ## Dictionary of city values within the serializer
        if city != 'karachi':       ## Any condition can be written here
            raise serializers.ValidationError('Only Karachi Peoples can be inserted')
        return data 