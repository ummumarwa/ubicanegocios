import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from modelos import ciudades, empresas, telefonos
from django.utils import simplejson

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

class GraboTel(webapp.RequestHandler):
    def post(self):
        """Grabo un telefono"""
        id=self.request.get('id')
        telefono=self.request.get('telefono')
        empresa=empresas.get_by_id(int(id))        
        tel=telefonos(parent=empresa,telefono=telefono)
        
        tel.put()
        return False

class GraboEmpresas(webapp.RequestHandler):
    def addKey(self,diccionario,key,data):
        diccionario={key:data}
        return diccionario
    
    def validonumero(self,num):
        if len(num)<=0:
            num="0"
        return num
    
    def post(self):
        """Grabo los datos y devuelvo el ID - pa los telefonos"""
        piso=self.request.get('piso')
        numext=self.request.get('numext')
        numint=self.request.get('numint')
        piso=self.validonumero(piso)
        numext=self.validonumero(numext)
        numint=self.validonumero(numint)
        
        empresa=empresas()
        empresa.nombre=self.request.get('desc')
        empresa.calle=self.request.get('calle')
        empresa.numeroExterior=int(numext)
        empresa.numeroInterior=int(numint)
        empresa.colonia=self.request.get('colonia')
        empresa.piso=int(piso)
        empresa.andador=self.request.get('andador')
        empresa.codigo_postal=int(self.request.get('cp'))
        empresa.sitioweb=self.request.get('web')
        empresa.correo=self.request.get('mail')
        empresa.nombreContacto=""
        empresa.paternoContacto=""
        empresa.maternoContacto=""
        #### 
        ciudad=self.request.get('ciudad')
        query="where ciudad='%s'"%ciudad
        cd=ciudades.gql(query)
        city=cd.fetch(1)
        for lstcd in city:
            empresa.id_Ciudad=lstcd.key().id()
        empresa.put()
        jsondic={}
        jsondata=[]
        jsondata+=[self.addKey(jsondic,"Dato", empresa.key().id())]
        self.response.out.write(simplejson.dumps(jsondata))
        return False