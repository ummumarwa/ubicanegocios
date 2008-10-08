import cgi
import wsgiref.handlers
import os

from google.appengine.ext import webapp
from modelos import lugares

from google.appengine.ext.webapp import template

class MainPage (webapp.RequestHandler):
	def get(self):
		"""Muestro la pantalla principal con solo las marcas de referencia"""
		marcas=lugares.all()
		
		template_values = {
			'lista_lugares': marcas,
		}
		path = os.path.join(os.path.dirname(__file__), 'templates/index.html')	
		self.response.out.write(template.render(path, template_values))