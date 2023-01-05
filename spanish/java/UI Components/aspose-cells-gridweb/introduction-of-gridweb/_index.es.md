---
title: Introducción de GridWeb
type: docs
weight: 10
url: /es/java/introduction-of-gridweb/
---
## **Cómo ejecutar Aspose.Cells para GridWeb Java Demostraciones**
{{% alert color="primary" %}} 

 Aspose.Cells para GridWeb Java Las demostraciones son fáciles de ejecutar. Solo necesitas implementar**gridwebdemo.war** en su servidor web. Descargue las demostraciones de este[Enlace](https://forum.aspose.com/uploads/discourse_instance3/22292).

Este artículo describe cómo ejecutar Aspose.Cells para GridWeb Java Demos en Apache Tomcat Server.

{{% /alert %}} 
### **Guía paso a paso para ejecutar demostraciones de GridWeb Java**
1.  Extracto**apache-tomcat-7.0.52.zip** en cualquier directorio, por ejemplo, C:\Tomcat

![todo:imagen_alternativa_texto](introduction-of-gridweb_1.png)



 La siguiente instantánea muestra los directorios y archivos extraídos del servidor Apache Tomcat

![todo:imagen_alternativa_texto](introduction-of-gridweb_2.png)



 Es posible que también deba configurar la variable de entorno**CATALINA_HOME** 

![todo:imagen_alternativa_texto](introduction-of-gridweb_3.png)

1. Abre el**tomcat-usuarios.xml** expediente.

![todo:imagen_alternativa_texto](introduction-of-gridweb_4.png)

1. Agregar este usuario:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Aquí el nombre de usuario es tomcat y la contraseña es secreta** 

![todo:imagen_alternativa_texto](introduction-of-gridweb_5.png)

1.  ejecutar el**inicio.bat** expediente.
 Ejecutará el servidor Apache Tomcat.

![todo:imagen_alternativa_texto](introduction-of-gridweb_6.png)



**Servidor Tomcat ejecutándose en una ventana de comandos** 

![todo:imagen_alternativa_texto](introduction-of-gridweb_7.png)

1.  Ahora abra el navegador y escriba**servidor local: 8080**.
 Se muestra la página web de Apache Tomcat.

   **La página web de Apache Tomcat** 

![todo:imagen_alternativa_texto](introduction-of-gridweb_8.png)

1.  Hacer clic**Aplicación de administrador** y escriba el nombre de usuario y la contraseña. (Como arriba: gato, secreto)

![todo:imagen_alternativa_texto](introduction-of-gridweb_9.png)

1.  Desplácese hacia abajo hasta la sección**Archivo WAR para implementar** y navega por el**gridwebdemo.war** expediente.
1.  Hacer clic**Desplegar**. 

![todo:imagen_alternativa_texto](introduction-of-gridweb_10.png)

1.  Navegar**gridwebdemo.war** expediente.

![todo:imagen_alternativa_texto](introduction-of-gridweb_11.png)

1.  Hacer clic**Desplegar**. 

![todo:imagen_alternativa_texto](introduction-of-gridweb_12.png)

1.  Una vez implementado, haga clic en**/gridwebdemo** y comience a ejecutar demostraciones.

![todo:imagen_alternativa_texto](introduction-of-gridweb_13.png)


 Se muestra la página de demostración de GridWeb.

**La página de demostración de GridWeb** 

![todo:imagen_alternativa_texto](introduction-of-gridweb_14.png)

1.  Haga clic en cualquier demostración y ejecútela.

   **Creación de demostración de contenido en ejecución** 

![todo:imagen_alternativa_texto](introduction-of-gridweb_15.png)



**Demostración de hojas de trabajo en ejecución** 

![todo:imagen_alternativa_texto](introduction-of-gridweb_16.png)



**Demostración de HeaderBar y CommandButton en ejecución** 

![todo:imagen_alternativa_texto](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb - Demostraciones**
{{% alert color="primary" %}} 

Para ponerlo en funcionamiento rápidamente, proporcionamos una serie de ejemplos de código y demostraciones que muestran cómo usar Aspose.Cells.GridWeb API.

Descargue las demostraciones desde el siguiente enlace:
[Aspose.Cells. Demostraciones GridWeb](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **Capacidades de los navegadores y Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb es un control web basado en GUI que se puede incrustar en páginas web JSP como otros controles web. Lo más importante del control web es brindar compatibilidad entre navegadores. Aspose.Cells.GridWeb proporciona soporte para varios navegadores.
### **Comparación**
Aspose.Cells.GridWeb es totalmente compatible con Internet Explorer (IE) de Microsoft. Sin embargo, en otros navegadores tiene limitaciones menores. Este tema proporciona una comparación detallada de qué características son compatibles con diferentes navegadores.

|**Características del lado del cliente**|**Microsoft Internet Explorer**|**Google cromo**|**Mozilla Firefox**|**Ópera**|
|:- |:- |:- |:- |:- |
|Menú contextual de Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Validación del lado del cliente|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Evento de doble clic|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| La lista desplegable (*Modo de cuadro combinado* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| La lista desplegable (*Modo de menú emergente* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Entrada/edición de fórmula|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Congelar o descongelar filas/columnas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| hipervínculos (*Modo de comando de celda* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| hipervínculos (*Modo URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Combinar o separar Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Múltiple Cells Copiar/Pegar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Múltiple Cells Entrada/Editar, Postback único|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formato numérico|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Paginación de hoja|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Solo lectura Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Filas/columnas de solo lectura|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Validación de datos usando expresiones regulares|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cambiar el tamaño del ancho de la columna|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cambiar el tamaño de la altura de la fila|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Insertar/eliminar filas y columnas|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Contenido de desplazamiento|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Pestañas de hoja de desplazamiento|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Establecer bordes de Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Establecer configuración de fuente de Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} El menú contextual de una celda solo se puede activar haciendo clic en el botón del menú del lado del cliente.
