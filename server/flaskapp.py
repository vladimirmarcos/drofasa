
import ast
from flask import Flask,render_template,request, redirect, url_for, flash,session
from system.conexion.basedatos import searchalldata
import math
import datetime
from base import convertintegretdata
app = Flask(__name__)
items=searchalldata("iva")
drogas = ["","","","",""]
cantidades = [0,0,0,0,0]
precios = [0.0,0.0,0.0,0.0,0.0]

app.secret_key = "tu_clave_secreta_aqui"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Obtener los elementos seleccionados
        selected_item = request.form.getlist('selected_items') 
        if len(selected_item) != 1:
            flash("Se debe seleccionar un elemento.")
            return redirect(url_for('home'))
        else:
            selected_item=ast.literal_eval(selected_item[0])
            return redirect("index.html", items=items)
    return render_template("index.html", items=items)

@app.route("/conceptodecompra", methods=["GET", "POST"])
def conceptodecompra():
    auxiliar=searchalldata("conceptocompra")
    concompra=[list(tupla) for tupla in auxiliar]
    for i in concompra:
            i[2]=convertintegretdata("iva", "nombre", i[2])
            i[3]=convertintegretdata("siap","nombre",i[3])
            i[4]=convertintegretdata("cuentacontable","nombre",i[4])
            i[5]=convertintegretdata("cuentastesoreria","nombre",i[5])
    if request.method == 'POST':
        items_per_page = int(request.form['items_per_page'])
        session['items_per_page'] = items_per_page
    else:
        items_per_page = session.get('items_per_page', 10)
    total_items = len(concompra)
    total_pages = math.ceil(total_items / items_per_page)
    page = int(request.args.get('page', 1))
    start = (page - 1) * items_per_page
    end = start + items_per_page
    displayed_items = concompra[start:end]
    return render_template('conceptodecompra.html', 
                           items=displayed_items, page=page, 
                           total_pages=total_pages, 
                           items_per_page=items_per_page,
                           cabeceras=["ID","Concepto","I.V.A","Clasificación S.I.A.P.","Cuenta Contable","Cuenta Tesorería"],
                           titulo="Conceptos de Compras")

@app.route("/iva", methods=["GET", "POST"])
def iva():
    auxiliar=searchalldata("iva")
    iva=[list(tupla) for tupla in auxiliar]
    if request.method == 'POST':
        items_per_page = int(request.form['items_per_page'])
        session['items_per_page'] = items_per_page
    else:
        items_per_page = session.get('items_per_page', 10)
    total_items = len(iva)
    total_pages = math.ceil(total_items / items_per_page)
    page = int(request.args.get('page', 1))
    start = (page - 1) * items_per_page
    end = start + items_per_page
    displayed_items = iva[start:end]
    return render_template('iva.html', 
                           items=displayed_items, page=page, 
                           total_pages=total_pages, 
                           items_per_page=items_per_page,cabeceras=["ID","IVA","Monto"],
                           titulo="Tipos de I.V.A.")

@app.route("/pf", methods=["GET", "POST"])
def fnp():
    auxiliar=searchalldata("proveedores")
    proveedores=[list(tupla) for tupla in auxiliar]
    today_date = datetime.datetime.today().strftime('%Y-%m-%d')
    if request.method == "POST":
        fecha = request.form.get("fecha") 
        tipo = request.form.get("tipo") 
        return redirect(url_for('cpm'))
        
    return render_template('proveedores/pf.html',
                           items=proveedores,
                           titulo="Conceptos de Compras",today_date =today_date )
    
@app.route("/cpm",methods=["GET", "POST"])
def cpm():
    auxiliar=searchalldata("droga")
    opciones=[list(tupla) for tupla in auxiliar]
    itemoption = [item[1] for item in opciones]
    if request.method == "POST":
        for i in range(0, 4):  
            cantidades[i] = int(request.form.get(f'cantidad{i}'))
            precios[i] = float(request.form.get(f'precio{i}'))
            drogas[i]=request.form.get(f'droga{i}')
        return redirect(url_for('lotesingreso')) 
    return render_template("cpm.html", drogas=drogas, cantidades=cantidades, precios=precios,opciones=itemoption)

@app.route("/lotesingreso")
def lotesingreso():
    opcion=[elemento for elemento in drogas if elemento != ""]
    codigostotales=[elemento for elemento in drogas if elemento != ""]
    listavalores=[elemento for elemento in cantidades if elemento != 0]
    diccionario = dict(zip(codigostotales, listavalores))
    return render_template('lotes/lotesingreso.html', cantidadesRequeridas=diccionario, codigos=codigostotales,opciones=opcion)

def run_flask():
    app.run(port=5000, debug=True,use_reloader=False)