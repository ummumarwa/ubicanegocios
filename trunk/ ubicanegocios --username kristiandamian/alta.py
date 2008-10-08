import cgi
import wsgiref.handlers
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from modelos import lugares

class alta (webapp.RequestHandler):    
    def get(self):
        """Muestro la pantalla para altas de marcas"""
        marcas=lugares.all()
        template_values = {
            'lista_lugares': marcas,
        }
        path = os.path.join(os.path.dirname(__file__), 'templates/alta.html')
        self.response.out.write(template.render(path,template_values))