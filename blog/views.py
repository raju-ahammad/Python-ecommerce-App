from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, View
from .models import BlogPost, CommentModel
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class BlogPostListView(ListView):
    model    = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'blog_post'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogPostListView, self).get_context_data(*args, **kwargs)
        context['created'] = BlogPost.objects.order_by('-created')[:8];
        context['recent'] = BlogPost.objects.order_by('-created')[:4];
        return context


class BlogPostDetail(DetailView):
    model    = BlogPost
    template_name = 'blog/detail.html'

    def post(self, request, *args, **kwargs):
        view = CommentView.as_view()
        return view(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetail, self).get_context_data(**kwargs)
        context['comments'] = CommentModel.objects.filter(post = self.get_object())
        context['form'] = CommentForm()
        context['recent'] = BlogPost.objects.order_by('-created')[:4];
        return context






class CommentView(CreateView):
    model = CommentModel
    fields = ['content']
    template_name = 'detail.html'
    def form_valid(self, form):
        models_name = CommentModel()
        models_name.content = self.request.POST['content']
        models_name.author = self.request.user
        models_name.post = BlogPost.objects.get(pk=self.kwargs['pk'])
        models_name.save()
        return redirect(self.get_success_url(id = self.kwargs['pk']))

    def get_success_url(self, **kwargs):
        if  kwargs != None:
            return reverse_lazy('blog_detail', kwargs = {'pk': kwargs['id']})
        else:
            return reverse_lazy('blog_detail', args = (self.object.id,))
