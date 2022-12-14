from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import EditPostView
urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('comment/<str:pk>', views.comment, name='comment'),
    path('pref/', views.pref, name='pref'),
    path('delete/<str:delete_id>', views.delete, name='delete'),
    path('delete_c/<str:delete_c_id>', views.delete_c, name='delete_c'),
    path('edit/<str:pk>', EditPostView.as_view(), name='edit'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('flag-post', views.flag_post, name='flag-post'),
    path('flag-comment', views.flag_comment, name='flag-comment'),
    path('signup', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('logout', views.logout, name='logout'),
    path('data', views.data, name='data'),
    path('flag_admin', views.flag_admin, name='flag_admin'),
]