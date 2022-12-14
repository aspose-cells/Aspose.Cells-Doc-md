---
title: Exportar archivo Excel Microsoft
type: docs
weight: 50
url: /es/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Es posible crear nuevos archivos Excel Microsoft o manipularlos existentes en sitios web en modo GUI utilizando el control Aspose.Cells.GridWeb. Los archivos se pueden guardar en archivos de Excel. Aspose.Cells.GridWeb sirve efectivamente como un editor de hojas de cálculo en línea. Este tema describe cómo guardar el contenido de la cuadrícula en archivos de Excel.

{{% /alert %}} 
## **Exportar archivos de Excel**
### **Exportar como archivo**
Para guardar el contenido del control Aspose.Cells.GridWeb como un archivo de Excel:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Guarde su trabajo como un archivo de Excel en una ruta específica.
1. Ejecute la aplicación.

{{% alert color="primary" %}} 

 Si no sabe cómo agregar el control Aspose.Cells.GridWeb a su formulario web, debe consultar[Agregar GridWeb al formulario web](/cells/es/net/add-gridweb-to-web-form/)

{{% /alert %}} 

Cuando se agrega el control Aspose.Cells.GridWeb a un formulario de Windows, el control se instancia automáticamente y se agrega al formulario con un tamaño predeterminado. No tiene que crear un objeto de control Aspose.Cells.GridWeb, todo lo que tiene que hacer es arrastrar y soltar el control y comenzar a usarlo.

El siguiente ejemplo de código ilustra cómo guardar el contenido de la cuadrícula en un archivo de Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Si su sistema de archivos es NTFS, otorgue acceso de lectura/escritura a las cuentas de usuario ASPNET o Todos o obtendrá una excepción de acceso denegado en tiempo de ejecución.

{{% /alert %}} 

El fragmento de código anterior se puede utilizar de varias maneras. Una forma común es agregar un botón que guarde el contenido de la cuadrícula en un archivo de Excel cuando se hace clic. Aspose.Cells. GridWeb ofrece un enfoque más sencillo para la tarea. Aspose.Cells. GridWeb tiene un evento llamado SaveCommand. El fragmento de código anterior se puede agregar al controlador de eventos del evento SaveCommand que permite a los usuarios guardar su trabajo haciendo clic en Aspose.Cells.**Ahorrar** botón.

**El evento SaveCommand de GridWeb** 

![todo:imagen_alternativa_texto](export-microsoft-excel-file_1.jpg)

**Guardar el contenido de la cuadrícula en Excel haciendo clic en el botón Guardar incorporado de GridWeb** 

![todo:imagen_alternativa_texto](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

 Si está trabajando en Visual Studio, puede crear fácilmente el controlador de eventos del evento SaveCommand haciendo doble clic en el evento en el**Propiedades** cristal. Para obtener más información al respecto, consulte[Trabajar con eventos de GridWeb](/cells/es/net/working-with-gridweb-events/)

{{% /alert %}} 
### **Exportar como flujo**
También es posible guardar el contenido de la cuadrícula en un flujo (por ejemplo, MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
