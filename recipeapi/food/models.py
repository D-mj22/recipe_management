from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Recipes(models.Model):
    title = models.CharField(max_length=40,unique=True,primary_key=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=10)
    cuisine = models.CharField(max_length=20)
    meal_type = models.CharField(max_length=20)
    servings = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='pictures',null=True,blank=True)
    ingredient_list = models.TextField()
    recipe_detail = models.TextField()

    def __str__(self):
        return self.title

class RateComment(models.Model):
    recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE,related_name='rating',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    rating = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField(null=True,blank=True)


    class Meta:
        unique_together = ('recipe','user')

    def __str__(self):
        return str({self.user}) + "rates" + str({self.recipe}) + "a" + str({self.rating})


