from flask import Flask,redirect,url_for,render_template,request, redirect, url_for
from flaskext.mysql import MySQL
from pymysql.cursors import Cursor

app=Flask(__name__)

#Conexion con BBDD MYSQL
mysql =MySQL()
app.config['MYSQL_DATABASE_HOST']= 'localhost'
app.config['MYSQL_DATABASE_USER']= 'root'
app.config['MYSQL_DATABASE_PASSWORD']= ''
app.config['MYSQL_DATABASE_DB']= 'centroconocimiento'
mysql.init_app(app)


# Iniciamos app
@app.route('/')

def home():
    #Conexion a la MySQL
    # sql ="INSERT INTO `empleados` (`id`, `nombre`, `corrreo`, `foto`) VALUES (NULL, 'Pedro', 'pedro@atsistemas.com', 'foto2.jpeg');"
    # conn=mysql.connect()
    # cursor=conn.cursor()
    # cursor.execute(sql)
    # conn.commit()

    if request.method=='POST':
        # Handle POST Request here
        return render_template('empleados/index.html')
    return render_template('empleados/index.html')



@app.route('/create')
def create():
   
    return render_template('empleados/create.html',msg="Por favor inserta una foto")
    
@app.route('/store', methods=['POST'])
def store():
   _nombre=request.form['txtNombre']
   _correo=request.form['txtCorreo']
   _foto=request.files['txtFoto']
   
   sql ="INSERT INTO `empleados` (`id`, `nombre`, `corrreo`, `foto`) VALUES (NULL, %s, %s, %s);"
   datos =(_nombre,_correo,_foto.filename)

   conn=mysql.connect()
   cursor=conn.cursor()
   cursor.execute(sql,datos)
   conn.commit()
   return render_template('empleados/index.html')

# Inicio de programa
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)