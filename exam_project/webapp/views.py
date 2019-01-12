from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from webapp.models import UserInfo, Post
from webapp.forms import UserForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class UserListView(LoginRequiredMixin, ListView):
    model = UserInfo
    template_name = 'user_list.html'

class UserDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.order = Post.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:user_detail', kwargs={'pk': self.object.user.pk})

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-date')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.autor = self.request.user.info
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse('webapp:post_list')