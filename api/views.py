from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project


@api_view(['GET'])
def get_routes(request):
    """
    routes
    """
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def get_projects(request):
    """
    get project view
    """
    print('USER:', request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    """
    get project view
    """
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
