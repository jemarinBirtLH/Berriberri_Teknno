# app.pyimport os
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_123')

# Datos de la empresa
empresa_info = {
    "nombre": "BerriBerri Teknno",
    "slogan": "Tecnología renovada para un futuro nuevo",
    "descripcion": "Servicio de recogida, reparación y reacondicionamiento de equipos tecnológicos",
    "servicios": [
        {
            "titulo": "Reacondicionamiento Tecnológico",
            "descripcion": "Recogemos, reparamos y actualizamos equipos tecnológicos, promoviendo la economía circular.",
            "icono": "fas fa-laptop-code"
        },
        {
            "titulo": "Formación en Habilidades Digitales",
            "descripcion": "Talleres presenciales y online de competencias digitales básicas y avanzadas.",
            "icono": "fas fa-chalkboard-teacher"
        },
        {
            "titulo": "Mantenimiento Integral",
            "descripcion": "Suscripciones de mantenimiento preventivo y correctivo a demanda para empresas.",
            "icono": "fas fa-tools"
        }
    ],
    "valores": [
        {
            "titulo": "Sostenibilidad",
            "descripcion": "Promovemos la economía circular reutilizando tecnología."
        },
        {
            "titulo": "Accesibilidad",
            "descripcion": "Tecnología asequible y formación para todos."
        },
        {
            "titulo": "Innovación",
            "descripcion": "Soluciones creativas e integradoras."
        },
        {
            "titulo": "Compromiso Social",
            "descripcion": "Atención especial a colectivos vulnerables."
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', empresa=empresa_info, now=datetime.now())

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', empresa=empresa_info, now=datetime.now())

@app.route('/formacion')
def formacion():
    return render_template('formacion.html', empresa=empresa_info, now=datetime.now())

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        
        flash(f'Gracias {nombre}, hemos recibido tu mensaje. Te contactaremos pronto.', 'success')
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html', empresa=empresa_info, now=datetime.now())

@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html', empresa=empresa_info, now=datetime.now())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('DEBUG', False))