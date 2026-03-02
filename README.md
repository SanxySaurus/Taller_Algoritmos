# Taller_Algoritmos

## Santiago Ramirez

## Santiago Gallego

## Kareem Andraos

# VademecumDB – API REST

Proyecto backend desarrollado en Flask para la gestión de un Vademécum.  
Permite administrar:

  * Grupos terapéuticos
  * Familias
  * Laboratorios
  * Enfermedades potenciales

Base de datos desarrollada en PostgreSQL.

# Normalización y Diseño de Tablas

El sistema fue estructurado utilizando SQLAlchemy con separación en entidades independientes y relaciones bien definidas.

Se definieron las siguientes tablas:

## Tabla therapeutic_groups

  * id (PK)
  * name (único, obligatorio)

## Tabla potential_illness

  * id (PK)
  * name (único, obligatorio)

## Tabla family

  * id (PK)
  * name (obligatorio)
  * potential_illness_id (FK → potential_illness.id)

Relación:
  * Una enfermedad potencial puede tener múltiples familias.
  * Se define mediante ForeignKey y relationship.

## Tabla laboratories

  * id (PK)
  * name (obligatorio)

Justificación:

  * Eliminación de redundancia.
  * Separación clara de entidades.
  * Uso correcto de claves primarias y foráneas.
  * Relación uno a muchos entre potential_illness y family.

# 2. Estructura del Proyecto

El proyecto está organizado por módulos:

common/
db/
routes/
  ├── family/
  ├── laboratories/
  ├── potential_illnesses/
  ├── therapeutic_groups/

Cada módulo contiene:
  * controller
  * service
  * routes

# Configuración de Base de Datos

Se utiliza PostgreSQL.

Base de datos sugerida:

vademecumDB

Archivo .env:

DB_URL=postgresql://postgres:TU_PASSWORD@localhost:5432/vademecumDB
HOST=127.0.0.1
PORT=5000

Reemplazar TU_PASSWORD por la contraseña de PostgreSQL.

# Inicialización

Para crear las tablas:

python db.init.py

# Ejecución del Proyecto

Crear entorno virtual:

python -m venv venv

Activar entorno (Windows):

venv\Scripts\activate

Instalar dependencias:

pip install flask flask-cors sqlalchemy psycopg2 python-dotenv

Ejecutar servidor:

python app.py

# CRUD Implementado

Se implementa CRUD completo para:

  * therapeutic_groups
  * family
  * laboratories
  * potential_illness

Operaciones disponibles:
  * Create
  * Read
  * Update
  * Delete

Las respuestas HTTP siguen formato estandarizado:

{
  "status": "success",
  "message": "Operación realizada correctamente",
  "data": {}
}


# Postman

https://santiagogallegob1419-3195064.postman.co/workspace/Santiago-Gallego's-Workspace~02319c38-b745-4d96-8a9b-1f8c3dfa0bec/collection/52305723-92846825-3108-4033-8540-9dd2470df237?action=share&creator=52305723&active-environment=52305723-ee8c621c-87e3-4e15-8043-d8528cb8ce89
https://santiagogallegob1419-3195064.postman.co/workspace/Santiago-Gallego's-Workspace~02319c38-b745-4d96-8a9b-1f8c3dfa0bec/collection/52305723-92846825-3108-4033-8540-9dd2470df237?action=share&creator=52305723&active-environment=52305723-ee8c621c-87e3-4e15-8043-d8528cb8ce89
