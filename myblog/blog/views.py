#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json,markdown,pytz
from blog.models import Tag,Blog
from func import *
# Create your views here.
def index(request):
	return render_to_response('index.html')

def test(request):
	artical=Blog.objects.get(id=9)
	return render_to_response('test.html',locals())
def list(request):
	blogs=Blog.objects.order_by('-update_time')
	date_list=get_Blog_byMonth()
	tag_list=get_Blog_byTag()    
	paginator = Paginator(blogs, 8)
	page=request.GET.get('page')
	try:
		blog_list=paginator.page(page)
	except PageNotAnInteger:
		blog_list=paginator.page(1)
	except EmptyPage:
		blog_list=paginator.paginator(paginator.num_pages)
	return render_to_response('list.html',locals())
def artical(request,aid):
	artical=Blog.objects.get(id=int(aid))
	return render_to_response('artical.html',locals())
def about(request):
	date_list=get_Blog_byMonth()
	tag_list=get_Blog_byTag()
	return render_to_response('about.html',locals())

def addblog(request):
	tags=Tag.objects.all()
	return render_to_response('addblog.html',locals())
def addtag(request):
	tag_name=request.GET.get('tag_name')
	newtag=Tag()
	newtag.tag_name=tag_name
	newtag.save()
	id=newtag.id
	tag={'id':id,'tag_name':tag_name}
	tag=json.dumps(tag)
	return HttpResponse(tag)
def addblogok(request):
	title=request.POST.get('title')
	tag_ids=request.POST.getlist('tag_name')
	content=request.POST.get('content')
	blog=Blog()
	blog.title=title
	blog.content=content
	blog.save()
	for tag_id in tag_ids:
		list=Tag.objects.get(id=int(tag_id))
		blog.tags.add(list)
	return HttpResponseRedirect('/list/')
#当前月份下的所有博客
def archive_month(request,year,month):
	blogs = Blog.objects.filter(update_time__year=year).filter(update_time__month=month).order_by('-update_time')
	date_list=get_Blog_byMonth()
	tag_list=get_Blog_byTag()
	paginator = Paginator(blogs, 8)
	page=request.GET.get('page')
	try:
		blog_list=paginator.page(page)
	except PageNotAnInteger:
		blog_list=paginator.page(1)
	except EmptyPage:
		blog_list=paginator.paginator(paginator.num_pages)
	return render_to_response('list.html',locals())
#当前标签下的所有博客
def tagDetail(request,tag):
	date_list=get_Blog_byMonth()
	tag_list=get_Blog_byTag()
	temp = Tag.objects.get(tag_name=tag)
	blogs = temp.blog_set.order_by('-update_time')
	paginator = Paginator(blogs,8)
	page=request.GET.get('page')
	try:
		blog_list=paginator.page(page)
	except PageNotAnInteger:
		blog_list=paginator.page(1)
	except EmptyPage:
		blog_list=paginator.paginator(paginator.num_pages)
	return render_to_response('list.html',locals())
