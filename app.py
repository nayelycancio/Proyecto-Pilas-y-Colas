from flask import Flask, render_template, request, redirect, url_for
from models.cola import ColaTarjetas
from models.pila import PilaApoyos

app = Flask(__name__)

# Instancias globales para el sistema
cola_tarjetas = ColaTarjetas()
historial_apoyos = PilaApoyos()

@app.route("/", methods=["GET"])
@app.route("/menu", methods=["GET"])
def menu():
    return render_template("menu.html")

@app.route("/cola", methods=["GET"])
def cola():
    return render_template("cola.html", cola=cola_tarjetas.mostrar_cola(), cola_vacia=cola_tarjetas.esta_vacia())

@app.route("/cola/agregar", methods=["POST"])
def agregar_a_cola():
    nombre = request.form.get("nombre")
    if nombre:
        cola_tarjetas.encolar(nombre)
    return redirect(url_for("cola"))

@app.route("/cola/atender", methods=["POST"])
def atender_cola():
    if not cola_tarjetas.esta_vacia():
        persona_atendida = cola_tarjetas.desencolar()
        # Aquí podrías agregar lógica adicional para registrar la entrega de la tarjeta
    return redirect(url_for("cola"))

@app.route("/pila", methods=["GET"])
def pila():
    return render_template("pila.html", historial=historial_apoyos.mostrar_pila(), pila_vacia=historial_apoyos.esta_vacia())

@app.route("/pila/agregar", methods=["POST"])
def agregar_apoyo():
    apoyo = request.form.get("apoyo")
    monto = request.form.get("monto")
    
    if apoyo:
        if monto and monto != "":
            descripcion = f"{apoyo} - ${monto}"
        else:
            descripcion = apoyo
        historial_apoyos.empilar(descripcion)
    return redirect(url_for("pila"))

@app.route("/pila/quitar", methods=["POST"])
def quitar_apoyo():
    if not historial_apoyos.esta_vacia():
        apoyo_quitado = historial_apoyos.desempilar()
        # Aquí podrías agregar lógica adicional para registrar la acción de quitar
    return redirect(url_for("pila"))

if __name__ == "__main__":
    app.run(debug=True)