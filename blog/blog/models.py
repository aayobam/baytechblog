from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse




class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, default=True)
    date_posted = models.DateTimeField(auto_now=timezone.now)
    
    
    class Meta:
        ordering = ('-date_posted',)
        
    def __str__(self):
        return f"{self.title}"
    
    def snippet(self):
        return f"{self.body[:150]}......"
    
    #to render class base (detail_view) properly with primary key(pk) and redirect
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    comment = models.TextField()
    commented_on = models.DateTimeField(auto_now=timezone.now)
    
    
    class Meta:
        ordering = ('-commented_on',)
    
    def __str__(self):
        return f"{self.comment_author} commented on {self.post}"
    
    def get_absolute_url(self):
        return reverse('post-list')
    