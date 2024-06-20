---
title: Empezando
type: docs
weight: 5
url: /es/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "configurar Aspose.Cells para Node.js via Java y pautas de instalación."
---

## **Requisitos del sistema**
Aspose.Cells para Node.js via Java es una API independiente de la plataforma y se puede usar en cualquier plataforma (Windows, Linux y MacOS) donde se hayan instalado [Node.js](https://nodejs.org/en/download/) y el puente [node-java](https://github.com/joeferner/node-java). La máquina debe tener Oracle JDK 7 o versiones superiores antes de configurar la instalación.
## **Instalar desde NPM**
Puede usar fácilmente Aspose.Cells para Node.js via Java desde [NPM](https://www.npmjs.com/package/aspose.cells) con el siguiente comando.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

Si encuentra algún problema durante el proceso de instalación, consulte https://www.npmjs.com/package/java.

## **Instalar desde archivo ZIP**
Para instalar y usar Aspose.Cells para Node.js via Java desde un archivo ZIP, siga las siguientes instrucciones:
### **Linux:**
- Descargue e instale [Node.js](https://nodejs.org/en/download/).
- Instale Oracle JDK (1.7 o 1.8) para Linux, configure la variable de entorno JAVA_HOME.
- Instale python 2.x
- Instala el puente [node-java](https://github.com/joeferner/node-java). Puedes ejecutar los siguientes comandos @ terminal: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Descargue "Aspose.Cells para Node.js via Java" y extráigalo en "aspose.cells.js.java/node_modules".
- Crea un archivo de prueba llamado **hello.js** usando el siguiente código de ejemplo en la carpeta "aspose.cells.js.java":

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ahora ejecuta "node hello.js" en el símbolo del sistema para ejecutarlo.
### **Windows:**
- Instala Oracle JDK8 y configura la variable de entorno JAVA_HOME.
- Instala Node.js y agrega node.exe a la variable de entorno PATH.
- Instala node-gyp.
- Instala Windows Build Tools.
- Instala el puente [node-java](https://www.npmjs.com/package/java) y ejecuta los siguientes comandos en el símbolo del sistema como administrador:



{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Descargue "Aspose.Cells para Node.js via Java" y extráigalo en "aspose.cells.js.java/node_modules".
- Crea un archivo llamado **hello.js** en la carpeta "aspose.cells.js.java" usando el siguiente código de ejemplo:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ahora ejecuta "node hello.js" en el símbolo del sistema para ejecutarlo.
### **Mac:**
- Descarga e instala Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Instala Oracle JDK 1.8 (recomendado) para Mac, configura la variable de entorno JAVA_HOME.
- Modify <key>Capacidades de JVM</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0_152.jdk" depends on your jdk version), make it looks like following:



{{< highlight java >}}

 <key>JavaVM</key>

        <dict>

                <key>JVMCapabilities</key>

                <array>

                        <string>JNI</string>

                        <string>BundledApp</string>

                        <string>CommandLine</string>

                </array>

{{< /highlight >}}



- Instala Python 2.x (si no está instalado).
- Instala el puente node-java. Puedes ejecutar los siguientes comandos @ terminal:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- Descargue "Aspose.Cells para Node.js via Java" y extráigalo en "aspose.cells.js.java/node_modules".
- Cree un archivo de prueba llamado **hello.js** usando el siguiente código de ejemplo en la carpeta "aspose.cells.js.java":



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ahora ejecute "node hello.js" en el símbolo del sistema para ejecutarlo.

