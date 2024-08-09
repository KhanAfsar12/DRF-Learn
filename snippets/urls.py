from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets.views import snippet_list, snippet_detail
from snippets import views


from .views import api_root, SnippetViewSet, UserViewSet
from rest_framework import renderers

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'post': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = SnippetViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })



# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),

# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# # urlpatterns += [
# #     path('api-auth/', include('rest_framework.urls')),
    
# # ]


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]