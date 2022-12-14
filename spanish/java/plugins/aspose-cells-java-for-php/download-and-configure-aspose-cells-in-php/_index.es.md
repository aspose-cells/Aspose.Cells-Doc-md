---
title: Descargar y Configurar Aspose.Cells en PHP
type: docs
weight: 10
url: /es/java/download-and-configure-aspose-cells-in-php/
---
## **Descargar bibliotecas requeridas**
Descargue las bibliotecas necesarias que se mencionan a continuación. Estos son los necesarios para ejecutar Aspose.Cells Java para ejemplos de PHP.

- **Aspose:** [Aspose.Cells for Java Componente](https://downloads.aspose.com/cells/java/)
- [PHP/Java Puente](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Descargar ejemplos de sitios de codificación social**
Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

-----
### **GitHub**
- **Aspose.Cells Java para ejemplos de PHP** 
  - [Aspose.Cells Java para PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Cómo configurar el código fuente en la plataforma Linux**
Siga estos sencillos pasos para abrir y ampliar el código fuente mientras usa:
## **1. Instalar el servidor Tomcat**
 Para instalar el servidor Tomcat, emita el siguiente comando en la consola de Linux. Esto instalará con éxito el servidor Tomcat.

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Descarga y configura PHP/JavaBridge**
 Para descargar los binarios de PHP/JavaBridge, emita el siguiente comando en la consola de Linux.

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


 Descomprima los archivos binarios de PHP/JavaBridge emitiendo el siguiente comando en la consola de Linux.

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Esto extraerá**JavaBridge.war**expediente. Cópialo en tomcat88**aplicaciones web** carpeta emitiendo el siguiente comando en la consola de Linux.

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


Al copiar, tomcat8 creará automáticamente una nueva carpeta "**JavaPuente**" en**aplicaciones web**. Una vez que se crea la carpeta, asegúrese de que su tomcat8 se esté ejecutando y luego verifique<http://localhost:8080/JavaBridge>en el navegador, debería abrir una página predeterminada de JavaBridge.

 Si aparece algún mensaje de error, instale**CGI rápido**emitiendo el siguiente comando en la consola de Linux.

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

Después de instalar php5.5 cgi, reinicie el servidor tomcat8 y verifique<http://localhost:8080/JavaBridge>de nuevo en el navegador.

Si**JAVA_HOME**se muestra el error, luego abra el archivo /etc/default/tomcat8 y elimine el comentario de la línea que configura JAVA_HOME. Verifique <http://localhost:8080/JavaBridge> en el navegador nuevamente, debería venir con la página de Ejemplos de PHP/JavaBridge.
## **3. Configure Aspose.Cells Java para ejemplos de PHP**
 Clone, ejemplos de PHP emitiendo los siguientes comandos dentro de la carpeta webapps/JavaBridge.

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **Cómo configurar el código fuente en la plataforma Windows**
Siga los sencillos pasos a continuación para configurar el puente PHP/Java en la plataforma Windows

\1. Instala PHP5 y configura como lo haces normalmente
\2. Instale JRE 6 (Java Runtime Environment) si aún no lo tiene. Puede verificar esto en C:\Archivos de programa, etc. Puede descargarlo aquí. Estoy usando JRE 6 porque es compatible con PHP Java Bridge (PJB).

\3. Instale Apache Tomcat 8.0. Puedes descargarlo aquí

 4.Descargar[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copie este archivo en el directorio de aplicaciones web de tomcat.
(por ejemplo: C:\Archivos de programa\Apache Software Foundation\Tomcat 8.0\webapps)

\5. Reinicie el servicio apache de tomcat.

 6.Ir a<http://localhost:8080/JavaBridge/test.php> para comprobar si php funciona. Puedes encontrar otros ejemplos allí.

7.Copie su archivo jar Aspose.Cells Java en C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

 \8. Clon[Aspose.Cells Java para PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) ejemplos dentro de la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

\8. Copie la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a su Aspose.Cells Java para la carpeta de ejemplos de PHP.

 \10. Reinicie el servicio apache tomcat y comience a usar ejemplos.
