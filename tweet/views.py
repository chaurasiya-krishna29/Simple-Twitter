from django.shortcuts import render,HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return HttpResponse("Hello Buddyss")

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method=="POST":
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)#commit is false because we dont want to save in database we are temporary saving it
            tweet.user = request.user #we want to add user also so we will call user from request, because from the form we will not get user we are calling from models
            tweet.save()
            return redirect('tweet_list')
    else:
        form =TweetForm()
    return render(request,'tweet_form.html',{'form':form})


@login_required
def tweet_edit(request,tweet_id):#tweet_id is the id of the tweets created ,pk stands for primary key,Tweet is the model created in the model file
    tweet = get_object_or_404(Tweet, pk=tweet_id,user=request.user)#user=request.user is used to check that the owner of the user who is login can only edit the tweets
    if request.method == "POST":
        form = TweetForm(request.POST,request.FILES,instance=tweet)#instance=tweet is used to get the tweet that is to be edited
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else :
        form = TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id,user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})


def register(request):
    if request.method =="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    return render(request,'registeration/register.html',{'form':form})
