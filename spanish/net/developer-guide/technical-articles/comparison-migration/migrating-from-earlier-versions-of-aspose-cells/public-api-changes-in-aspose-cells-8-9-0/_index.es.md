---
title: Cambios en la API Pública en Aspose.Cells 8.9.0
type: docs
weight: 300
url: /es/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.8.3 hasta la 8.9.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos métodos públicos actualizados, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Propiedad Added HtmlSaveOptions.DefaultFontName**
Aspose.Cells for .NET 8.9.0 ha expuesto la propiedad DefaultFontName para la clase HtmlSaveOptions que permite especificar el nombre de fuente predeterminado al renderizar hojas de cálculo en formato HTML. La fuente predeterminada se usará solo cuando la fuente del estilo no exista. El valor predeterminado de la propiedad HtmlSaveOptions.DefaultFontName es null, lo que significa que la API Aspose.Cells for .NET utilizará la fuente universal que tenga la misma familia que la fuente original.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo sobre [Establecer fuente predeterminada al renderizar hojas de cálculo en formato HTML](/cells/es/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Propiedad Agregada ImageOrPrintOptions.DefaultFont**
Aspose.Cells for .NET 8.9.0 permite establecer el nombre de fuente predeterminado para la clase ImageOrPrintOptions mediante la exposición de la propiedad DefaultFont. Dicha propiedad puede usarse cuando los caracteres Unicode en la hoja de cálculo no están configurados con la fuente correcta en el estilo de celda, por lo que estos caracteres pueden aparecer como bloques en las imágenes resultantes.

{{% alert color="primary" %}} 

Establezca la propiedad DefaultFont en MingLiu o MS Gothic para mostrar caracteres Unicode. Si dicha propiedad no está establecida, Aspose.Cells utilizará la fuente predeterminada del sistema para mostrar caracteres Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo sobre [Establecer fuente predeterminada al renderizar hojas de cálculo en formatos de imagen](/cells/es/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **Se agregó la propiedad PivotTable.IsExcel2003Compatible**
La API Aspose.Cells for .NET ha expuesto la propiedad Booleana IsExcel2003Compatible para la clase PivotTable, que permite especificar si el PivotTable es compatible con Excel 2003 para fines de actualización. El valor predeterminado de la propiedad IsExcel2003Compatible es true, lo que significa que una cadena debe ser menor o igual a 255 caracteres. Si la cadena es mayor a 255 caracteres, se truncará. Si es false, no se impondrá la restricción mencionada anteriormente.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta función, revise el artículo sobre [Compatibilidad para Excel 2003 al actualizar tablas dinámicas](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **Se agregó el método GridWeb.GetVersion**
Aspose.Cells.GridWeb para .NET 8.9.0 ha expuesto el método de fábrica {GetVersion} que devuelve la versión de lanzamiento del componente GridWeb.
