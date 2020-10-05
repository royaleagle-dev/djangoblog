from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 255)
	body = models.TextField(max_length = 4000)
	category = models.ForeignKey('Category', on_delete = models.CASCADE)
	tags = models.ManyToManyField('Tag')
	author = models.CharField(max_length = 255)
	postDate = models.DateTimeField(auto_now_add = True)
	lastModified = models.DateTimeField(auto_now = True)
	lBan = models.ImageField(upload_to = 'uploads/images/l', null = True, blank = True)
	pBan = models.ImageField(upload_to = 'uploads/images/p', null = True, blank = True)
	nBan = models.ImageField(upload_to = 'uploads/images/n', null = True, blank = True)
	state = (
		('d','draft'),
		('p', 'published'),
	)
	postState = models.CharField(max_length=1, choices=state, default = 'd')

	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length = 255)

	def __str__(self):
		return self.name

class Category(models.Model):
	title = models.CharField(max_length = 255)

	def __str__(self):
		return self.title