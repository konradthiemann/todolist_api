
from django.contrib import admin
from rest_framework import routers
from todo.views import TodoViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
