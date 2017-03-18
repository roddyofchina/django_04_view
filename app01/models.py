# coding:utf8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# 分类表

class Category(models.Model):
	name = models.CharField(max_length=20, verbose_name="分类名")
	cat_url = models.CharField(max_length=20, verbose_name="分类url", default='/')
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = u'分类'
		verbose_name_plural = verbose_name


class Author(AbstractUser):
	phone_number = models.CharField(max_length=11)
	
	def __unicode__(self):
		return self.username
	
	class Meta:
		verbose_name = u'用户'
		verbose_name_plural = verbose_name


# 文章表

class Article(models.Model):
	title = models.CharField(max_length=50, verbose_name=u"标题")
	content = models.TextField(verbose_name=u"内容")
	author = models.ForeignKey(Author)
	category = models.ForeignKey(Category)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name = u"文章"
		verbose_name_plural = verbose_name


# 友情连接表
class Links(models.Model):
	url = models.URLField(verbose_name=u'地址')
	name = models.CharField(max_length=20, verbose_name=u"名称")
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = u"友情链接"
		verbose_name_plural = verbose_name


