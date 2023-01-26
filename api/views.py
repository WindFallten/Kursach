from django.shortcuts import render
from rest_framework import viewsets
from main.models import Reviews,News,Comments,Category,Articl,Place
from .serializers import ReviewsSerializer,NewsSerializer,CommentsSerializer,CategorySerializer,ArticlSerializer,PlaceSerializer
# Create your views here.


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ArticlViewSet(viewsets.ModelViewSet):
    queryset = Articl.objects.all()
    serializer_class = ArticlSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
