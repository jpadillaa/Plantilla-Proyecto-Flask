from apirest import api
from apirest.views import RecursoRegistro, RecursoLogin
### TODO: Importe las vistas de su proyecto

api.add_resource(RecursoRegistro, '/api/auth/registro')
api.add_resource(RecursoLogin, '/api/auth/login')

### TODO: Agregue las rutas de sus endpoints 