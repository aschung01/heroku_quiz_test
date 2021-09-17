from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
  class Meta:
    model = Quiz
    fields = ('title', 'body', 'answer')