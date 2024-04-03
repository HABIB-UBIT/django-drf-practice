from rest_framework import serializers
from .models import student

## Validator
def start_with_h(value):
    if value[0].lower() != 'h':
        raise serializers.ValidationError('Name should be start with H')

class StudentSerializer(serializers.ModelSerializer):
     # name = serializers.CharField(max_length=100, validators= [start_with_h])   ## If you want to validate the name field this is how you can do
    # name= serializers.CharField(read_only= True)  ## We can only read the data but cannot update when read_only is true
    class Meta:
        model= student
        fields= '__all__'

        ## another way to declare read_only function on fields
        # read_only_fields= ['name']

        ## another way to declare read_only function on fields
        # extra_kwargs= {'name':{'read_only':True}}

## It has by default create and update methods
        
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