from django.test import TestCase
from . models import Post, Tag, Category

def createCategory(title):
	return Category.objects.create(title = title)

def createTag(name):
	return Tag.objects.create(name = name)

def createPost(title, body, author, postState):
	tag = Tag.objects.create(name = 'NewT')
	post = Post.objects.create(title=title, body=body, category=createCategory("New"), author=author, postState=postState)
	post.tags.add(tag)
	return post

class PostTestCase(TestCase):
	def setUp(self):
		createPost('New Post', 'This is a new Post', 'Ayotunde', 'p')

	def testPostStr(self):
		post = Post.objects.get(id=1)
		self.assertEqual(post.__str__(), 'New Post')		

class TagTestCase(TestCase):
	def testTagStr(self):
		tag = Tag.objects.create(name = 'New Tag')
		self.assertEqual(tag.__str__(), 'New Tag')

class CategortTestCase(TestCase):
	def testCategoryStr(self):
		category = Category.objects.create(title = "New Cat")
		self.assertEqual(category.__str__(), "New Cat")
