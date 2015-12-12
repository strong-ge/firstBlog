#coding:utf-8
from blog.models import Tag,Blog
#按月归档
def get_Blog_byMonth(): 
	post_date = Blog.objects.datetimes('update_time','month')
	date_list=[]       
	for i in range(len(post_date)):
		date_list.append([])
	for i in range(len(post_date)):
		curyear = post_date[i].year
		curmonth = post_date[i].month
		tempArticle = Blog.objects.filter(update_time__year=curyear).filter(update_time__month=curmonth)
		tempNum = len(tempArticle)
		date_list[i].append(post_date[i])
		date_list[i].append(tempNum)
	return date_list
#按标签归档
def get_Blog_byTag():
	tags = Tag.objects.all()#获取所有标签
	tag_list = []
	for i  in range(len(tags)):
		tag_list.append([])
	for i  in range(len(tags)):
		temp = Tag.objects.get(tag_name = tags[i]) #获取当前标签
		posts = temp.blog_set.all() #获取当前标签下的所有文章
		tag_list[i].append(tags[i].tag_name)
		tag_list[i].append(len(posts))
	return tag_list