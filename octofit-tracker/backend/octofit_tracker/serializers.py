from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Team, Activity, LeaderboardEntry, Workout

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
		model = UserProfile
		fields = ['id', 'user', 'bio', 'avatar', 'team']

class TeamSerializer(serializers.ModelSerializer):
	members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Team
		fields = ['id', 'name', 'description', 'created_at', 'members']

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workout
		fields = ['id', 'name', 'description', 'difficulty', 'duration_minutes']

class ActivitySerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	workout = WorkoutSerializer(read_only=True)
	class Meta:
		model = Activity
		fields = ['id', 'user', 'workout', 'date', 'duration_minutes', 'calories_burned']

class LeaderboardEntrySerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	team = TeamSerializer(read_only=True)
	class Meta:
		model = LeaderboardEntry
		fields = ['id', 'user', 'team', 'total_points']
