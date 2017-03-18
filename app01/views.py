#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView,RedirectView


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from app01.models import Article
# Create your views here.

#基础视图函数
class MyView(View):
	def get(self,request,*args,**kwargs):
		return HttpResponse('Hello,world!')
	
	

#TemplateView视图
class MyhtmlView(TemplateView):
	template_name = "home.html"
	
	def get_context_data(self, **kwargs):
		#重载父类方法
		context = super(MyhtmlView,self).get_context_data(**kwargs)
		list_data = ['sichuan','chengdu','meishan','guangdong']
		context.update({'username':'luodi','list_data':list_data})
		
		return context



#RedirectView重定向URl
class RedUrlView(RedirectView):
	
	url=''  #目的url，可以不配置，如果没有设置将使用pattern_name指定的url
	
	permanent = False   #是否永久重定向，默认为True
	query_string = True     #是否把GET请求的参数带给目的URL
	pattern_name =  'roddy'  #url
	def get_redirect_url(self, *args, **kwargs):
		#逻辑代码
		return super(RedUrlView,self).get_redirect_url(*args,**kwargs)
	

	
#ListView视图使用
class ArticleListView(ListView):
	template_name = 'Article.html'
	model = Article
	context_object_name="article_list"  #传给模版中的变量
	

	def get_context_data(self, **kwargs):
		
		dirlist={'username':'roddy'}
		context=super(ArticleListView,self).get_context_data(**kwargs)
		context.update(dirlist)
		
		return context


#DetailView视图
class ArticleDetail(DetailView):
	model = Article
	template_name = 'ArticleDetail.html'
	context_object_name = "article_detail"
	
	def get_context_data(self, **kwargs):
		
		return super(ArticleDetail,self).get_context_data(**kwargs)

