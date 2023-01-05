---
title: Trabajar con Visual Studio
type: docs
weight: 20
url: /es/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

Este tema explica cómo usar Aspose.Cells.GridWeb en aplicaciones ASP.NET con Visual Studio.NET 2005. Este tema es útil para los desarrolladores principiantes que trabajan con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Trabajando con Aspose.Cells.GridWeb usando Visual Studio 2013**
Este tema muestra cómo usar Aspose.Cells.GridWeb creando un sitio web de muestra en Visual Studio 2013. El proceso se ha dividido en pasos.
### **Paso 1: Creación de un nuevo sitio web**
1. Abra Visual Studio 2013.
1.  Desde el**Archivo** menú, seleccione**Nuevo Menú** , después**Sitio web**. 

![todo:imagen_alternativa_texto](working-with-visual-studio_1.png)


 Se abre el cuadro de diálogo Nuevo sitio web.

1.  Seleccione**ASP.NET Sitio de formularios web** de las plantillas instaladas de Visual Studio.
1.  Elija el modo HTTP para la ubicación del sitio web.

![todo:imagen_alternativa_texto](working-with-visual-studio_2.png)




1.  Especifique una ubicación donde se crearán y almacenarán los archivos del sitio web.
 1. Haga clic en**Navegar** en el cuadro de diálogo Nuevo sitio web.

![todo:imagen_alternativa_texto](working-with-visual-studio_3.png)



 Se muestra el cuadro de diálogo Elegir ubicación.

1.  Haga clic en el**IIS locales** pestaña.
Se muestran todas las carpetas y aplicaciones web almacenadas en su carpeta raíz de IIS (por ejemplo: C:\Inetpub\wwwroot).

![todo:imagen_alternativa_texto](working-with-visual-studio_4.png)




1. Ahora cree una nueva aplicación web en su IIS local donde se almacenarán los archivos del sitio web.
 El cuadro de diálogo Elegir ubicación le permite crear y eliminar aplicaciones web o directorios virtuales en su IIS local. Para crear una aplicación web, haga clic en un botón como se muestra a continuación en la figura.

![todo:imagen_alternativa_texto](working-with-visual-studio_5.png)



 Se crea una nueva aplicación web con el nombre predeterminado WebSite.

1. Cambie el nombre de la aplicación web. Lo renombramos GridWebOn2013.
1.  Hacer clic**Abierto**. 

![todo:imagen_alternativa_texto](working-with-visual-studio_6.png)



 Vuelve al cuadro de diálogo Nuevo sitio web. La ruta de la ubicación del sitio web se establece en<http://localhost/GridWebOn2013>. 

1.  Hacer clic**DE ACUERDO** para permitir que Visual Studio cree un sitio web.

![todo:imagen_alternativa_texto](working-with-visual-studio_7.png)
### **Paso 2: Comprobación de las vistas de origen y diseño de una página web**
 Visual Studio 2013 habrá creado un sitio web predeterminado. Contiene una página web default.aspx con texto y marcas ficticias.

**Vista de origen de la página default.aspx** 

![todo:imagen_alternativa_texto](working-with-visual-studio_8.png)



Todas las páginas web (incluido ASP.NET) se pueden abrir en dos modos. Una es la vista de fuente que permite a los desarrolladores acceder y modificar el código fuente. El segundo modo es la vista de diseño que se puede utilizar para diseñar páginas web de forma WYSIWYG. La captura de pantalla anterior muestra una vista de origen de la página web default.aspx. Para ver la vista de diseño, haga clic en**Diseño**. 

**Vista de diseño de la página default.aspx** 

![todo:imagen_alternativa_texto](working-with-visual-studio_9.png)




Elimine la página Default.aspx agregada por Visual Studio y agregue una nueva página Default.aspx en blanco.

![todo:imagen_alternativa_texto](working-with-visual-studio_10.png)
### **Paso 3: Agregar Aspose.Cells.GridWeb a la página web**
 Simplemente puede agregar el control Aspose.Cells.GridWeb (o GridWeb) a una página web arrastrándolo desde la caja de herramientas.

![todo:imagen_alternativa_texto](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

 Si no sabe cómo agregar Aspose.Cells.GridWeb a la caja de herramientas, consulte[Integre Aspose.Cells Grid Controls con Visual Studio.NET](/cells/es/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

 Una vez que el control GridWeb se coloca en la página web, se mostraría así:

![todo:imagen_alternativa_texto](working-with-visual-studio_12.png)



### **Paso 4: cambie la etiqueta <!DOCTYPE>**
1.  Cambie a la vista de fuente y encuentre lo siguiente**<!DOCTYPE>** etiqueta en el código fuente:

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1.  Seleccione la etiqueta completa.

![todo:imagen_alternativa_texto](working-with-visual-studio_13.png)




1.  Conservar, modificar o eliminar la<!DOCTYPE> etiqueta.
1.  O modificar el<!DOCTYPE> etiqueta con la siguiente:

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Paso 5: Cambiar el tamaño de Aspose.Cells.GridWeb Control**
 Puede cambiar el ancho y el alto del control GridWeb después de arrastrarlo al sitio web.

 En la vista de diseño, puede cambiar el tamaño del ancho y el alto de GridWeb.

![todo:imagen_alternativa_texto](working-with-visual-studio_14.png)



### **Paso 6: Configuración de las propiedades de Aspose.Cells.GridWeb**
 Configure las propiedades Aspose.Cells.GridWeb en WYSIWYG haciendo clic en el**Propiedades** botón en el lado derecho de Visual Studio 2013 IDE.
 Se muestra un cuadro de diálogo Propiedades.

![todo:imagen_alternativa_texto](working-with-visual-studio_15.png)



El panel Propiedades permite configurar la apariencia de GridWeb y algunas otras propiedades para controlar el comportamiento de GridWeb.
### **Paso 7: ejecutar su primer sitio web que contenga Aspose.Cells.GridWeb**
 Construir y ejecutar el sitio web.

1.  Ejecute el sitio web directamente desde Visual Studio presionando Ctrl+F5 o haciendo clic en**Empezar a depurar**. 

![todo:imagen_alternativa_texto](working-with-visual-studio_16.png)

 Ahora, puede comenzar a jugar con el control GridWeb.

**Control GridWeb en acción** 

![todo:imagen_alternativa_texto](working-with-visual-studio_17.png)
