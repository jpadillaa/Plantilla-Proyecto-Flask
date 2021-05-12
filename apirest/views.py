import os
from datetime import timedelta
from flask import request, current_app, send_from_directory
from werkzeug.utils import secure_filename
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Api

from apirest import api, db
from apirest.models import Admin, admin_schema
### TODO: Importe sus modelos y sus schemas

'''
Recurso que administra el servicio de login
'''
class RecursoLogin(Resource):
    def post(self):
        request.get_json(force=True)
        usuario = Admin.query.get(request.json['email'])
        if usuario is None:
            return {'message':'El email ingresado no está registrado'}, 400
        if not usuario.verificar_clave(request.json['pw']):
            return {'message': 'Contraseña incorrecta'}, 400
        try:
            access_token = create_access_token(identity = request.json['email'], expires_delta=timedelta(days=1))
            return {
                'message':'Sesion iniciada',
                'access_token':access_token
            }
        except:
            return {'message':'Ha ocurrido un error'}, 500
    
'''
Recurso que administra el servicio de registro
'''
class RecursoRegistro(Resource):
    def post(self):
        if Admin.query.filter_by(email=request.json['email']).first() is not None:
            return {'message': f'El correo({request.json["email"]}) ya está registrado'}, 400
        if request.json['email'] == '' or request.json['pw'] == '' or request.json['nombres'] == '' or request.json['apellidos'] == '':
            return {'message': 'Campos invalidos'}, 400
        nuevo_admin = Admin(
            email = request.json['email'],
            pw = request.json['pw'],
            nombres = request.json['nombres'],
            apellidos = request.json['apellidos']
        )
        nuevo_admin.hashear_clave()

        try:
            db.session.add(nuevo_admin)
            db.session.commit()
            access_token = create_access_token(identity = request.json['email'], expires_delta=timedelta(days=1))
            return {
                'message': f'El correo {request.json["email"]} ha sido registrado',
                'access_token': access_token 
            }
        except:
            return {'message':'Ha ocurrido un error'}, 500

### TODO: Agregue sus recursos