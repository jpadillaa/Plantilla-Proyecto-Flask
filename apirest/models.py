from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from apirest import ma, db

'''
Modelos
'''
class Admin(db.Model):
    nombres = db.Column(db.String(200))
    apellidos = db.Column(db.String(200))
    email = db.Column(db.String(100), primary_key=True)
    pw = db.Column(db.String(100))

    def hashear_clave(self):
        '''
        Hashea la clave en la base de datos
        '''
        self.pw = generate_password_hash(self.pw, 'sha256')

    def verificar_clave(self, clave):
        '''
        Verifica la clave hasheada con la del parámetro
        '''
        return check_password_hash(self.pw, clave)

### TODO: Agregue los modelos de su proyecto 

'''
Schemas
'''
class AdminSchema(ma.Schema):
    '''
    Representa el schema de un admin
    '''
    class Meta:
        fields = ("nombres", "apellidos", "email", "pw")

admin_schema = AdminSchema()

### TODO: Agregue los schemas de su proyecto 
