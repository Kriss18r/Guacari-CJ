from django.urls import path
from . import views

app_name = 'GuacariBlog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('eventos/', views.EventListView.as_view(), name='event_list'),
    path('miembros/', views.MemberListView.as_view(), name='member_list'),
]