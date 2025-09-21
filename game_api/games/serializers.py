from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Developer, Platform, Game, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['telephone']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        
        return user

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'name', 'country', 'founded_year']

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name', 'manufacturer']

class GameSerializer(serializers.ModelSerializer):
    developer = serializers.PrimaryKeyRelatedField(queryset=Developer.objects.all())
    platforms = serializers.PrimaryKeyRelatedField(queryset=Platform.objects.all(), many=True)

    class Meta:
        model = Game
        fields = ['id', 'title', 'release_date', 'developer', 'platforms', 'genre', 'summary']