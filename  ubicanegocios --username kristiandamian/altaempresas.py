import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from modelos import ciudades

class pantallaAltaEmpresas(webapp.RequestHandler):
    def get(self,correo):
        correo=self.request.get('correo')
        path = os.path.join(os.path.dirname(__file__), 'templates/altaempresas.html')
        datos = {
            'correo':correo,
            'listaciudades':ciudades.all(),
        }
        self.response.out.write(template.render(path,datos))
        return False