from django import forms
from food.models import Recipes

class recipieform(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = "__all__"

