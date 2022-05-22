from django.http import HttpResponse
from rest_framework import views
from rest_framework.response import Response

from create_proj.models import BackEndChoices, FrontEndChoices, DatabaseChoices
from create_proj.serializers import ProjectChoicesSerializer, ProjectSerializer
from create_proj.helpers import create_project_archive


class ProjectChoicesView(views.APIView):
    """."""

    serializer_class = ProjectChoicesSerializer

    def get(self, request, *args, **kwargs):
        """."""

        serializer = self.serializer_class({
            "backend": {item[0]: item[1] for item in BackEndChoices.choices},
            "frontend": {item[0]: item[1] for item in FrontEndChoices.choices},
            "database": {item[0]: item[1] for item in DatabaseChoices.choices},
        })
        return Response({"choices": serializer.data})


class ProjectCreateView(views.APIView):
    """."""

    serializer_class = ProjectSerializer

    def post(self, request, *args, **kwargs):
        """."""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        backend = serializer.validated_data.get('backend')
        frontend = serializer.validated_data.get('frontend')
        database = serializer.validated_data.get('database')

        archive_path = create_project_archive(backend, frontend, database)

        archive = open(archive_path, 'rb')
        response = HttpResponse(archive, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={archive_path.name}'
        return response
