import cgi
import wsgiref.handlers

from MainPage import MainPage
from alta import alta
from altaajax import altaajax, bajaajax
from abc import abc
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


#Defino  la pantalla principal dentro de la clase MainPage
application = webapp.WSGIApplication([
        ('/', MainPage),
        ('/alta',alta),
        ('/altaajax',altaajax),
        ('/bajaajax',bajaajax),
        ('/abc',abc)],debug=True)


def main():
  run_wsgi_app(application)

#si lo corro como funcion principal que hago? Creo una instancia de application
if __name__ == '__main__':
  main()