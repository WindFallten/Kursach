from django.urls import path, include
from rest_framework import routers
from api.views import ReviewsViewSet,NewsViewSet,CommentsViewSet,CategoryViewSet,ArticlViewSet,PlaceViewSet

router = routers.DefaultRouter()
router.register(r'reviews', ReviewsViewSet)
router.register(r'news', NewsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'articl', ArticlViewSet)
router.register(r'place', PlaceViewSet)
