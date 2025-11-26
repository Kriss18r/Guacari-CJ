from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

#Modelos para el blog

# Modelo de Categoria

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# Modelo de Post
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) ##para url amigables
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    cover_image = models.ImageField(upload_to='posts/covers/', null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    
    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
    
# Modelo de Foto adicional para posts

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    image = models.ImageField(upload_to='posts/photos/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Photo {self.id} - {self.caption[:20]}"
    
# Modelo de Evento

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    banner = models.ImageField(upload_to='events/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['start']

    def __str__(self):
        return self.title    

# Modelo de Miembro del equipo
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='members/', null=True, blank=True)
    joined_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"