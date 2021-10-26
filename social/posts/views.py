"""
importing default views
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    """
    Class is Used for showing list of post  
    """
    model = models.Post
    select_related = ("user", "group")

class UserPosts(generic.ListView):
    """
    class is created for User post.
    """
    model = models.Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        """
        method will show the post of the user which is logged in
        otherwise raise exception
        """
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact
                                = self.kwargs.get("username"))
        
        except User.DoesNotExist:
            raise Http404

        else :
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        """
        used for returning the context
        """
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class PostDetail(SelectRelatedMixin, generic.DetailView):
    """
    used for detail of post
    """
    model = models.Post
    select_related = ("user", "group")

    def get_queryset(self):
        """
        method will filter user as per the username of user
        """
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get("username"))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    """
    used for creating post
    """
    fields = ('message','group')
    model = models.Post

    def form_valid(self, form):
        """
        connect the actual post to the user itself
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    """
    created for delete post
    """
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        """
        filter the post as per the user        
        """
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
