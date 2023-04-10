from rest_framework import viewsets

from lives.models import Program
from lives.serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        search_title = self.request.query_params.get('title')
        if search_title:
            qs = qs.filter(title__icontains=search_title)  # title__contains: 대소문자 구분할 경우

        return qs
