from google.appengine.ext import db

class estados (db.Model):    
    estado=db.StringProperty(required=True)
    

class idiomas (db.Model):
    idioma=db.StringProperty(required=True)
    
class telefonos(db.Model):
    telefono = db.StringProperty(required=True)

    
class usuarios(db.Model):    
    usuario= db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    nombre = db.StringProperty(required=True)
    paterno = db.StringProperty(required=True)
    materno = db.StringProperty(required=True)
    fecha_nacimiento=db.DateProperty()
    fecha_alta =db.DateProperty()
    sexo=db.StringProperty()
    pregunta_secreta = db.StringProperty()
    respuesta_secreta = db.StringProperty()

class ciudades (db.Model):
    ciudad=db.StringProperty(required=True)
    estado=db.ReferenceProperty(estados)
       
class descripciones (db.Model):
    descripcion=db.StringProperty(required=True)
    idioma=db.ReferenceProperty(idiomas)  

class empresas (db.Model):
    nombre=db.StringProperty(required=True)
    calle=db.StringProperty(required=True)
    codigo_postal=db.IntegerProperty()
    numeroExterior=db.IntegerProperty()    
    numeroInterior=db.IntegerProperty()
    colonia=db.StringProperty()
    id_Ciudad=db.ReferenceProperty(ciudades)
    piso=db.IntegerProperty()
    andador=db.StringProperty()
    sitioweb=db.LinkProperty()
    correo=db.EmailProperty()
    nombreContacto = db.StringProperty()
    paternoContacto= db.StringProperty()
    maternoContacto= db.StringProperty()
    telefonos=db.ReferenceProperty(telefonos)
    
class tipos_lugares(db.Model):
    tipo=db.StringProperty(required=True)
    
    
class lugares (db.Model):
    descripcion = db.StringProperty()
    longitud = db.FloatProperty()
    latitud = db.FloatProperty()
    tipo = db.ReferenceProperty(tipos_lugares)
    empresa = db.ReferenceProperty(empresas)
    calle = db.StringProperty()
    numero_exterior = db.IntegerProperty()
    numero_interior = db.IntegerProperty()
    colonia = db.StringProperty()
    ciudad = db.ReferenceProperty(ciudades)
    piso = db.IntegerProperty()
    andador  = db.StringProperty()
    sitioWeb = db.LinkProperty()
    correo = db.EmailProperty()
    usuario=db.ReferenceProperty(usuarios)
    descripciones=db.ReferenceProperty(descripciones)
    telefonos=db.ReferenceProperty(telefonos)

    