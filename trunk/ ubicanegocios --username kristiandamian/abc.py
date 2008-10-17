#!/usr/bin/env python

import cgi
import wsgiref.handlers
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from modelos import idiomas, estados, ciudades

class abc (webapp.RequestHandler):    
    def get(self):
        """Muestro el ABC de los objetos sencillos"""
        path = os.path.join(os.path.dirname(__file__), 'templates/abc.html')
        listaidiomas = {
            'listaidiomas':idiomas.all(),
            'listaestados':estados.all(),            
        }
        self.response.out.write(template.render(path,listaidiomas))