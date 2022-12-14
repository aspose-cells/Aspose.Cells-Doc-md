---
title: Público API Cambios en Aspose.Cells 8.9.0
type: docs
weight: 300
url: /es/net/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.8.3 a la 8.9.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Se agregó la propiedad HtmlSaveOptions.DefaultFontName**
Aspose.Cells for .NET 8.9.0 ha expuesto la propiedad DefaultFontName para la clase HtmlSaveOptions que permite especificar el nombre de fuente predeterminado al representar hojas de cálculo en formato HTML. La fuente predeterminada se utilizará solo cuando la fuente de estilo no exista. El valor predeterminado de la propiedad HtmlSaveOptions.DefaultFontName es nulo, lo que significa que Aspose.Cells for .NET API utilizará la fuente universal que tiene la misma familia que la fuente original.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo sobre[Configuración de la fuente predeterminada para representar hojas de cálculo en formato HTML](/cells/es/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Se agregó la propiedad ImageOrPrintOptions.DefaultFont**
Aspose.Cells for .NET 8.9.0 permite establecer el nombre de fuente predeterminado para la clase ImageOrPrintOptions al exponer la propiedad DefaultFont. Dicha propiedad se puede usar cuando los caracteres Unicode en la hoja de cálculo no están configurados con la fuente correcta en el estilo de celda, por lo tanto, dichos caracteres pueden aparecer como bloques en las imágenes resultantes.

{{% alert color="primary" %}} 

Establezca la propiedad DefaultFont en MingLiu o MS Gothic para mostrar caracteres Unicode. Si no se establece dicha propiedad, Aspose.Cells utilizará la fuente predeterminada del sistema para mostrar caracteres Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo sobre[Configuración de fuente predeterminada para renderizar hojas de cálculo en formatos de imagen](/cells/es/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells for .NET API ha expuesto la propiedad de tipo booleano IsExcel2003Compatible para la clase de tabla dinámica que permite especificar si la tabla dinámica es compatible con Excel 2003 para fines de actualización. El valor predeterminado de la propiedad IsExcel2003Compatible es verdadero, lo que significa que una cadena debe tener 255 caracteres o menos. Si la cadena tiene más de 255 caracteres, se truncará. En caso de ser falsa, no se impondrá la restricción antes mencionada.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo sobre[Compatibilidad con Excel 2003 para actualizar tablas dinámicas](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells.GridWeb for .NET 8.9.0 ha expuesto el método de fábrica {GetVersion}} que devuelve la versión de lanzamiento del componente GridWeb.
