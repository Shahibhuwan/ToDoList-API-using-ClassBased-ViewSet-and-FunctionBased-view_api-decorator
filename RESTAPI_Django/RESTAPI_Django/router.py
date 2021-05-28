from api.viewsets import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', TaskViewSet)

#list, retrieve, update , destroy
# GET : api/TaskViewSet/
# POST : api/TaskViewSet/
# DELETE : api/TaskViewSet/id/
# PUT : api/TaskViewSet/id/
