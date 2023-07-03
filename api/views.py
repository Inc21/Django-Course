"""
View for api
"""

from rest_framework.decorators import api_view, permission_classes  # noqa
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from projects.models import Project, Review
from .serializers import ProjectSerializer


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_vote(request, pk):
    """
    project vote
    """
    project = Project.objects.get(id=pk)  # noqa
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,
    )

    review.value = data['value']
    review.save()
    project.get_vote_count

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
