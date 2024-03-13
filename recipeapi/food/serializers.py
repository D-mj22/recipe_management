from rest_framework import serializers
from food.models import Recipes, RateComment
from django.contrib.auth.models import User


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['title','author','category','cuisine','meal_type','servings','date_added','updated_at','image','ingredient_list','recipe_detail']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','password']

    def create(self,validated_data):
        u = User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u

class RateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateComment
        fields = "__all__"
