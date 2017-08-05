from .models import Category, Post

def get_category_cnt(name):
	ca = Category.objects.all().distinct
