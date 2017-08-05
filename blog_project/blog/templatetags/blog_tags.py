from django import template
from django.urls import reverse
from django.shortcuts import get_object_or_404
from ..models import Post, Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num = 5):
	return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
	return Post.objects.dates('created_time', 'month', order = 'DESC')

@register.simple_tag
def get_categories():
	return Category.objects.all()

@register.simple_tag
def get_index_url():
	return reverse('blog:index')

@register.simple_tag
def get_category_cnt(cat_pk):
	cat = get_object_or_404(Category, pk = cat_pk)
	lst = Post.objects.all().filter(category = cat)
	return lst.count()
