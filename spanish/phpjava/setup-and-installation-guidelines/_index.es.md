---
title: Directrices de configuración e instalación
type: docs
weight: 20
url: /es/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: configuración Aspose.Cells for PHP via Java y pautas de instalación
---
## **Requisitos del sistema**
Aspose.Cells for PHP via Java es independiente de la plataforma API y se puede usar en cualquier plataforma (Windows, Linux, MacOS, etc.) donde[PHP](https://www.php.net/downloads.php)7 o versiones superiores están instaladas. La máquina debe tener Oracle JDK 7 o versiones superiores antes de configurar la instalación.
## **Instalación y uso**
Aspose.Cells for PHP via Java se distribuye como un archivo ZIP.

Para configurar el entorno, instalar y usar Aspose.Cells for PHP via Java, siga las instrucciones:
### **Linux:**
- Descargar[PHP](https://www.php.net/downloads.php)fuente e instalarlo. O use el comando “sudo apt install php-xxx” para instalar el binario php.
- Instale Oracle JDK (1.7 o 1.8) para Linux, configure la variable de entorno JAVA_HOME.
- Descargue/Obtenga "Aspose.Cells for PHP via Java" API y extráigalo. Habrá una carpeta llamada "aspose.cells".
- Descargue PHP/Java Bridge binary (JavaBridge.jar) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdelo en la carpeta "aspose.cells".
- Descargue la biblioteca PHP java/Java.inc (Java.inc) de http://php-java-bridge.sourceforge.net/pjb/download.php y guárdela en la carpeta "aspose.cells".
- Ejecute "PHP/Java Bridge" en la carpeta anterior con el siguiente comando.

|$ JAVA_INICIO/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
|:- |
- Ejecute "example.php" en la carpeta "aspose.cells" para ejecutar el ejemplo con el siguiente comando:

|$ php ejemplo.php|
|:- |
### **Windows:**
- Descargar[PHP](https://www.php.net/downloads.php)binario de Windows y agregue "php.exe" a PATH.
- Instale Oracle JDK (1.7 o 1.8) para Windows y configure la variable de entorno JAVA_HOME.
- Descargue "Aspose.Cells for PHP via Java" API y extráigalo. Habrá una carpeta llamada "aspose.cells".
- Descargue PHP/Java Bridge binary (JavaBridge.jar) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdelo en la carpeta "aspose.cells".
- Descargue la biblioteca PHP java/Java.inc (Java.inc) de http://php-java-bridge.sourceforge.net/pjb/download.php y guárdela en la carpeta "aspose.cells".
- Ejecute "PHP/Java Bridge" en la carpeta anterior con el siguiente comando. Seleccione el puerto de escucha HTTP 8080 cuando se inició el puente y haga clic en el botón Aceptar.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Ejecute "example.php" en la carpeta "aspose.cells" para ejecutar el ejemplo con el siguiente comando:

|> php ejemplo.php|
|:- |
### **Mac:**
- Instalar[PHP](https://www.php.net/downloads.php).
- Instale Oracle JDK (1.7 o 1.8) para Mac, configure la variable de entorno JAVA_HOME.
- Descargue "Aspose.Cells for PHP via Java" API y extráigalo. Habrá una carpeta llamada "aspose.cells".
- Descargue PHP/Java Bridge binary (JavaBridge.jar) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdelo en la carpeta "aspose.cells".
- Descargue la biblioteca PHP java/Java.inc (Java.inc) de http://php-java-bridge.sourceforge.net/pjb/download.php y guárdela en la carpeta "aspose.cells".
- Ejecute "PHP/Java Bridge" en la carpeta anterior con el siguiente comando. Seleccione el puerto de escucha HTTP 8080 cuando se inició el puente y haga clic en el botón Aceptar.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Ejecute "example.php" en la carpeta "aspose.cells" para ejecutar el ejemplo con el siguiente comando:

|$ php ejemplo.php|
|:- |


