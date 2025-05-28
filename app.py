# app.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 

# Inicializa la aplicación Flask
app = Flask(__name__)

# Habilita CORS para todas las rutas.
CORS(app)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trenes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la extensión SQLAlchemy con la aplicación Flask
db = SQLAlchemy(app)

# Define el modelo de datos para la tabla 'Tren' en la base de datos.
class Tren(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(80), unique=True, nullable=False)
    origen = db.Column(db.String(120), nullable=False)
    destino = db.Column(db.String(120), nullable=False)
    empresa = db.Column(db.String(120), nullable=False)
    # Nuevos campos
    fecha = db.Column(db.String(120), nullable=False)    # Para almacenar la fecha como texto (ej. YYYY-MM-DD)
    estatus = db.Column(db.String(120), nullable=False)  # Para almacenar el estatus (ej. "En Hora", "Retrasado")
    situacion = db.Column(db.String(120), nullable=False) # Para almacenar la situación (ej. "Andén 5", "En Ruta")


    def __repr__(self):
        return f'<Tren {self.numero}>'

    # Método para convertir el objeto Tren en un diccionario, incluyendo los nuevos campos.
    def to_dict(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'origen': self.origen,
            'destino': self.destino,
            'empresa': self.empresa,
            'fecha': self.fecha,
            'estatus': self.estatus,
            'situacion': self.situacion
        }

# Bloque que se ejecuta una vez al iniciar la aplicación para crear las tablas de la base de datos
# si aún no existen.
with app.app_context():
    db.create_all()

# --- Rutas de la API (Endpoints) ---

# Ruta para la página principal que renderiza el HTML.
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener todos los trenes o añadir un nuevo tren.
@app.route('/trenes', methods=['GET', 'POST'])
def handle_trenes():
    if request.method == 'GET':
        trenes = Tren.query.all()
        return jsonify([tren.to_dict() for tren in trenes])
    elif request.method == 'POST':
        data = request.get_json()
        # Validar que todos los campos requeridos estén presentes, incluyendo los nuevos
        required_fields = ('numero', 'origen', 'destino', 'empresa', 'fecha', 'estatus', 'situacion')
        if not data or not all(k in data for k in required_fields):
            return jsonify({'message': f'Datos incompletos. Se requieren: {", ".join(required_fields)}'}), 400
        
        nuevo_tren = Tren(
            numero=data['numero'],
            origen=data['origen'],
            destino=data['destino'],
            empresa=data['empresa'],
            fecha=data['fecha'],
            estatus=data['estatus'],
            situacion=data['situacion']
        )
        db.session.add(nuevo_tren)
        db.session.commit()
        return jsonify(nuevo_tren.to_dict()), 201

# Ruta para obtener, actualizar o eliminar un tren específico por su ID.
@app.route('/trenes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_single_tren(id):
    tren = Tren.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(tren.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        
        if 'numero' in data:
            tren.numero = data['numero']
        if 'origen' in data:
            tren.origen = data['origen']
        if 'destino' in data:
            tren.destino = data['destino']
        if 'empresa' in data:
            tren.empresa = data['empresa']
        # Actualizar los nuevos campos si están presentes
        if 'fecha' in data:
            tren.fecha = data['fecha']
        if 'estatus' in data:
            tren.estatus = data['estatus']
        if 'situacion' in data:
            tren.situacion = data['situacion']
        
        db.session.commit()
        return jsonify(tren.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(tren)
        db.session.commit()
        return jsonify({'message': 'Tren eliminado'}), 204

# Bloque principal para ejecutar la aplicación Flask.
if __name__ == '__main__':
    app.run(debug=True)
