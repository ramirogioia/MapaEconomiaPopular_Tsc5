# Mapa Economia Popular - Trabajo Social Comunitario

---

 Mapa Economia Popular es un conjunto de recursos que ofrece los siguientes servicios:

- Grabado de formularios e informacion de interes para la Universidad Nacional de Avellaneda.
- Lectura de información desde la base de datos POSTGRESS de la facultad, tanto para la carga de categorias, subcategorias y los rubros.
- Conexión con una aplicacion backend implementada con NodeJS usada como intermediario entre la UI y la base de datos.
- Diseño de HTML que presenta un formulario WEB para ingresar informacion de interes.

**Desarrollo de Canales e Innovación**

Versión: 1.0

## Comenzando 🚀

---

_Clonar el proyecto:_

    git clone https://bitbucket.gscorp.ad/scm/du6/api-documental.git


### Pre-requisitos 📋

---

_Que cosas necesitas para instalar el software_

```
* Java 11
* gradle 5.6
* Docker
* SQL server 2017
```

**Administrador de versiones (Recomendado)**

- SDK https://sdkman.io/install

**Comandos SDK:**

_Instalar version java_

    sdk install java 11.0.4-open

_Instalar version gradle_

    sdk install gradle 5.6.1

**Instalar docker en ubuntu 18.04**

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

**Crear base de datos en docker**

_Extraer la imagen de contenedor de SQL Server 2017 para Linux desde el registro de contenedor de Microsoft._

    sudo docker pull mcr.microsoft.com/mssql/server:2017-latest

_Ejecutar la imagen de contenedor con Docker_

    sudo docker run --name mssql -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Password0401' -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-latest

_Para listar los containers ,y así obtener el < CONTAINER_ID > para reemplazarlo en el paso que sigue:_

    sudo docker ps -a

_Para acceder al container y crear la base de api-documental_

    sudo docker exec -it < CONTAINER_ID > /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Password0401' -Q 'CREATE DATABASE FormulariosDigitales'

_Levantar la base (antes de correr los test)_

    sudo docker start mssql

**Gestionar base de datos**

_por consola, luego de levantar la base_

    sudo docker exec -it sql-server "bash"
    ________________________________________________________________________________________________________________________
    
    #/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Password0401’

_por GUI: descargar dbeaver_

DBeaver https://dbeaver.io/download/

### Instalación 🔧

---

_Clonar el repositorio en la maquina local e instalar las dependencias con gradle_

```
gradle build
```

_Si todavía no se levantó la base de datos dockerizada, levantarla(ver prerequisitos para la creación de la base de datos)_

```
sudo docker start mssql
```

_Migrar la base de datos con flyway_

```
gradle flywayClean flywayMigrate -DflywayDbName=FormulariosDigitales -DflywayServer=localhost -DflywayServerPort=1433 -DflywayDbPassword=Password0401 -DflywayDbUser=sa
```

_Por ultimo, puede levantar la instancia tomcat con el siguiente comando parado en la carpeta del proyecto_

```
gradle bootRun
```

## URLS del proyecto ✏️

---

**Logs de Kibana**

- Desarrollo: http://kibana.k8sds.gscorp.ad/
- Testing: http://kibana.k8stst.gscorp.ad/
- Producción:

**Swagger**

- Desarrollo: http://api-documental.k8sds.gscorp.ad/swagger-ui.html
- Testing: http://api-documental.k8stst.gscorp.ad/swagger-ui.html
- Producción:

**SonarQube:**

- Desarrollo: http://10.241.164.132:9001/dashboard?id=snapshot.ar.com.supervielle%3Aapi-documental-develop

**Jenkins:**
http://jenkinsspv:8085/job/api-documental/



## Diagrama de Arquitectura 🖇️

![[api-documental]diagrama-arquitectura](docs/[api-documental]diagrama-arquitectura.jpg)

## Ejecutando las pruebas ⚙️

---

_Para ejecutar las pruebas unitarias y de integración, utilizar el siguiente comando_

```
gradle test
```

_Para ejecutar las pruebas de aceptación, integración y unitarias, utilizar el siguiente comando_

```
gradle verify
```

## Construido con 🛠️

---

_Herramientas utilizadas en el proyecto_

- [Flask](https://github.com/sronmiz/flask-sqlite-form) - Flask
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) - WTForms





### Prerequisites
* Flask
* WTForms
### Downloading
```
git clone https://github.com/sronmiz/flask-sqlite-form.git
```
### Running
```
cd flask-sqlite-form
export FLASK_APP=form.py
flask run
```
