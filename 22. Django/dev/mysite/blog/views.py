from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse#, Http404
from .models import Post
# Create your views here.

def test1(request):
  # 서비스 처리
  return HttpResponse("hello!")

def test2(request, no):
  print(type(no))
  return HttpResponse(f'{no}')
# no url에서 받은 path 변수

def list(request):
  post_list = Post.objects.all()
  titles = ''

  for post in post_list:
    titles += post.title

  return HttpResponse(titles)

def detail(request, id):
  # try:
  #   post = Post.objects.get(id=id)

  # except Post.DoesNotExist:
  #   raise Http404('존재하지 않는 테이터입니다.')

  post = get_object_or_404(Post, id=id)

  return HttpResponse(post.title)
