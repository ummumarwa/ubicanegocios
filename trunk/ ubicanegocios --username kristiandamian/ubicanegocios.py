import cgi
import wsgiref.handlers

from MainPage import MainPage
from correo import envioCorreoConfirmacion, ValidaCuenta, ValidaLogin
from alta import alta
from altaajax import altaajax, bajaajax, objAjax
from altaempresas import pantallaAltaEmpresas
from abc import abc
from login import pantallalogin
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app



#Defino  la pantalla principal dentro de la clase MainPage
application = webapp.WSGIApplication([
        ('/', MainPage),
        ('/alta',alta),
        ('/altaajax',altaajax),
        ('/bajaajax',bajaajax),
        ('/objAjax',objAjax),
        ('/login',pantallalogin),        
        ('/enviocorreo',envioCorreoConfirmacion),
        ('/validologin',ValidaLogin),
        ('/altaempresas/(.*)',pantallaAltaEmpresas),
        ('/validacuenta/(.*)',ValidaCuenta),
        ('/abc',abc)],debug=True)


def main():
    run_wsgi_app(application)

#si lo corro como funcion principal que hago? Creo una instancia de application
if __name__ == '__main__':
  main()