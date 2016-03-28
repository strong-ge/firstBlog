from django.db import models
from django.core.urlresolvers import reverse
class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.tag_name

class Blog(models.Model):
    """docstring for Blogs"""
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.title

class IP(models.Model):
    dream_id = models.IntegerField(default=0)
    ip_address=models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
                return self.ip_address

class Dream(models.Model):
    ip=models.ForeignKey(IP)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    content = models.TextField()
    pic_name = models.CharField(max_length=30)
    pic_path=models.FileField(upload_to='./upload/')
    love_num = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name

