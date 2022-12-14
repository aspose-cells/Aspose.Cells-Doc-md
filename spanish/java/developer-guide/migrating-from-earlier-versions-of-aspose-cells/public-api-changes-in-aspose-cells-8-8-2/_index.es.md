---
title: Público API Cambios en Aspose.Cells 8.8.2
type: docs
weight: 290
url: /es/java/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.8.1 a la 8.8.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Actualice automáticamente las referencias mientras elimina filas y columnas en blanco**
 Aspose.Cells for Java 8.8.2 ha expuesto las versiones sobrecargadas de los métodos Cells.deleteBlankRows y Cells.deleteBlankColumns. Los nuevos métodos pueden aceptar una instancia de la clase DeleteOptions y pueden usarse para superar las situaciones que podrían surgir debido a referencias rotas en fórmulas, datos de series de gráficos, etc. La clase DeleteOptions actualmente tiene solo un miembro, una propiedad de tipo booleano con el nombre UpdateReference. Si dicha propiedad se establece en verdadero y la instancia de la clase DeleteOptions se pasa a los métodos Cells.deleteBlankRows y Cells.deleteBlankColumns, API ajustará internamente las referencias de fórmula (si las hay) para adaptarse a los cambios.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Eliminación de filas y columnas en blanco con referencias actualizadas](/cells/es/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
