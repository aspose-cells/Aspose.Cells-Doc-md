---
title: Cambios en la API Pública en Aspose.Cells 8.8.2
type: docs
weight: 280
url: /es/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.8.1 a la 8.8.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento entre bastidores en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Actualización Automática de Referencias al Eliminar Filas y Columnas en Blanco**
Aspose.Cells for .NET 8.8.2 ha expuesto las versiones sobrecargadas de los métodos Cells.DeleteBlankRows y Cells.DeleteBlankColumns. Los nuevos métodos pueden aceptar una instancia de la clase DeleteOptions y pueden utilizarse para superar las situaciones que podrían surgir debido a las referencias rotas en fórmulas, datos de series de gráficos, etc. La clase DeleteOptions actualmente tiene solo un miembro, una propiedad de tipo Booleano llamada UpdateReference. Si dicha propiedad se establece en verdadero y se pasa la instancia de la clase DeleteOptions a los métodos Cells.DeleteBlankRows y Cells.DeleteBlankColumns, la API ajustará internamente las referencias de la fórmula (si las hay) para acomodar los cambios.

{{% alert color="primary" %}} 

Para más detalles sobre esta funcionalidad, por favor revise el artículo detallado sobre [Eliminación de Filas y Columnas en Blanco con Referencias Actualizadas](/cells/es/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
