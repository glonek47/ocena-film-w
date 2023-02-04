from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from ocena.serializers import Actor_DirectorSerializer, FilmSerializer, OcenkaSerializer, UserSerializer
from ocena.models import Actor_Director, Film, Ocenka
from rest_framework import generics, permissions
from rest_framework.response import Response
"""
class UserViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows users to be viewed or edited.
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows groups to be viewed or edited.
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.
"""
#class FilmCreateApiView(generics.CreateAPIView):
 #   serializer_class

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

#class FilmApiView(generics.ListCreateAPIView):
 #   serializer_class = FilmSerializer
 #   queryset = Film.objects.all()
class Actor_DirectorList(generics.ListCreateAPIView):
    queryset = Actor_Director.objects.all()
    serializer_class = Actor_DirectorSerializer
    permission_classes = [permissions.IsAuthenticated] 

class Actor_DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor_Director.objects.all()
    serializer_class = Actor_DirectorSerializer
    permission_classes = [permissions.IsAuthenticated] 

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticated] 

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticated] 

class OcenkaList(generics.ListCreateAPIView):
    queryset = Ocenka.objects.all()
    serializer_class = OcenkaSerializer
    permission_classes = [permissions.IsAuthenticated] 

class OcenkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ocenka.objects.all()
    serializer_class = OcenkaSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
class UserCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    model = User
    serializer_class = UserSerializer