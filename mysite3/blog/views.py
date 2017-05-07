from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from blog.models import Post


#--- List View
class PostLV(ListView):
	model = Post
	template_name = 'blog/post_all.html' # 디폴트 post_list.html
	context_object_name = 'posts' # 디폴트 objects_list
	paginate_by = 2


#--- Detail View
class PostDV(DetailView):
	model = Post


#--- Archive View
class PostAV(ArchiveIndexView):
	model = Post
	date_field = 'modify_date'


class PostYAV(YearArchiveView):
	model = Post
	date_field = 'modify_date'
	make_object_list = True


class PostMAV(MonthArchiveView):
	model = Post
	date_field = 'modify_date'


class PostDAV(DayArchiveView):
	model = Post
	date_field = 'modify_date'


class PostTAV(TodayArchiveView):
	model = Post
	date_field = 'modify_date'
