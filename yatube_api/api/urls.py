from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name: str = 'api_v1'

router = DefaultRouter()
router.register('posts', PostViewSet, 'posts')
router.register('groups', GroupViewSet, 'groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                'comments'
                )
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='auth-token'),
]
