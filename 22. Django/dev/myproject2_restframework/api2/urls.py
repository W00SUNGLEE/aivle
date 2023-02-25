from django.urls import path, include
from rest_framework import routers
#from api2.views import *
from api2 import views

# Routers provide an easy way of automatically determining the URL conf.

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),   
# ]


urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostRetrieveView.as_view(), name='post-detail'),
    path('comment/', views.CommentView.as_view(), name='comment-list'),
    path('like/<int:pk>', views.PostLikeAPIView.as_view(), name='post-like'),
]