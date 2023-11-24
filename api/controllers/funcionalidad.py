from flask import Blueprint, jsonify, request, abort
from flask_restplus import Api, Resource, fields
 
from api.functions import get_funcionalidad

bp_api_fun = Blueprint("Api", __name__, url_prefix="/api")

api = Api(bp_api_fun, version="1.0", title="Api", description="End Points")
ns_model = api.namespace("Methods", description="Metodos")
ns_model_funcionalidad = api.namespace("funcionalidad", description="Funcionalidad")



class VerificarDatos:
    CrearTb_seg_funcionalidad = api.model(
        "tb_auditoria",
        {
            "id_funcionalidad": fields.Integer(
                description="Id funcionalidad",
                required=True,
            ),
            "nombre_funcionalidad": fields.String(
                description="funcionalidad modulo",
                required=True,
            ),
          
            "link": fields.String(
                description="link",
            ),
            "icono": fields.String(
                description="icono",
            ),
        },
    )


@ns_model_funcionalidad.route("/")
@api.doc(description="Funcionalidad")
class Funcionalidad(Resource):
    def get(self):
        funcionalidad = get_funcionalidad()
        return jsonify(funcionalidad)

    @ns_model_funcionalidad.expect(VerificarDatos.CrearTb_seg_funcionalidad, validate=True)
    def post(self):
        try:
            funcionalidad_db = create_funcionalidad(request.json)
        except Exception as e:
            abort(400, str(e))
        return jsonify(
            {
                "auditoria_id": funcionalidad_db.id_funcionalidad,
                "message": "Auditoria creada exitosamente",
            }
        )

@ns_model_funcionalidad.route("/")
@api.doc(description="Funcionalidad")
class Funcionalidad(Resource):
    def get(self):
        funcionalidad = get_funcionalidad()
        return jsonify(funcionalidad)

    @ns_model_funcionalidad.expect(VerificarDatos.CrearTb_seg_funcionalidad, validate=True)
    def post(self):
        try:
            funcionalidad_db = create_funcionalidad(request.json)
        except Exception as e:
            abort(400, str(e))
        return jsonify(
            {
                "auditoria_id": funcionalidad_db.id_funcionalidad,
                "message": "Auditoria creada exitosamente",
            }
        )