from rest_framework import viewsets

from live.models import Program
from live.serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
