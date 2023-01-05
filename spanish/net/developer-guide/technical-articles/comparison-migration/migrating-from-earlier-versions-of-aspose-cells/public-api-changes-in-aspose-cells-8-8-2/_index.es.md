---
title: Público API Cambios en Aspose.Cells 8.8.2
type: docs
weight: 280
url: /es/net/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.8.1 a la 8.8.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Actualizar referencias automáticamente mientras se eliminan filas y columnas en blanco**
Aspose.Cells for .NET 8.8.2 ha expuesto las versiones sobrecargadas de los métodos Cells.DeleteBlankRows y Cells.DeleteBlankColumns. Los nuevos métodos pueden aceptar una instancia de la clase DeleteOptions y pueden usarse para superar las situaciones que podrían surgir debido a referencias rotas en fórmulas, datos de series de gráficos, etc. La clase DeleteOptions actualmente tiene solo un miembro, una propiedad de tipo booleano con el nombre UpdateReference. Si dicha propiedad se establece en verdadero y la instancia de la clase DeleteOptions se pasa a los métodos Cells.DeleteBlankRows y Cells.DeleteBlankColumns, API ajustará internamente las referencias de fórmula (si las hay) para adaptarse a los cambios.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Eliminación de filas y columnas en blanco con referencias actualizadas](/cells/es/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
