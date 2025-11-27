from django.views.generic import ListView, DetailView
from .models import Post, Event, Member

# Create your views here.

##Clases para las vistas del blog

#Clase para listar las publicaciones del blog
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6
    queryset = Post.objects.filter(is_published=True).order_by('-published_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

##Clase para listar los eventos

class EventListView(ListView):
    model = Event
    template_name = 'blog/event_list.html'
    context_object_name = 'events'

##Clase para listar los miembros

class MemberListView(ListView):
    model = Member
    template_name = 'blog/member_list.html'
    context_object_name = 'members'