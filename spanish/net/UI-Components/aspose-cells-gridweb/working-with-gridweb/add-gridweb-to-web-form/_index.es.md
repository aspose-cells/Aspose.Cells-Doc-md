---
title: Agregar GridWeb al formulario web
type: docs
weight: 10
url: /es/net/add-gridweb-to-web-form/
---
{{% alert color="primary" %}} 

Este tema proporciona una guía básica paso a paso para principiantes para ayudarlos a crear y usar el control Aspose.Cells.GridWeb en aplicaciones web.

{{% /alert %}} 
## **Creación y uso de Aspose.Cells.GridWeb Control**
### **Paso 1: crear un proyecto de aplicación web**
Primero, cree un proyecto de aplicación web en el que usar el control Aspose.Cells.GridWeb:

1. Abra Visual Studio.
1.  Desde el**Archivo** menú, seleccione**Nuevo** seguido por**Proyecto**. 

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_1.png)



Aparece un cuadro de diálogo Nuevo proyecto.

1.  Seleccione**ASP.NET Aplicación web** para el idioma deseado.

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_2.png)

1.  Seleccione**Formularios web** modelo.

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_3.png)

1. Agregue un nuevo formulario web al proyecto.
### **Paso 2: incrustar el control en el formulario web**
 Arrastre y suelte el control Aspose.Cells.GridWeb desde la caja de herramientas de Visual Studio al formulario web.

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

 Para obtener información sobre cómo agregar controles de cuadrícula Aspose.Cells a la caja de herramientas de Visual Studio, lea[Integre Aspose.Cells.Grid Controls con Visual Studio.NET](/cells/es/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

 Cuando el control se ha agregado al formulario, se representa así:

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_5.png)
### **Paso 3: Control de cambio de tamaño**
El formulario se representa en un tamaño predeterminado. Ajuste el tamaño arrastrando los bordes o las esquinas.

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_6.png)
### **Paso 4: Configuración de las propiedades de control**
 Aspose.Cells. El control GridWeb también se puede configurar usando varias propiedades.

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_7.png)

Es posible ajustar muchas propiedades del control con el cuadro de diálogo Propiedades. Las propiedades básicas incluyen altura, anchura, color y estilos visuales. Las propiedades avanzadas incluyen el modo de edición, el modo de sesión y el modo de doble clic. Además, es posible establecer controladores de eventos personalizados en el cuadro de diálogo Propiedades.

También hay algunas herramientas de configuración adicionales para Aspose.Cells.GridWeb que se pueden ver en la parte inferior del cuadro de diálogo Propiedades como hipervínculos, o haga clic con el botón derecho en el control GridWeb para encontrarlas. Estas herramientas de configuración incluyen:

- Botones de comando personalizados
#### **Botones de comando personalizados**
Para abrir el editor de botones de comando personalizados:
 Haga clic con el botón derecho en el control GridWeb y seleccione**Botones de comando personalizados**. 

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_8.png)



 Se muestra el cuadro de diálogo Editor de la colección CustomCommandButton.

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_9.png)

El cuadro de diálogo permite a los desarrolladores agregar y eliminar botones de comando personalizados en el control GridWeb.


### **Importante**
Aspose.Cells.GridWeb también proporciona sus archivos de recursos con el control. El "ac_cliente" es una carpeta (@ su directorio de instalación) que contiene archivos y Aspose.Cells. GridWeb usa esta carpeta para administrar su configuración interna y otras funciones, tiene archivos de secuencias de comandos, archivos de imagen y otros archivos para especificar el comportamiento de GridWeb y establecer otras operaciones. config se usa para administrar los recursos del cliente incrustado (imágenes, scripts, etc.) Además, cuando necesite implementar la aplicación web que tiene control GridWeb, también debe copiar el archivo "acw_cliente" en la carpeta de su proyecto, al menos su aplicación web (implementada en el servidor) no pudo encontrarlo. Siempre puede especificar la carpeta de recursos agregando las siguientes líneas de código en la sección de configuración (por ejemplo, en el archivo web.config en su Proyecto VS.NET):



|<p>{{< highlight "java" >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
|:- |


{{% alert color="primary" %}}

La ruta siempre está relacionada con el directorio del proyecto. No debe usar ningún directorio que esté fuera del directorio del proyecto. Por lo tanto, es necesario copiar el directorio "acw_client" (@ su carpeta de instalación de GridWeb) en el directorio/subdirectorio del proyecto.

{{% /alert %}}
### **Paso 5: Ejecución de la aplicación web**
 Ejecute la aplicación presionando Ctrl+F5 o haciendo clic en el**Comenzar** botón.

 Cuando la aplicación se ejecuta en un navegador, se muestra la página WebForm1.aspx, que ahora contiene un control Aspose.Cells.GridWeb vacío. Agregue valores a las celdas haciendo clic en ellas. También es posible realizar otras tareas como cambiar la altura de una fila o el ancho de una columna, copiar (Ctrl+C) o cortar (Ctrl+X) datos de celdas en el portapapeles y pegar (Ctrl+V) datos en celdas. . Para realizar más operaciones, haga clic derecho en el control para ver la lista completa de opciones.

**Menú contextual del control GridWeb** 

![todo:imagen_alternativa_texto](add-gridweb-to-web-form_10.png)
