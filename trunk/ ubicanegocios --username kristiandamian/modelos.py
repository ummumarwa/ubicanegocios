from google.appengine.ext import db

class estados (db.Model):    
    estado=db.StringProperty()
    

class idiomas (db.Model):
    idioma=db.StringProperty()
    
class telefonos(db.Model):
    telefono = db.StringProperty()

    
class usuarios(db.Model):    
    usuario= db.StringProperty()
    password = db.StringProperty()
    nombre = db.StringProperty()
    paterno = db.StringProperty()
    materno = db.StringProperty()
    fecha_nacimiento=db.DateProperty()
    fecha_alta =db.DateProperty()
    sexo=db.StringProperty()
    pregunta_secreta = db.StringProperty()
    respuesta_secreta = db.StringProperty()

class ciudades (db.Model):
    ciudad=db.StringProperty()
    estado=db.ReferenceProperty(estados)
       
class descripciones (db.Model):
    descripcion=db.StringProperty()
    idioma=db.ReferenceProperty(idiomas)  

class empresas (db.Model):
    nombre=db.StringProperty()
    calle=db.StringProperty()
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
    tipo=db.StringProperty()
    
    
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

    