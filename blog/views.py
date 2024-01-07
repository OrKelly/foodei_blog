from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from blog.models import Post, Comment
from .forms import CommentForm, AddPostForm
from modules.services.utils import AuthorRequiredMixin


class PostListView(ListView):
    model = Post
    extra_context = {'title': 'Блог' }
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug']).select_related('category')

class TagListView(ListView):
    model = Post
    extra_context = {'title': 'Блог'}
    def get_queryset(self):
        return Post.objects.filter(tag__slug=self.kwargs['slug']).select_related('category')

class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    extra_context = {'title': 'Блог'}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class AddPost(LoginRequiredMixin,CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Добавление поста'}

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePost(AuthorRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'blog/add_post.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Редактирование поста'}

    def form_valid(self, form):
        w = form.save(commit=False)
        return super().form_valid(form)


class DeletePost(AuthorRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    slug_url_kwarg = 'post_slug'
    template_name = 'blog/delete_post.html'
    extra_context = {'title': 'Удаление'}


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        w.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class UpdateComment(AuthorRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/update_comment.html'
    pk_url_kwarg = 'pk'
    extra_context = {'title': 'Редактирование комментария'}

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def form_valid(self, form):
        w = form.save(commit=False)
        return super().form_valid(form)



class DeleteComment(AuthorRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'
    template_name = 'blog/delete_comment.html'
    extra_context = {'title': 'Удаление комментария'}

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class HomeView(ListView):
    extra_context = {'title': 'Главная страница'}
    model = Post
    paginate_by = 5
    template_name = 'blog/home.html'
