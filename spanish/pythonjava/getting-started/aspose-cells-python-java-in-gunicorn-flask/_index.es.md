---
title: Cómo usar Aspose.Cells para Python via Java en entorno Gunicorn+Flask
type: docs
weight: 40
url: /es/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: Esta sección compara los componentes de Aspose.Cells para Python via Java y algunas otras bibliotecas de operaciones de Excel en Python.
keywords: Python Excel, Excel Python, Excel Python via Java, Python via Java Excel, ¿Por qué Aspose.Cells para Python via Java, ¿Por qué no xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas.
---

{{% alert color="primary" %}}

Este tema para principiantes muestra cómo los desarrolladores pueden crear una aplicación sencilla (Hola Mundo) usando Aspose.Cells para Python via Java. La aplicación crea un archivo de Microsoft Excel con las palabras Hola Mundo en una celda específica de una hoja de cálculo.

{{% /alert %}}



## **Preparación completa del entorno**

El entorno de ejecución de ejemplo de esta guía es Ubuntu: 20.04, puedes ajustarlo según tu situación real. Para garantizar que los ejemplos funcionen correctamente, necesitamos instalar algunas herramientas necesarias en el entorno. A continuación se presenta una breve guía paso a paso para ayudarte a completar el proceso. Ten en cuenta que esto es solo una guía aproximada y los detalles específicos pueden variar según tu sistema y necesidades.

### Python

Si no está instalado, instálalo de la siguiente manera:
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
Verificar versión
```
python3 --version
pip3 --version
```

### Java
Si no está instalado, instálalo de la siguiente manera:
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
Verificar versión
```
java -version
```

### entorno virtualenv
El entorno virtual se instala según tus necesidades reales. Se recomienda usar entornos virtuales para gestionar las dependencias del proyecto en entornos de desarrollo y producción.
Por favor, sigue el siguiente comando para instalar:
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
Crear un entorno virtual
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
Iniciar el entorno virtual
```
source myenv/bin/activate
```

***Aviso: si se usa un entorno virtual, las siguientes operaciones requieren que actives primero el entorno virtual correspondiente***

### Flask
Si no está instalado, por favor siga el siguiente comando para instalar:
```
pip install Flask
```

### Gunicorn
Si no está instalado, por favor siga el siguiente comando para instalar:
```
pip install gunicorn
```

### Jpype
Si no está instalado, por favor siga el siguiente comando para instalar:
```
pip install jpype1
```

### aspose-cells
Si no está instalado, por favor siga el siguiente comando para instalar:
```
pip install aspose-cells
```

## **Creación de la aplicación Hola Mundo**

Para crear la aplicación Hola Mundo utilizando la API de Aspose.Cells:

1. Cree una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook).
1. Aplique la licencia:
   1. Si has comprado una licencia, entonces úsala en tu aplicación para acceder a la funcionalidad completa de Aspose.Cells.
   1. Si estás usando la versión de evaluación del componente (si estás usando Aspose.Cells sin una licencia), omite este paso.
1. Crear un nuevo archivo de Microsoft Excel o abrir un archivo existente en el cual quieras agregar/actualizar algún texto.
1. Acceder a cualquier celda de una hoja de cálculo en el archivo de Microsoft Excel.
1. Inserte las palabras **¡Hola, mundo!** en una celda accesada.
1. Genere el archivo modificado de Microsoft Excel.

Los ejemplos a continuación demuestran los pasos anteriores.

### **Creando un Libro de trabajo**

El siguiente ejemplo crea un nuevo libro de trabajo desde cero, escribe las palabras "¡Hola, mundo!" en la celda A1 en la primera hoja de trabajo, y guarda el archivo.

Supongamos que tenemos una ruta de prueba "/app". Realizaremos el siguiente trabajo bajo esta ruta de prueba.

#### Archivos de la aplicación Flask: hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### Archivo de clase de inicio personalizado de Gunicorn: custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### Iniciar el servicio

Verifique que todos los paquetes necesarios por el servicio estén instalados, luego inicie el servicio.

Si usa el entorno virtual python3-venv, necesita crear un entorno virtual en la ruta de prueba, iniciarlo y luego instalar todos los paquetes necesarios.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### Ver resultados

1. Abra el navegador y visite http://127.0.0.1:5000/.

2. Ingrese el nombre del archivo que desea guardar en el cuadro de entrada.

3. Haga clic en el botón 'Generar' para guardar el archivo.

Después de hacer esto, obtendrá un archivo Excel llamado con el contenido ingresado en la ruta de prueba actual. La vista previa es la siguiente:

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Usando Docker

O puede poner las operaciones anteriores en un contenedor Docker. Es muy simple usar Docker para construir el entorno utilizado por el ejemplo. Solo coloque las operaciones anteriores en el archivo Dockerfile.

Aquí hay un archivo Dockerfile para referencia. Enumera algunos kits de herramientas necesarios para construir el entorno.

### Dockerfile

``` 
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    openjdk-11-jdk \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "custom_gunicorn.py"]
```

### requirements.txt

Este archivo se utiliza principalmente para proporcionar un entorno de dependencias para proyectos de Python. Puede modificar la versión en este archivo según sus necesidades.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### Archivos principales

La estructura principal de archivos es la siguiente:
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### Iniciar el contenedor

Puede iniciar el contenedor usando el siguiente comando
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
