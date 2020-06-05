from django.shortcuts import render, redirect
from blog_posts.forms import BlogPostForm, RegisterForm, LoginForm
from .models import Post
from django.contrib.auth import authenticate, login

# Create your views here.
def postform(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/allposts')
            except:
                pass
    else:
        form = BlogPostForm()
    return render(request,'blog_posts/post_form.html',{'form':form})

def listofposts(request):
	posts = Post.objects.all()
	return render(request, 'blog_posts/post_list.html', {'posts':posts})

def delete(request, id):
	post = Post.objects.get(id=id)
	post.delete()
	return redirect('/allposts')

def edit(request, id):
	curr = Post.objects.get(id=id)
	posts = Post.objects.exclude(id=id)
	return render(request, 'blog_posts/post_list.html', {'posts':posts, 'curr':curr})

def update(request, id):
	post = Post.objects.get(id=id)
	form = BlogPostForm(request.POST)
	print (form)
	posts = Post.objects.exclude(id=id)
	if form.is_valid():
		print ("asasdasdasd")
		post.delete()
		form.save()
		return redirect("/allposts")
	return render(request, 'blog_posts/post_list.html', {'posts':posts, 'curr':post, 'form':form})



def registeruser(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/blogpost')
			except:
				pass
	else:
		form = RegisterForm()
	return render(response,'auth_pages/register_page.html',{'form':form})


def loginuser(request):
	form = LoginForm()
	username = request.POST.get('username',False)
	password = request.POST.get('password',False)
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('/blogpost')
	else:
		return render(request, 'auth_pages/signin_page.html', {'form': form})

		



