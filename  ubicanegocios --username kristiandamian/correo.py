#!/usr/bin/env python

from google.appengine.api import mail
from google.appengine.ext import webapp
from modelos import usuarios
import os
from google.appengine.ext.webapp import template

from google.appengine.ext.db import Key

class envioCorreoConfirmacion(webapp.RequestHandler): 
    def post(self):             
        correo = self.request.get('correo')
        
        usuario=usuarios()
        usuario.correo=correo
        usuario.validado=False
        usuario.put()       
        
        
        url="http://ubicanegocios.appspot.com/validacuenta/?id=%i" % usuario.key().id()
        
        textoCorreo="Estimad@ usuari@: \n"
        
        textoCorreo+="El equipo de ubicanegocios.com le comunica que se ha intentado crear"
        textoCorreo+="una cuenta con su direccion de correo electronico.\n\n"        
        textoCorreo+="Si esta de acuerdo en crear dicha cuenta por favor haga click en el link adjunto,"
        textoCorreo+="o copie y pegue la direccion en su navegador\n\n"
        textoCorreo+=url
        textoCorreo+="\n\n"
        textoCorreo+="Le agradecemos el interes en nuestro sitio y esperamos sus comentarios\n\n"
        
        textoCorreo+="Saludos."
        
        mail.send_mail(sender="kristiandamian@gmail.com",
              to=correo,
              subject="Su cuenta de ubicanegocios.com",
              body=textoCorreo)
        
        return False
        
    
class ValidaCuenta(webapp.RequestHandler):
    def get(self,id):
        """Marco como validado el correo y le doy las gracias al usuario"""
        Myid=self.request.get('id')
        usuario=usuarios.get_by_id(int(Myid))
        validado=usuario.validado
        usuario.validado=True
        usuario.put()
        path = os.path.join(os.path.dirname(__file__), 'templates/gracias.html')
                
        self.response.out.write(template.render(path,None))
        return False
    