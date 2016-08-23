from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from models import User, Comment, Like


def index(request):

    return render(request, 'onproject/index.html', {})

def main(request):
    uname = ''
    comment_list = []
    liked_comments = []
    if 'uname' in request.session:
        uname = request.session['uname']
    comment_list = Comment.objects.all()
    liked_comments = Like.objects.filter(username=uname)
    return render(request, 'onproject/main.html', {'uname' : uname, 'comment_list': comment_list, 'liked_comments':liked_comments})


def create_user(request):

    if request.method == 'POST':
        name = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")
        if User.objects.filter(username=uname).exists():
            return render(request, 'onproject/index.html', {})
        user = User(username = uname,pwd = pwd, name =  name, sirname = lname, email = email)
        user.save()
        request.session['uname'] = uname
        return HttpResponseRedirect(reverse('main'))
    return HttpResponseRedirect(reverse('main'))


def log_in(request):

    if request.method == 'POST':
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        if User.objects.filter(username=uname, pwd = pwd).exists():
            request.session['uname'] = uname
            return HttpResponseRedirect(reverse('main'))

    return HttpResponseRedirect(reverse('index'))


@csrf_exempt
def post_comment(request):
    if request.method == 'POST':
        uname = ''
        if 'uname' in request.session:
            uname = request.session['uname']
        comment = request.POST.get("comment")
        new_comment = Comment(username = uname, comment =  comment, pub_date = '', likes = 0)
        new_comment.save()
    return HttpResponse('Done')

@csrf_exempt
def like_comment(request):
    if request.method == 'POST':
        uname = ''
        if 'uname' in request.session:
            uname = request.session['uname']
        comment_id = request.POST.get("comment_id")
        liked_comment = Comment.objects.get(id = comment_id)
        liked_comment.likes = liked_comment.likes + 1
        liked_comment.save()
        new_like = Like(username = uname, comment_id = comment_id)
        new_like.save()
    return HttpResponse('Done')


@csrf_exempt
def unlike_comment(request):
    if request.method == 'POST':
        uname = ''
        if 'uname' in request.session:
            uname = request.session['uname']
        comment_id = request.POST.get("comment_id")
        unliked_comment = Comment.objects.get(id = comment_id)
        unliked_comment.likes = unliked_comment.likes - 1
        unliked_comment.save()
        Like.objects.get(username = uname, comment_id = comment_id).delete()
    return HttpResponse('Done')

