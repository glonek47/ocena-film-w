from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ocena.models import Actor_Director, Film, Ocenka 

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        """
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class Actor_DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor_Director
        fields = ('imie', 'nazwisko')


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'
        depth = 1

class OcenkaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ocenka
        fields = '__all__'
