from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post
from cms.dateManip import months

class IndexListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'cms/index.html'

	def queryset(self):
		queryset = {
			'latest': Post.objects.filter(postState__exact = 'p').order_by('-id')[:1],
			'latest2':Post.objects.filter(postState__exact = 'p').order_by('-id')[:2],
			'latest10':Post.objects.filter(postState__exact = 'p').order_by('-id')[:10],

			#the rest goes here
		}
		return queryset

class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'cms/postDetail.html'

	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#obj = super().get_object
		context['related'] = Post.objects.filter(category__exact = self.object.category)
		return context



from django.views.generic.dates import MonthArchiveView

class PostMonthArchive(MonthArchiveView):
	queryset = Post.objects.all()
	date_field = "postDate"
	template_name = "cms/date.html"


def monthArchive(request):
	posts = Post.objects.all()
	monthList = [ ];
	monthList = set(monthList)

	for i in posts:
		result = months(i.postDate.month) + ' '+ str(i.postDate.year)
		monthList.add(result)

	context = {
	'monthList':monthList
	}
	return render(request, 'cms/monthArchive.html', context)


	
