#!/usr/bin/env python
import cgi
from modelos import idiomas, estados, tipos_lugares
from google.appengine.ext import db
from google.appengine.ext import webapp

#import simplejson 

#para traer el json

from django.utils import simplejson
#from django.core.serializers import serialize

class altaajax(webapp.RequestHandler):
    def post(self):
        objeto = self.request.get('tipoObjeto')
        dato=self.request.get('Dato')
        instanciaDB=None;
        if objeto=="Idioma":
            instanciaDB=idiomas(idioma=dato)            
        elif objeto=="Estados": 
            instanciaDB=estados(estado=dato)
        else:
            instanciaDB=tipos_lugares(tipo=dato)            
        instanciaDB.put()
        return False

class bajaajax(webapp.RequestHandler):
    def post(self):
        objeto = self.request.get('tipoObjeto')
        dato=self.request.get('Dato')
        DB=None;
        campo=None;
        if objeto=="Idioma":
            DB="idiomas"
            campo="idioma"
        elif objeto=="Estados": 
            DB="estados"
            campo="estado"
        else:
            DB="tipos_lugares"
            campo="tipo"
            
        q = db.GqlQuery("SELECT * FROM "+DB+" WHERE "+campo+" = '"+dato+"'")
        for campos in q:
            campos.delete() #ejecuto la consulta y borro uno por uno
        return False
    
class objAjax (webapp.RequestHandler):
    def addKey(self,diccionario,key,data):
        diccionario={key:data}
        return diccionario
    
    def obtengoidiomas(self):
        """Obtengo el campo idioma del objeto Idiomas"""
        jsondic={}
        jsondata=[]
        for datos in idiomas.all():            
            jsondata+=[self.addKey(jsondic,"Dato", datos.idioma)]
        return jsondata
    
    def obtengoestados(self):
        jsondic={}
        jsondata=[]
        for datos in estados.all():
            jsondata+=[self.addKey(jsondic,"Dato", datos.estado)]                       
        return jsondata
    
    def obtengolugares(self):
        jsondic={}
        jsondata=[]
        for datos in tipos_lugares.all():            
            jsondata+=[self.addKey(jsondic,"Dato",datos.tipo)]
        return jsondata
    
    def post(self):
        objeto = self.request.get('tipoObjeto')        
        jsondata=[]
        if objeto=="Idioma":
            jsondata=self.obtengoidiomas()
        elif objeto=="Estados": 
            jsondata=self.obtengoestados()
        else:
            jsondata=self.obtengolugares()                    
        self.response.out.write(simplejson.dumps(jsondata))
        return False
    

