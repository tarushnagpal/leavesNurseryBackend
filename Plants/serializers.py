from rest_framework import serializers
from Plants.models import Plant

class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ('binomial_name', 'indian_name', 'is_featured', 'image_url')
