from google.appengine.ext import db


class idiomas (db.Model):
    idioma=db.StringProperty()

class estados (db.Model):    
    estado=db.StringProperty()
    #ciudades=db.ListProperty(db.Key)

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
       
class descripciones (db.Model):
    descripcion=db.StringProperty()
    idioma=db.ReferenceProperty(idiomas)  

class usuarios(db.Model):
    correo=db.StringProperty()
    validado=db.BooleanProperty()
    
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
    telefonos=db.ListProperty(db.Key)
    usuario=db.ReferenceProperty(usuarios)
    
class tipos_lugares(db.Model):
    tipo=db.StringProperty()
    
    
class lugares (db.Model):
    descripcion = db.StringProperty()
    longitud = db.FloatProperty()
    latitud = db.FloatProperty()
    tipo = db.ReferenceProperty(tipos_lugares)
    #empresa = db.ReferenceProperty(empresas) <- Se utilizara la propiedad "parent"
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
    telefonos=db.ListProperty(db.Key)

class telefonos(db.Model):
    telefono = db.StringProperty()

    