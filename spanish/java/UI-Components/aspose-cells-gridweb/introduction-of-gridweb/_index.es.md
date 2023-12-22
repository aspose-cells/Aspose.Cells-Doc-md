---
title: Introducción de GridWeb
type: docs
weight: 10
url: /es/java/introduction-of-gridweb/
---
##  **Conceptos básicos de GridWeb**
 Aspose.Cells.GridWeb es un control web basado en GUI que se puede incrustar en páginas web JSP o en cualquier página html en un servidor Java.
{{% alert color="primary" %}} 

Es fácil y simple de usar.

Le ayuda a crear rápidamente un editor web en línea para archivos de hojas de cálculo.

También admite la importación y exportación de todo tipo de archivos en formato de hoja de cálculo, que es 100% compatible con archivos MS Excel.

##  **Aspose.Cells.GridWeb - Demostraciones**
{{% alert color="primary" %}} 

Para que pueda empezar a utilizarlo rápidamente, le proporcionamos una serie de ejemplos de código y demostraciones que muestran cómo utilizar Aspose.Cells.GridWeb API.

Descargue las demostraciones desde el siguiente enlace:
[Aspose.Cells.Demostraciones de GridWeb](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


##  **Cómo ejecutar Aspose.Cells para demostraciones de GridWeb Java**
{{% alert color="primary" %}} 

 Aspose.Cells para las demostraciones de GridWeb Java son fáciles de ejecutar. Sólo necesitas implementar**gridwebdemo.guerra** en su servidor web. Descargue las demostraciones de este[enlace](https://forum.aspose.com/uploads/discourse_instance3/22292).

Este artículo describe cómo ejecutar Aspose.Cells para demostraciones de GridWeb Java en el servidor Apache Tomcat.

{{% /alert %}} 
###  **Guía paso a paso para ejecutar demostraciones de GridWeb Java**
1.  Extracto**apache-tomcat-7.0.52.zip** en cualquier directorio, por ejemplo C:\Tomcat

![todo:image_alt_text](introduction-of-gridweb_1.png)



 La siguiente instantánea muestra los directorios y archivos extraídos del servidor Apache Tomcat.

![todo:image_alt_text](introduction-of-gridweb_2.png)



 Es posible que también necesites configurar la variable de entorno.**CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1.  Abre el**usuarios de tomcat.xml** archivo.

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Añade este usuario:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Aquí el nombre de usuario es tomcat y la contraseña es secreta** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1.  Ejecute el**inicio.bat** archivo.
 Ejecutará el servidor Apache Tomcat.

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Servidor Tomcat ejecutándose en una ventana de comandos** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Ahora abra el navegador y escriba *localhost:8080**.
 Se muestra la página web de Apache Tomcat.

   **La página web de Apache Tomcat** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1.  Hacer clic**Aplicación de administrador** y escriba el nombre de usuario y la contraseña. (Como arriba: tomcat, secreto)

![todo:image_alt_text](introduction-of-gridweb_9.png)

1.  Desplázate hacia abajo hasta la sección**Archivo WAR para implementar** y navegar por el**gridwebdemo.guerra** archivo.
1.  Haga clic en *Implementar**.

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. Navegar**gridwebdemo.guerra** archivo.

![todo:image_alt_text](introduction-of-gridweb_11.png)

1.  Haga clic en *Implementar**.

![todo:image_alt_text](introduction-of-gridweb_12.png)

1.  Una vez implementado, haga clic en**/gridwebdemo** y comenzar a ejecutar demostraciones.

![todo:image_alt_text](introduction-of-gridweb_13.png)


 Se muestra la página de demostración de GridWeb.

**La página de demostración de GridWeb** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1.  Haga clic en cualquier demostración y ejecútela.

   **Creando contenido demo ejecutándose** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Demostración de hojas de trabajo en ejecución** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**Demostración de HeaderBar y CommandButton en ejecución** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
##  **Capacidades de los navegadores y Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb es un control web basado en GUI que se puede incrustar en páginas web JSP como otros controles web. Lo más importante del control web es brindar soporte para varios navegadores. Aspose.Cells.GridWeb proporciona soporte para varios navegadores.
###  **Comparación**
Aspose.Cells.GridWeb es totalmente compatible con Internet Explorer (IE) de Microsoft. Sin embargo, en otros navegadores tiene limitaciones menores. Este tema proporciona una comparación detallada de qué funciones son compatibles con diferentes navegadores.

|**Funciones del lado del cliente**|**Microsoft Internet Explorer**|**Google Cromo**|**Mozilla Firefox**|**Ópera**|
| :- | :- | :- | :- | :- |
|Menú contextual de Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Validación del lado del cliente|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Evento de doble clic|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| La lista desplegable (*Modo cuadro combinado* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| La lista desplegable (*Modo de menú emergente* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Entrada/edición de fórmula|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Congelar o descongelar filas/columnas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Hipervínculos (*Modo de comando celular* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Hipervínculos (*Modo URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Fusionar o separar Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Múltiple Cells Copiar/Pegar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Entrada/edición múltiple Cells, devolución de datos única|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formato numérico|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Paginación de hojas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sólo lectura Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Filas/columnas de solo lectura|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Validación de datos mediante expresiones regulares|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cambiar el tamaño del ancho de la columna|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cambiar el tamaño de la altura de la fila|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Insertar/eliminar filas y columnas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Desplazar contenido|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Pestañas de hoja de desplazamiento|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Establecer bordes de Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Establecer la configuración de fuente de Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} El menú contextual de una celda solo se puede activar haciendo clic en el botón de menú del lado del Cliente.
