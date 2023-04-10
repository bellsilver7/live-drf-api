from rest_framework import serializers

from lives.models import Program, STREAM_STATUS_CHOICES


# Serializers define the API representation.
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
