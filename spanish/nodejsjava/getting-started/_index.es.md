---
title: Empezando
type: docs
weight: 5
url: /es/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: configuración Aspose.Cells for Node.js via Java y pautas de instalación
---
## **Requisitos del sistema**
 Aspose.Cells for Node.js via Java es independiente de la plataforma API y se puede usar en cualquier plataforma (Windows, Linux y MacOS) donde[Nodo.js](https://nodejs.org/en/download/) y[nodo-java](https://github.com/joeferner/node-java) puente están instalados. La máquina debe tener Oracle JDK 7 o versiones superiores antes de configurar la instalación.
## **Instalar desde NPM**
 Puede usar fácilmente Aspose.Cells for Node.js via Java desde[MNP](https://www.npmjs.com/package/aspose.cells) con el siguiente comando.
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

Si encuentra algún problema durante el proceso de instalación, consulte https://www.npmjs.com/package/java.

## **Instalar desde archivo ZIP**
Para instalar y usar Aspose.Cells for Node.js via Java desde un archivo ZIP, siga las siguientes instrucciones:
### **Linux:**
-  Descargar e instalar[Nodo.js](https://nodejs.org/en/download/).
- Instale Oracle JDK (1.7 o 1.8) para Linux, configure la variable de entorno JAVA_HOME.
- Instalar python 2.x
-  Instalar[nodo-java](https://github.com/joeferner/node-java) puente. Puede ejecutar los siguientes comandos @ terminal:



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Descargue "Aspose.Cells for Node.js via Java" y extráigalo en "aspose.cells.js.java/node_modules".
- Cree un archivo de prueba llamado**hola.js**usando el siguiente código de muestra en la carpeta "aspose.cells.js.java":

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ahora ejecute "node hello.js" @ símbolo del sistema para ejecutarlo.
### **Windows:**
- Instale Oracle JDK8 y configure la variable de entorno JAVA_HOME.
- Instale Node.js y agregue node.exe a PATH.
- Instale el nodo-gyp.
- Instale las herramientas de compilación Windows.
-  Instalar[puente nodo-java](https://www.npmjs.com/package/java) y ejecute los siguientes comandos @ símbolo del sistema como administrador:



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Descargue "Aspose.Cells for Node.js via Java" y extráigalo en "aspose.cells.js.java/node_modules".
-  Crear un archivo llamado**hola.js**en la carpeta "aspose.cells.js.java" usando el siguiente código de muestra:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ahora ejecute "node hello.js" @ símbolo del sistema para ejecutarlo.
### **Mac:**
- Descargue e instale Node.js ([*https://nodejs.org/en/descargar/*](https://nodejs.org/en/download/))
- Instale Oracle JDK 1.8 (recomendado) para Mac, configure la variable de entorno JAVA_HOME.
-  Modificar<key>Capacidades de JVM</key> sección en "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" con privilegio de raíz. ("jdk1.8.0_152.jdk" depende de su versión de jdk), haga que tenga el siguiente aspecto:



{{< highlight "java" >}}

 <key>JavaVM</key>

        <dict>

                <key>JVMCapabilities</key>

                <array>

                        <string>JNI</string>

                        <string>BundledApp</string>

                        <string>CommandLine</string>

                </array>

{{< /highlight >}}



- Instale Python 2.x (si no está instalado).
- Instale el puente nodo-java. Puede ejecutar los siguientes comandos @ terminal:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm instalar java

- Descargue "Aspose.Cells for Node.js via Java" y extráigalo en "aspose.cells.js.java/node_modules".
-  Cree un archivo de prueba llamado**hola.js** usando el siguiente código de muestra en la carpeta "aspose.cells.js.java":



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ahora ejecute "node hello.js" @ símbolo del sistema para ejecutarlo.

