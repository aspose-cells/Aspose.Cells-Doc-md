---
title: Descargar y Configurar Aspose.Cells en PHP
type: docs
weight: 10
url: /es/java/download-and-configure-aspose-cells-in-php/
---

## **Descargar Bibliotecas Requeridas**
Descargar las bibliotecas requeridas mencionadas a continuación. Estas son necesarias para ejecutar ejemplos de Aspose.Cells Java para PHP.

- **Aspose:** [Aspose.Cells for Java Componente](https://downloads.aspose.com/cells/java/)
- [Puente PHP/Java](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Descargar Ejemplos de Sitios de Codificación Social**
Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

-----
### **GitHub**
- **Ejemplos de Aspose.Cells Java para PHP** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Cómo configurar el código fuente en la plataforma Linux**
Por favor, siga estos sencillos pasos para abrir y extender el código fuente al usar:
## **1. Instalar el servidor Tomcat**
Para instalar el servidor Tomcat, emita el siguiente comando en la consola de Linux. Esto instalará correctamente el servidor Tomcat. 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Descargar y configurar PHP/JavaBridge**
Para descargar los binarios de PHP/JavaBridge, emita el siguiente comando en la consola de Linux. 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Descomprima los binarios de PHP/JavaBridge emitiendo el siguiente comando en la consola de Linux. 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Esto extraerá el archivo **JavaBridge.war**. Copie a la carpeta **webapps** de **tomcat8** emitiendo el siguiente comando en la consola de Linux. 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

Si aparece algún mensaje de error, instale **FastCGI** emitiendo el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. Configurar los ejemplos de Aspose.Cells Java para PHP**
Clonar ejemplos de PHP emitiendo los siguientes comandos dentro de la carpeta webapps/JavaBridge.  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **Cómo configurar el código fuente en la Plataforma Windows**
Siga los siguientes sencillos pasos para configurar PHP/Java Bridge en la plataforma Windows

\1. Instalar PHP5 y configurar como lo hace normalmente
\ 2. Instale JRE 6 (Entorno de ejecución de Java) si aún no lo tiene. Puede verificar esto en C: \ Archivos de programa, etc. Puede descargarlo aquí. Estoy usando JRE 6 ya que es compatible con PHP Java Bridge (PJB).

\ 3. Instale Apache Tomcat 8.0. Puede descargarlo aquí

4. Descargue [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copie este archivo en el directorio webapps de tomcat.
(ej: C: \ Archivos de programa \ Apache Software Foundation \ Tomcat 8.0 \ webapps)

\ 5. Reinicie el servicio de apache tomcat.

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. Copiar tu archivo jar de Aspose.Cells Java en C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

\ 8. Clone los ejemplos de [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) dentro de la carpeta C: \ Archivos de programa \ Apache Software Foundation \ Tomcat 8.0 \ webapps \

\ 8. Copie la carpeta C: \ Archivos de programa \ Apache Software Foundation \ Tomcat 8.0 \ webapps \ JavaBridge \ java a su carpeta de ejemplos de Aspose.Cells Java para PHP.

\ 10. Reinicie el servicio de apache tomcat y comience a usar los ejemplos. 
