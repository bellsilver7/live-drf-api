from rest_framework import serializers

from live.models import Program


# Serializers define the API representation.
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
        # fields = ('id', 'title', 'description')
