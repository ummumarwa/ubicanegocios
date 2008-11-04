#!/usr/bin/env python

from google.appengine.api import mail
from google.appengine.ext import webapp
from modelos import usuarios
import os

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson

from google.appengine.ext.webapp import template

from google.appengine.ext.db import Key

class envioCorreoConfirmacion(webapp.RequestHandler):
    def addKey(self,diccionario,key,data):
        diccionario={key:data}
        return diccionario
    
    def validocorreo(self,correo):
        """Verifico si ese usuario es nuevo"""
        valido=True
        query="where correo='%s'" % correo
        usuario=usuarios.gql(query)        
        for usr in usuario:
            valido=False
        return valido
    
    def post(self):             
        correo = self.request.get('correo')
        mensaje="Ocurrio un error en el envio del correo"
        if(self.validocorreo(correo)):
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
            textoCorreo+="Si ha recibido este correo por error no necesita hacer nada para cancelar la cuenta,\n"
            textoCorreo+="dicha cuenta no se activara y no recibira mas correos por nuestra parte\n\n"
            textoCorreo+="Le agradecemos el interes en nuestro sitio y esperamos sus comentarios\n\n"
            
            textoCorreo+="Saludos."
            mensaje="Se ha enviado un correo de confirmacion en la cuenta definida"
            mail.send_mail(sender="kristiandamian@gmail.com",
                  to=correo,
                  subject="Su cuenta de ubicanegocios.com",
                  body=textoCorreo)
        else:
            mensaje="Ese correo ya esta dado de alta en el sistema"
        jsondic={}
        jsondata=[]
        jsondata+=[self.addKey(jsondic,"Dato", mensaje)]
        self.response.out.write(simplejson.dumps(jsondata))
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
    
class ValidaLogin(webapp.RequestHandler):
    def addKey(self,diccionario,key,data):
        diccionario={key:data}
        return diccionario
    
    def post(self):
        """Valido que el correo este capturado y activo"""
        mensaje="Ocurrio un error en la consulta"
        correo=self.request.get('correo')
        query="where correo='%s'" % correo
        usuario=usuarios.gql(query)
        encontrado=False
        for usr in usuario:
            if usr.validado:
                encontrado=True
                break
        if encontrado:
            #HttpResponseRedirect("./altaempresas")
            mensaje="Login exitoso"
        else:
            mensaje="Usuario invalido"
        jsondic={}
        jsondata=[]
        jsondata+=[self.addKey(jsondic,"Dato", mensaje)]
        self.response.out.write(simplejson.dumps(jsondata))
        return jsondata