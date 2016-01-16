from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect
from blog.forms import UserLoginForm, RegisterForm
from blog.models import UserInfo, Post, Likes
from django.http import HttpResponse
from django.db.models import Count
from django.views.generic import TemplateView

def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.me1thod == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)

        else:
            login(request, user)
            return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterCreateView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = 'index.html'

          
class PostListView(TemplateView):
   model = Post
   template_name = "index.html"
   def get_context_data(self,**kwargs):
       context = super(PostListView, self).get_context_data(**kwargs)
       posts = Post.objects.all()
       context['posts'] = posts[:5]
       context['likes'] = Post.objects.annotate(number_likes=Count('likes')).order_by('-number_likes')[:5]
              
       return context


class PostDetailView(DetailView):

    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = self.get_object()
        context1 = Likes.objects.filter(post = post.pk)
       # context2 = Likes.objects.author(post = post.pk)
        context['likes_list'] = context1
        context['likes_list_top3'] = context1[:3]
        context['likes_count'] = len(context1)     
        return context



'''def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    if request.method == 'GET':
        form = UserPostCommentForm()
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = UserPostCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = UserPostComment(text=text, post=post, author=request.user)
            comment.save()
        return redirect('post_details', pk=pk)'''

 
