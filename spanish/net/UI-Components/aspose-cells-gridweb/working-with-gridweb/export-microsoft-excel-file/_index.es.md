---
title: Exportar archivo de Microsoft Excel
type: docs
weight: 50
url: /es/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb, exportar
description: Este artículo presenta cómo exportar un archivo en GridWeb.
---

{{% alert color="primary" %}} 

Es posible crear nuevos o manipular archivos de Microsoft Excel existentes en sitios web en modo GUI utilizando el control Aspose.Cells.GridWeb. Luego, los archivos pueden guardarse como archivos de Excel. Aspose.Cells.GridWeb sirve como un editor de hojas de cálculo en línea de manera efectiva. Este tema describe cómo guardar contenido de la cuadrícula en archivos de Excel.

{{% /alert %}} 
## **Exportar archivos de Excel**
### **Exportar como un archivo**
Para guardar el contenido del control Aspose.Cells.GridWeb como un archivo de Excel:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Guarde su trabajo como un archivo de Excel en una ruta especificada.
1. Ejecute la aplicación.

{{% alert color="primary" %}} 

Si no sabes cómo agregar el control Aspose.Cells.GridWeb a tu formulario web, debes consultar [Agregar GridWeb a Formulario Web](/cells/es/net/aspose-cells-gridweb/add-gridweb-to-web-form/)

{{% /alert %}} 

Cuando se agrega el control Aspose.Cells.GridWeb a un formulario de Windows, el control se instancia automáticamente y se agrega al formulario con un tamaño predeterminado. No es necesario crear un objeto de control Aspose.Cells.GridWeb, todo lo que tienes que hacer es arrastrar y soltar el control y comenzar a usarlo.

El ejemplo de código a continuación ilustra cómo guardar el contenido de la cuadrícula en un archivo de Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Si tu sistema de archivos es NTFS, otorga acceso de lectura/escritura a las cuentas de usuario ASPNET o Everyone o recibirás una excepción de acceso denegado en tiempo de ejecución.

{{% /alert %}} 

El fragmento de código anterior se puede utilizar de varias formas. Una forma común es agregar un botón que guarde el contenido de la cuadrícula en un archivo de Excel al hacer clic. Aspose.Cells.GridWeb ofrece un enfoque más fácil para la tarea. Aspose.Cells.GridWeb tiene un evento llamado SaveCommand. El fragmento de código anterior se puede agregar al manejador de eventos del evento SaveCommand que permite a los usuarios guardar su trabajo haciendo clic en el botón **Guardar** integrado de Aspose.Cells.GridWeb.

**El evento SaveCommand de GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**Guardar contenido de la cuadrícula en Excel al hacer clic en el botón Guardar integrado de GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Si estás trabajando en Visual Studio, puedes crear fácilmente el manejador de eventos del evento SaveCommand haciendo doble clic en el evento en el panel de **Propiedades**. Para obtener más información al respecto, consulta [Trabajar con Eventos de GridWeb](/cells/es/net/aspose-cells-gridweb/working-with-gridweb-events/)

{{% /alert %}} 
### **Exportar como un flujo**
También es posible guardar el contenido de la cuadrícula en un flujo (por ejemplo, MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
