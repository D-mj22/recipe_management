from django.shortcuts import render
from rest_framework.views import APIView
from food.models import Recipes,RateComment
from food.serializers import RecipeSerializer, UserSerializer, RateCommentSerializer
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class ListAll(APIView):                     # List all recipes
    def get_object(self):
        try:
            a = Recipes.objects.all()
            return a
        except:
            raise Http404

    def get(self,request):
        g = self.get_object()
        list_all = RecipeSerializer(g,many=True)
        return Response(list_all.data,status=status.HTTP_200_OK)


class RecipeViews(viewsets.ModelViewSet):           # GET,GET-pk,POST,PUT,DELETE request
    permission_classes = [IsAuthenticated]
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend]         # Filter recipes
    filterset_fields = ['cuisine', 'meal_type','ingredient_list']

class Search(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]         # Search recipes
    search_fields = ['title','ingredient_list']

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class Register(APIView):
    # def get(self,request):
    #     u = User.objects.all()
    #     user = UserSerializer(u,many=True)
    #     return Response(user.data)
    #
    # def post(self,request):
    #     u = UserSerializer(data=request.data)
    #     if u.is_valid():
    #         u.save()
    #         return Response(u.data,status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','POST'])
# def rate_review(request, recipe_id):
#     permission_classes = [IsAuthenticated]
#     if request.method=="GET":
#         all_r = RateComment.objects.all()
#         r1 = RateCommentSerializer(all_r,many=True)
#         return Response(r1)
#     if request.method=="POST":
#         r = RateCommentSerializer(data=request.data)
#         if r.is_valid():
#             r.save(recipe_id=recipe_id, user=request.user)
#             return Response(r.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

class Rate_review(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        # id = request.data.get('recipe')
        r = RateCommentSerializer(data=request.data)
        u = self.request.user

        if r.is_valid():
            # r.save(user=u,recipe=id)
            r.validated_data['user']=u
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)































