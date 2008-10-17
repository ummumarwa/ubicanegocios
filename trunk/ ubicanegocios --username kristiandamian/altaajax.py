#!/usr/bin/env python
import cgi
from modelos import idiomas, estados, tipos_lugares, ciudades
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
        elif objeto=="Ciudades":
            estado=self.request.get('Estado')
            query="where estado = '"+estado+"' " 
            Estado=estados.gql(query )
            ObjEstado=Estado.fetch(1) #solo obtengo el primer registro, para evitar duplicados
            instanciaDB=ciudades(parent=ObjEstado[0],ciudad=dato)            
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
        elif objeto=="Ciudades":
            estado = self.request.get('Estado')
            DB=None
            campo=None
            #Borro las ciudades que se llamen igual, pero SOLO de ese estado
            query="where estado = '"+estado+"' " 
            Estado=estados.gql(query)
            ObjEstado=Estado.fetch(1) #solo obtengo el primer registro, para evitar duplicados
            
            for lstcd in ObjEstado:
                cities=ciudades.all().ancestor(lstcd)
                query="where ciudad = '"+dato+"' " 
                for city in cities:
                    if city.ciudad==dato:
                        city.delete()
        else:
            DB="tipos_lugares"
            campo="tipo"
        
        if not DB==None:
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
    
    def obtengoCiudades(self, estado):
        jsondic={}
        jsondata=[]
        query="where estado = '"+estado+"' " 
        Estado=estados.gql(query)
        ObjEstado=Estado.fetch(1) #solo obtengo el primer registro, para evitar duplicados
        
        for lstcd in ObjEstado:
            cities=ciudades.all().ancestor(lstcd)
            for city in cities:
                jsondata+=[self.addKey(jsondic,"Dato",city.ciudad)]
        return jsondata
    
    def post(self):
        objeto = self.request.get('tipoObjeto')        
        jsondata=[]
        if objeto=="Idioma":
            jsondata=self.obtengoidiomas()
        elif objeto=="Estados": 
            jsondata=self.obtengoestados()
        elif objeto=="Ciudades":
            jsondata=self.obtengoCiudades(estado=self.request.get('Estado'))
        else:
            jsondata=self.obtengolugares()                    
        self.response.out.write(simplejson.dumps(jsondata))
        return False