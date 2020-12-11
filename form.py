import dbConnector
from custom_validators import height_validator,weight_validator
import requests
import json

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators, SubmitField, SelectField, IntegerField

db = dbConnector.dbConnector()
db.build_table()

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SeCrEt'

class Questionnaire(Form):

    nombreunidadproductiva = TextField('Nombre_unidad_productiva:',[validators.InputRequired()])
    callenumero = TextField('Calle_y_numero:',[validators.InputRequired()])
    localidad = TextField('Localidad:',[validators.InputRequired()])
    rubro = TextField('Rubro:',[validators.InputRequired()])
    aniorecuperacion = IntegerField('Año_de_recuperacion:',[validators.InputRequired()])

    feelings_options = requests.get('http://localhost:8081/categories').json()
    feelings_options2 = requests.get('http://localhost:8081/categories/1/subcategories').json()
    feelings_options3 = requests.get('http://localhost:8081/business-area').json()
    
    lista_tupla=[]
    lista_tupla2=[]
    lista_tupla3=[]
    
    for i in feelings_options:
        tupla=(i['id'],i['name'])
        lista_tupla.append(tupla)
    for ii in feelings_options2:
        tupla=(ii['id'],ii['name'])
        lista_tupla2.append(tupla)
    for iii in feelings_options3:
        tupla=(iii['id'],iii['name'])
        lista_tupla3.append(tupla)



    feelings = SelectField('Feelings about yourself:',coerce=int, \
        choices=lista_tupla,validators=[validators.InputRequired()])
    
    subcategoria = SelectField('Feelings about yourself:',coerce=int, \
        choices=lista_tupla2,validators=[validators.InputRequired()])
    
    rubro = SelectField('Feelings about yourself:',coerce=int, \
        choices=lista_tupla3,validators=[validators.InputRequired()])

 
@app.route("/", methods=['GET', 'POST'])
def form_handling():

    form = Questionnaire(request.form)

    values = (form.nombreunidadproductiva.data,form.callenumero.data,form.localidad.data,form.aniorecuperacion.data,form.feelings.data,form.subcategoria.data,form.rubro.data)
    

    if request.method == 'POST':
        print(values)
        
        if form.validate():
            print("EMA, TOMA")
            requestjson={
                "name": form.nombreunidadproductiva.data,
                "initializedAt": form.aniorecuperacion.data,
                "street": form.callenumero.data,
                "streetNumber": "975",
                "district": "Avellaneda",
                "province": "Buenos Aires",
                "country": "Argentina",
                "locality": form.localidad.data,
                "services": "Servicios",
                "baseOrganization": "organizacion base",
                "federation": "Federación",
                "articulations": "articulaciones",
                "referent": "Alguien",
                "mail": "mail@mail.com",
                "phone": "111111111111",
                "website": "website.com.ar",
                "categoryId": form.feelings.data,
                "subcategoryId": form.subcategoria.data,
                "businessAreaId": form.rubro.data
            }
            
            print(requestjson)
            
            postresponse = requests.post('http://localhost:8081/entities', data = requestjson)
            
            print(postresponse)
            
            flash('Success!','success')

        else:
            flash('Error:'+str(form.errors),'danger')

    return render_template('index.html', form=form)

@app.route('/categorias')
def categorias():
    categorias_json = requests.get('https://run.mocky.io/v3/3d10418b-2e5c-479b-8dfb-cc28ad0bee99').json()
    categoria_elegida = "Emprendedores"
    indice_categoria_elegida = 0

    for categoria in categorias_json:
        if categoria["name"] == categoria_elegida:
            indice_categoria_elegida = categoria["id"]
    print("ID de la categoria harcodeada en el codigo:")
    print(indice_categoria_elegida)

    return render_template('test.html', colours=categorias_json)

class Questionnaire2(Form):

    name = TextField('Name:',[validators.InputRequired()])
    surname = TextField('Surname:',[validators.InputRequired()])
    email = TextField('Email:',[validators.InputRequired(),validators.Email()])
    weight = TextField('Weight (kg):',[validators.InputRequired(),weight_validator])
    height = TextField('Height (kg):',[validators.InputRequired(),height_validator])
    edad = TextField('edad:',[validators.InputRequired(),height_validator])

    feelings_options = requests.get('https://run.mocky.io/v3/3d10418b-2e5c-479b-8dfb-cc28ad0bee99').json()
    #print(feelings_options)
    lista=[]
    for i in feelings_options:
        lista.append(i['name'])
    print("lista: ",lista)
    feelings_options=lista
    feelings_options = [(1,'Bad!!!!'),(2,'OK'),(3,'Good')]

    feelings = SelectField('Feelings about yourself:',coerce=int, \
        choices=feelings_options,validators=[validators.InputRequired()])



@app.route('/categorias2')
def categorias2():
    form = Questionnaire2(request.form)
    categorias_json = requests.get('https://run.mocky.io/v3/3d10418b-2e5c-479b-8dfb-cc28ad0bee99').json()
    categoria_elegida = "Emprendedores"
    indice_categoria_elegida = 0

    for categoria in categorias_json:
        if categoria["name"] == categoria_elegida:
            indice_categoria_elegida = categoria["id"]
    print("ID de la categoria harcodeada en el codigo:")
    print(indice_categoria_elegida)

    return render_template('test.html', colours=categorias_json)


if __name__ == "__main__":
    app.run(debug=True)
