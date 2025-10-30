---
title: Introducción de GridWeb
type: docs
weight: 10
url: /es/java/introduction-of-gridweb/
---
## **Conceptos básicos de GridWeb**
Aspose.Cells.GridWeb es un control web basado en GUI que se puede incrustar en páginas web JSP o cualquier página html en el servidor java. 

Es fácil y sencillo de usar.

Te ayuda a construir rápidamente un editor web en línea para archivos de hojas de cálculo.

También es compatible con la importación y exportación de todo tipo de archivos de hojas de cálculo que son 100% compatibles con los archivos de MS excel.

## **Aspose.Cells.GridWeb - Demos**

Para que pueda comenzar rápidamente, proporcionamos una serie de ejemplos de código y demos que muestran cómo utilizar la API de Aspose.Cells.GridWeb.

Por favor, descargue los demos desde el siguiente enlace:
[Demos de Aspose.Cells.GridWeb](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb)


## **Cómo ejecutar los demos de Aspose.Cells for GridWeb Java**
{{% alert color="primary" %}} 

Los demos de Aspose.Cells for GridWeb Java son fáciles de ejecutar. Solo necesita implementar **gridwebdemo.war** en su servidor web. Por favor, descargue los demos desde este [enlace](https://forum.aspose.com/uploads/discourse_instance3/22292).

Este artículo describe cómo ejecutar los demos de Aspose.Cells for GridWeb Java en el servidor Apache Tomcat.

{{% /alert %}} 
### **Guía paso a paso para ejecutar los demos de GridWeb Java**
1. Extraer **apache-tomcat-7.0.52.zip** en cualquier directorio, por ejemplo, C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



La siguiente captura muestra los directorios y archivos extraídos del servidor Apache Tomcat 

![todo:image_alt_text](introduction-of-gridweb_2.png)



También es posible que necesite configurar la variable de entorno **CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. Abrir el archivo **tomcat-users.xml** 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Agregar este usuario:

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**El nombre de usuario es tomcat y la contraseña es secret** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. Ejecutar el archivo **startup.bat**
   Ejecutará el servidor Apache Tomcat. 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Servidor Tomcat en ejecución en una ventana de comando** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Ahora abre el navegador y escribe **localhost:8080**.
   Se muestra la página web de Apache Tomcat. 

   **La página web de Apache Tomcat** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. Haz clic en **Manager App** y escribe nombre de usuario y contraseña. (Como arriba: tomcat, secret) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. Desplázate hacia abajo hasta la sección **Archivo WAR para implementar** y busca el archivo **gridwebdemo.war**.
1. Haz clic en **Implementar**. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. Busca el archivo **gridwebdemo.war**. 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. Haz clic en **Implementar**. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. Una vez implementado, haz clic en **/gridwebdemo** y comienza a ejecutar demos. 

![todo:image_alt_text](introduction-of-gridweb_13.png)


Se muestra la página de demostración de GridWeb. 

**La página de demostración de GridWeb** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. Haz clic en cualquier demo y ejecútalo. 

   **Demo de creación de contenidos en ejecución** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Demo de hojas de cálculo en ejecución** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**Demo de barra de encabezado y botón de comando en ejecución** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


## **Capacidades de navegadores y Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb es un control web basado en GUI que se puede incrustar en páginas web JSP como otros controles web. Lo más importante de este control web es proporcionar soporte multi-navegador. Aspose.Cells.GridWeb proporciona soporte multi-navegador.
### **Comparación**
Aspose.Cells.GridWeb es totalmente compatible con Internet Explorer (IE) de Microsoft. Sin embargo, en otros navegadores, tiene limitaciones menores. Este tema proporciona una comparación detallada de qué características son compatibles con diferentes navegadores.

|**Características del lado del cliente**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|Menú contextual de celda|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Validación del lado del cliente|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Evento de doble clic|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Lista desplegable ( *Modo de cuadro combinado* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Lista desplegable ( *Modo de menú emergente* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Entrada/edición de fórmula|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Congelar o descongelar filas/columnas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hipervínculos ( *Modo de comando de celda* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hipervínculos ( *Modo de URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Combinar o separar celdas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Copiar/pegar varias celdas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Entrada/edición de varias celdas, un solo envío de datos|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formato de número|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Páginas de hoja|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Celdas de solo lectura|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Filas/columnas de solo lectura|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Validación de datos usando expresiones regulares|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cambiar el ancho de columna|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ajustar Altura de Fila|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Insertar/Eliminar Filas y Columnas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Desplazar Contenido|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Desplazar Pestañas de Hojas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Establecer Bordes de las Celdas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Establecer Configuraciones de Fuente de las Celdas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
