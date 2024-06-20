---
title: Trabajar con Visual Studio
type: docs
weight: 20
url: /es/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: Este artículo presenta cómo usar GridWeb en Visual Studio.
---

{{% alert color="primary" %}} 

Este tema explica cómo usar Aspose.Cells.GridWeb en aplicaciones ASP.NET usando Visual Studio .NET 2005. Este tema es útil para los desarrolladores principiantes que trabajan con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Trabajar con Aspose.Cells.GridWeb usando Visual Studio 2013**
Este tema muestra cómo usar Aspose.Cells.GridWeb al crear un sitio web de ejemplo en Visual Studio 2013. El proceso se ha dividido en pasos.
### **Paso 1: Crear un nuevo sitio web**
1. Abra Visual Studio 2013.
1. Desde el menú **Archivo**, seleccione **Nuevo Menú**, luego **Sitio Web**. 

![todo:image_alt_text](working-with-visual-studio_1.png)


Se abre el cuadro de diálogo Nuevo sitio web. 

1. Seleccione **Sitio web de formularios web ASP.NET** de las plantillas instaladas de Visual Studio.
1. Elija el modo HTTP para la ubicación del sitio web. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. Especifique una ubicación donde se crearán y almacenarán los archivos del sitio web. 
   1. Haga clic en **Examinar** en el cuadro de diálogo Nuevo sitio web. 

![todo:image_alt_text](working-with-visual-studio_3.png)



Se muestra el cuadro de diálogo Elegir ubicación. 

1. Haga clic en la pestaña **IIS local**.
   Se muestran todas las carpetas y aplicaciones web almacenadas en su carpeta raíz de IIS (por ejemplo: C:\Inetpub\wwwroot). 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Ahora cree una nueva aplicación web en su IIS local donde se almacenarán los archivos del sitio web.
   El cuadro de diálogo Elegir ubicación le permite crear y eliminar aplicaciones web o directorios virtuales en su IIS local. Para crear una aplicación web, haga clic en un botón como se muestra a continuación en la figura. 

![todo:image_alt_text](working-with-visual-studio_5.png)



Se crea una nueva aplicación web con el nombre predeterminado WebSite. 

1. Cambie el nombre de la aplicación web. Lo renombramos a GridWebOn2013.
1. Haga clic en **Abrir**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. Haga clic en **Aceptar** para que Visual Studio cree un sitio web. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Paso 2: Verificación de las vistas de código fuente y diseño de una página web**
Visual Studio 2013 habrá creado un sitio web predeterminado. Contiene una página web default.aspx con algún texto ficticio y marcado. 

**Vista de código fuente de la página default.aspx** 

![todo:image_alt_text](working-with-visual-studio_8.png)



Todas las páginas web (incluidas las de ASP.NET) pueden abrirse en dos modos. Uno es la vista de código fuente que permite a los desarrolladores acceder y modificar el código fuente. El segundo modo es la vista de diseño que se puede utilizar para diseñar páginas web de forma WYSIWYG. La captura de pantalla anterior muestra una vista de código fuente de la página web default.aspx. Para ver la vista de diseño, haga clic en **Diseño**. 

**Vista de diseño de la página default.aspx** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Elimine la página Default.aspx agregada por Visual Studio y agregue una nueva página Default.aspx en blanco.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Paso 3: Agregar Aspose.Cells.GridWeb a la página web**
Simplemente puede agregar el control Aspose.Cells.GridWeb (o GridWeb) a una página web arrastrándolo desde la caja de herramientas. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

Si no sabe cómo agregar Aspose.Cells.GridWeb a la caja de herramientas, consulte [Integrar los controles de cuadrícula de Aspose.Cells con Visual Studio.NET](/cells/es/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

Una vez que el control GridWeb se coloca en la página web, se renderizará de la siguiente manera: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. Seleccione la etiqueta completa. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Paso 5: Cambiar el tamaño del control Aspose.Cells.GridWeb**
Puede cambiar el ancho y alto del control GridWeb después de arrastrarlo al sitio web. 

En la vista de diseño, puede cambiar el ancho y alto del control GridWeb. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Paso 6: Configurar las propiedades de Aspose.Cells.GridWeb**
Configure las propiedades de Aspose.Cells.GridWeb en WYSIWYG haciendo clic en el botón **Propiedades** en el lado derecho del IDE de Visual Studio 2013. 
Se muestra un cuadro de diálogo de propiedades. 

![todo:image_alt_text](working-with-visual-studio_15.png)



El panel de propiedades hace posible configurar la apariencia y algunas otras propiedades para controlar el comportamiento de GridWeb.
### **Paso 7: Ejecutar su primer sitio web que contiene Aspose.Cells.GridWeb**
Construya y ejecute el sitio web. 

1. Ejecute el sitio web directamente desde Visual Studio presionando Ctrl+F5 o haciendo clic en **Iniciar depuración**. 

![todo:image_alt_text](working-with-visual-studio_16.png)

Ahora puede comenzar a usar el control GridWeb. 

**Control GridWeb en acción** 

![todo:image_alt_text](working-with-visual-studio_17.png)
