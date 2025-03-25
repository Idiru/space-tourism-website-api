"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from app.models import Crew, Technologie, Destination



# Serializers define the API representation.
class CrewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crew
        fields = ['name', 'job', 'description', "url"]

class TechnologiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technologie
        fields = ['name','description', "url"]
        
class DestinationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destination
        fields = ['name','description', "avg_distance", "est_travel_time", "url"]

# ViewSets define the view behavior.
class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    
class TechnologiesViewSet(viewsets.ModelViewSet):
    queryset = Technologie.objects.all()
    serializer_class = TechnologiesSerializer
    
class DestinationsViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationsSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'crew', CrewViewSet)
router.register(r'technologies', TechnologiesViewSet)
router.register(r'destinations', DestinationsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]


