---
title: Guías de instalación y configuración
type: docs
weight: 20
url: /es/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "configurar Aspose.Cells para PHP via Java y directrices de instalación."
---



## **Requisitos del sistema**
Aspose.Cells para PHP via Java es una API independiente de la plataforma y se puede utilizar en cualquier plataforma (Windows, Linux, MacOS, etc.) donde se haya instalado [PHP](https://www.php.net/downloads.php) versión 7 o superior. La máquina debe tener Oracle JDK 7 o versiones superiores antes de configurar la instalación.
## **Instalación y Uso**
Aspose.Cells para PHP via Java se distribuye como un archivo ZIP.

Para configurar el entorno, instalar y usar Aspose.Cells para PHP via Java, siga las instrucciones:
### **Linux:**
- Descargue el origen de [PHP](https://www.php.net/downloads.php) e instálelo. O use el comando “sudo apt install php-xxx” para instalar el binario de PHP.
- Instale Oracle JDK (1.7 o 1.8) para Linux, configure la variable de entorno JAVA_HOME.
- Descargue/Obtenga la API "Aspose.Cells para PHP via Java" y extráigala. Habrá una carpeta llamada "aspose.cells".
- Descarga el archivo binario del Puente PHP/Java (JavaBridge.jar) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdalo en la carpeta "aspose.cells".
- Descarga la biblioteca PHP de java/Java.inc (Java.inc) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdala en la carpeta "aspose.cells".
- Ejecute el “Puente PHP/Java” en la carpeta anterior con el siguiente comando.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- Ejecuta "example.php" en la carpeta “aspose.cells” para ejecutar el ejemplo con el siguiente comando:

|$ php example.php|
| :- |
### **Windows:**
- Descargue el binario de PHP para Windows desde (https://www.php.net/downloads.php) y agregue "php.exe" al PATH.
- Instale Oracle JDK (1.7 o 1.8) para Windows y configure la variable de entorno JAVA_HOME.
- Descargue la API "Aspose.Cells for PHP via Java" y extráigala. Habrá una carpeta llamada "aspose.cells".
- Descarga el archivo binario del Puente PHP/Java (JavaBridge.jar) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdalo en la carpeta "aspose.cells".
- Descarga la biblioteca PHP de java/Java.inc (Java.inc) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdala en la carpeta "aspose.cells".
- Ejecuta “PHP/Java Bridge” en la carpeta anterior con el siguiente comando. Selecciona el puerto del listener http 8080 cuando se inicie el puente y haz clic en el botón OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Ejecuta "example.php" en la carpeta “aspose.cells” para ejecutar el ejemplo con el siguiente comando:

|> php example.php|
| :- |
### **Mac:**
- Instale [PHP](https://www.php.net/downloads.php).
- Instale Oracle JDK (1.7 o 1.8) para Mac, configure la variable de entorno JAVA_HOME.
- Descargue la API "Aspose.Cells for PHP via Java" y extráigala. Habrá una carpeta llamada "aspose.cells".
- Descarga el archivo binario del Puente PHP/Java (JavaBridge.jar) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdalo en la carpeta "aspose.cells".
- Descarga la biblioteca PHP de java/Java.inc (Java.inc) desde http://php-java-bridge.sourceforge.net/pjb/download.php y guárdala en la carpeta "aspose.cells".
- Ejecuta “PHP/Java Bridge” en la carpeta anterior con el siguiente comando. Selecciona el puerto del listener http 8080 cuando se inicie el puente y haz clic en el botón OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Ejecuta "example.php" en la carpeta “aspose.cells” para ejecutar el ejemplo con el siguiente comando:

|$ php example.php|
| :- |


