---
title: Agregar GridWeb al formulario web
type: docs
weight: 10
url: /es/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: Este artículo introduce cómo trabajar con formularios web en GridWeb.
---

{{% alert color="primary" %}} 

Este tema proporciona una guía básica paso a paso para principiantes que les ayudará a crear y utilizar el control Aspose.Cells.GridWeb en aplicaciones web.

{{% /alert %}} 
## **Creación y uso del control Aspose.Cells.GridWeb**
### **Paso 1: Crear un Proyecto de Aplicación Web**
Primero, cree un proyecto de aplicación web en el que se utilizará el control Aspose.Cells.GridWeb:

1. Abra Visual Studio.
1. Desde el menú **Archivo**, seleccione **Nuevo** seguido de **Proyecto**. 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



Aparece un cuadro de diálogo Nuevo Proyecto.

1. Seleccione **Aplicación web ASP.NET** para el lenguaje deseado. 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. Seleccione la plantilla de **Formularios web**. 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. Agregue un nuevo formulario web al proyecto.
### **Paso 2: Incrustar el Control en el Formulario Web**
Arrastre y suelte el control Aspose.Cells.GridWeb desde la caja de herramientas de Visual Studio al formulario web. 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

Para aprender cómo agregar controles Aspose.Cells Grid al Cuadro de herramientas de Visual Studio, por favor lea [Integrar controles Aspose.Cells.Grid con Visual Studio.NET](/cells/es/net/aspose-cells-gridweb/integrar-controles-aspose-cells-grid-con-visual-studio-net/).

{{% /alert %}} 

Una vez que el control se ha agregado al formulario, se representa así: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **Paso 3: Redimensionar el Control**
El formulario se representa con un tamaño predeterminado. Ajuste el tamaño arrastrando los bordes o esquinas. 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **Paso 4: Configurar Propiedades del Control**
El control Aspose.Cells.GridWeb también se puede configurar utilizando diversas propiedades. 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

Es posible ajustar muchas propiedades del control con el cuadro de diálogo Propiedades. Las propiedades básicas incluyen altura, ancho, color y estilos visuales. Las propiedades avanzadas incluyen el modo de edición, modo de sesión y modo de doble clic. Además, es posible establecer manipuladores de eventos personalizados en el cuadro de diálogo Propiedades.

También hay algunas herramientas de configuración adicionales para Aspose.Cells.GridWeb que se pueden ver en la parte inferior del cuadro de diálogo de Propiedades como hipervínculos, o hacer clic derecho en el control GridWeb para encontrarlas. Estas herramientas de configuración incluyen:

- Botones de Comando Personalizados
#### **Botones de Comando Personalizados**
Para abrir el editor de botones de comando personalizados:
Hacer clic derecho en el control GridWeb y seleccionar **Botones de Comando Personalizados**. 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



Se muestra el cuadro de diálogo del Editor de Colección de Botones de Comando Personalizados. 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

El diálogo permite a los desarrolladores agregar y quitar botones de comando personalizados en el control GridWeb.


### **Importante**
Aspose.Cells.GridWeb también proporciona sus archivos de recursos con el control. El "acw_client" es una carpeta (en tu directorio de instalación) que contiene archivos y Aspose.Cells.GridWeb utiliza esta carpeta para gestionar su configuración interna y otras funcionalidades, tiene archivos de scripts, archivos de imagen y otros archivos para especificar el comportamiento de GridWeb y establecer otras operaciones. El archivo de configuración se utiliza para gestionar los recursos del cliente incrustados (imágenes, scripts, etc.). Además, cuando necesites implementar la aplicación web con el control GridWeb, también copiarás el directorio "acw_client" en la carpeta de tu proyecto al menos tu aplicación web (implementada en el servidor) no podría encontrarlo. Siempre puedes especificar la carpeta de recursos agregando las siguientes líneas de código en la sección de configuración (por ejemplo, en el archivo web.config de tu proyecto en Visual Studio .NET):



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

La ruta siempre está relacionada con el directorio del proyecto. No debes usar ningún directorio que esté fuera del directorio del proyecto. Por lo tanto, es necesario copiar el directorio "acw_client" (en tu carpeta de instalación de GridWeb) en el directorio/subdirectorio del proyecto.

{{% /alert %}}
### **Paso 5: Ejecutar la Aplicación Web**
Ejecuta la aplicación presionando Ctrl+F5 o haciendo clic en el botón **Iniciar**. 

Cuando la aplicación se ejecuta en un navegador, se muestra la página WebForm1.aspx, ahora con un control GridWeb de Aspose.Cells vacío. Agrega valores a las celdas haciendo clic en ellas. También es posible realizar otras tareas como cambiar la altura de una fila o el ancho de una columna, copiar (Ctrl+C) o cortar (Ctrl+X) datos de celda al portapapeles y pegar (Ctrl+V) datos en la celda. Para realizar más operaciones, haz clic derecho en el control para ver la lista completa de opciones. 

**Menú contextual del control GridWeb** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
