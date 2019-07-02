from test_plus.test import TestCase
from django_dynamic_fixture import G

from django.urls import reverse
from .models import PostRestaurant
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.
class BlogTestCase(TestCase):

	def setUp(self):
		self.username = "test username"
		self.user = G(User, username=self.username)
		self.titulo = "test titulo post"
		now = datetime.now().date()
		
		self.blog = G(PostRestaurant, user=self.user, titulo=self.titulo, fecha_publicado=now, fecha_desactivado=now)


	def test_post_home(self):
		# reverse url , redirect
		url = reverse('restaurante:post_restaurant')
		response = self.get(url) #/blog
		self.response_200()
		self.assertContains(response, self.titulo)

	def test_post_home_q(self):
		# reverse url , redirect
		url = reverse('restaurante:post_restaurant')
		#blog/?q=nicolef
		url_query = "{}?q={}".format(url, self.username)
		response = self.get(url_query) #/blog
		self.response_200()
		self.assertContains(response, self.titulo)

		



