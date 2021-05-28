from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def list(self, request):
    #     queryset = Task.objects.all()
    #     serializer = TaskSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Task.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer =TaskSerializer(user)
    #     return Response(serializer.data)