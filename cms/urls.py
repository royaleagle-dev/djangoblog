from . import views
from django.urls import path

app_name = 'cms'

urlpatterns = [
	path('', views.IndexListView.as_view(), name = 'index'),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
	path('<int:year>/<int:month>/', views.PostMonthArchive.as_view(month_format = '%m'), name = 'monthArchive'),
	path('archive/', views.monthArchive, name = 'monthArchive'),
	path('categories/', views.categoryPostListing, name = 'categoryPostListing')
]