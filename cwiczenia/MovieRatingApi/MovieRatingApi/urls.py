"""movie_rating_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ocena import views
from django.contrib.auth.models import User
from ocena.views import Actor_DirectorList, Actor_DirectorDetail, FilmList, FilmDetail, OcenkaList, OcenkaDetail


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    #path('film/', views.FilmApiView.as_view()),
    path('actor_director/', Actor_DirectorList.as_view(), name='actor_director-list'),
    path('actor_director/<int:pk>/', Actor_DirectorDetail.as_view(), name='actor_director-detail'),
    path('film/', FilmList.as_view(), name='film-list'),
    path('film/<int:pk>/', FilmDetail.as_view(), name='film-detail'),
    path('ocenka/', OcenkaList.as_view(), name='ocenka-list'),
    path('ocenka/<int:pk>/', OcenkaDetail.as_view(), name='ocenka-detail'),
]
