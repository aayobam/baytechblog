from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.contrib import messages
from .forms import CommentForm


# Create your views here.

# displays home and also available post lists
class BlogListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    
    
    def get_queryset(self):
        return Post.objects.order_by('-date_posted')
    
    
# Expands full information of a post list.
def detail_view(request, pk):
    template_name = "blog/post_detail.html"
    posts = get_object_or_404(Post, pk=pk)
    comments = posts.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            
            # selects the current athenticated user
            comment_form.instance.comment_author = request.user
            comment_form.instance.email = request.user.email
            
            # collects the comment but don't save yet
            new_comment = comment_form.save(commit=False)
            
            #add the comment to the current post detail.
            new_comment.post=posts
            
            #save and return comment author and its comment body.
            comment_form.save()
            new_comment.save()
            
            messages.success(request, f"Your comment has been added")
            return redirect('post-detail', pk=pk)
    else:
        comment_form = CommentForm()
    template_name = "blog/post_detail.html"
    context = {
        "posts":posts,
        "comment_form":comment_form,
        "comments":comments,
        "new_comment":new_comment,
    }
    return render(request, template_name, context)


# Enables only authenticated users to create new post(s)
class BlogCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = "blog/new_post.html"
    fields = ["title", "body"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    



class BlogUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "body"]
    
     # returns author associated with a post, edit/updates the post and updates the post list.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
   
    
class BlogDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    template_name = "blog/post_delete.html"
    fields = ["title","body"]
    success_url = reverse_lazy('post-list')
    success_message ="post deleted succeffully"
    
    
     # returns author associated with a post, deletes the post and updates the post list.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class CommentUpdateView(UpdateView, LoginRequiredMixin):
    model = Comment
    template_name = "blog/comment_edit.html"
    fields = ["comment"]
    success_url = reverse_lazy('post-list')
    
     # returns author associated with a comment, edit/updates the comment and updates the post detail.
    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        return super().form_valid(form)
    
    
    

# Deletes comment
class CommentDeleteView(DeleteView, LoginRequiredMixin):
    model = Comment
    template_name = "blog/comment_delete.html"
    success_url = reverse_lazy('post-list')
    
    # returns author associated with a comment, deletes the comment and updates the post detail.
    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        return super().form_valid(form)
    
    
    
