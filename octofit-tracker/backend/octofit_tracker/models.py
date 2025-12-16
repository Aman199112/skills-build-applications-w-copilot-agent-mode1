
from djongo import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	avatar = models.URLField(blank=True)
	team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

	def __str__(self):
		return self.user.username

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	difficulty = models.CharField(max_length=50)
	duration_minutes = models.PositiveIntegerField()

	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	duration_minutes = models.PositiveIntegerField()
	calories_burned = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.user.username} - {self.workout.name} on {self.date}"

class LeaderboardEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
	total_points = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.user.username} - {self.total_points} pts"
