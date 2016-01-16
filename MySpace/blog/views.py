from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from blog.forms import UserLoginForm, RegisterForm, UserPostCommentForm
from blog.models import UserInfo, Post, Likes, Topics, UserPostComment
from django.http import HttpResponse
from django.db.models import Count
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm


class ContextExtraMixin(object):
	def get_context_data(self, **kwargs):
		context = super(ContextExtraMixin, self).get_context_data(**kwargs)
		context['topics'] = Topics.objects.all()
		return context

def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form, 'topics' : Topics.objects.all(),}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!',
                
            }
            return render(request, 'login.html', context)

        else:
            login(request, user)
            return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')

class RegisterCreateView(ContextExtraMixin, CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

          
class PostListView(ContextExtraMixin,TemplateView):
    model = Post
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        request = self.request
        if(request.user.is_authenticated()):
            posts = Post.objects.all()
            context['posts'] = posts[:5]
            context['likes'] = Post.objects.annotate(number_likes=Count('likes')).order_by('-number_likes')[:5]
        else:
            posts = Post.objects.filter(acces=True)
            context['posts'] = posts[:5]
            context['likes'] = posts.annotate(number_likes=Count('likes')).order_by('-number_likes')[:5]
              
        return context



class PostDetailView(ContextExtraMixin, DetailView):


    model = Post
    template_name = 'post_details.html'
    form  = UserPostCommentForm()


    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = self.get_object()
        context['likes_list'] = Likes.objects.filter(post = post.pk)
        context['likes_list_top3'] = context['likes_list'][:3]
        context['likes_count'] = len(context['likes_list']) - len(context['likes_list_top3'])  
        context['form'] = UserPostCommentForm()
        return context

    def post(self, request, *args, **kargs):
    	form = UserPostCommentForm(request.POST)
    	obj = self.get_object()

    	if form.is_valid():
    		comment = form.save(commit=False)
    		comment.author = request.user
    		comment.post = obj
    		comment.save()
    	return redirect('post_details', pk = obj.pk)

class TopicPostListView(ContextExtraMixin, TemplateView):
   model = Post
   template_name = "index.html"
   def get_context_data(self,**kwargs):
       context = super(TopicPostListView, self).get_context_data(**kwargs)
       
       posts = Post.objects.filter( topic__pk = kwargs['pk'])
       context['posts'] = posts
       context['likes'] = posts.annotate(number_likes=Count('likes')).order_by('-number_likes')
              
       return context






