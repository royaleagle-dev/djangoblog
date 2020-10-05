from . import views
from django.urls import path

app_name = 'cms'

urlpatterns = [
	path('', views.IndexListView.as_view(), name = 'index'),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
]