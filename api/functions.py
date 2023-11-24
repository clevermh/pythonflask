from db.db import session
from sqlalchemy import select
from db.models import Auditoria
from db.models import Funcionalidad
from sqlalchemy.orm import Session


def generic_post(data):
    try:
        session.add(data)
        session.commit()
        session.refresh(data)
    # except:
    except Exception as e:
        session.rollback()
        raise Exception("Error al crear el registro")
    return data


def get_auditoria():
    query = session.query(
        Auditoria.id_auditoria,
        Auditoria.id_usuario,
        Auditoria.modulo,
        Auditoria.link,
        Auditoria.icono,
        Auditoria.fecha_creacion,
    ).all()

    return [dict(i) for i in query]


def create_auditoria(data):
    auditoria = Auditoria(**data)
    auditoria_db = generic_post(auditoria)
    return auditoria_db


def get_funcionalidad():
    query = session.query(
        Funcionalidad.id_funcionalidad, 
        Funcionalidad.nombre_funcionalidad,
        Funcionalidad.link,
        Funcionalidad.icono,
        Funcionalidad.fecha_creacion,
    ).all()

    return [dict(i) for i in query]


def create_funcionalidad(data):
    funcionalidad = Funcionalidad(**data)
    funcionalidad_db = generic_post(funcionalidad)
    return funcionalidad_db

 