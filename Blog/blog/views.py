from django.shortcuts import render
from .forms import UserForm,CreateBlogForm
from .models import CreateBlog, Comments
from django.shortcuts import redirect
from django.views.generic import ListView,DetailView,CreateView

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    blogs = CreateBlog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            username = user_form.save()
            username.set_password(username.password)
            username.save()

            registered = True
            return render(request, 'register.html', {'registered':registered})

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        return render(request, 'register.html',{'registered':registered,'user_form':user_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Acc not active')

        else:
            print("Someone tries to login and failed")
            return HttpResponse('invalid login details')

    else:
        return render(request, 'login.html', {})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def createBlog(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        blog = request.POST.get('blog')
        print(title)
        print(request.user)
        create_blog = CreateBlog(user=request.user,title=title, blog=blog)
        create_blog.save()
        return redirect('blog:profile')
    else:
        return render(request, 'create_blog.html')

class BlogDetailView(DetailView):
    model = CreateBlog
    context_object_name = 'blog_detail'

class CreateBlogView(CreateView):
    fields = ('title', 'blog')
    model = CreateBlog

def comment(request, pk):
    
    if request.method == 'POST':
        post = CreateBlog.objects.get(pk=pk)
        comment = request.POST.get('comment')
        username = request.user
        new_comment = Comments(user=username,post=post,text=comment)
        new_comment.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'comment.html')


    