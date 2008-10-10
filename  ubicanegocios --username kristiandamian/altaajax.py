#!/usr/bin/env python
import cgi
from modelos import idiomas, estados, tipos_lugares
from google.appengine.ext import db
from google.appengine.ext import webapp

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