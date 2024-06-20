---
title: Cambios en la API Pública en Aspose.Cells 8.9.0
type: docs
weight: 310
url: /es/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.8.3 hasta la 8.9.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos métodos públicos actualizados, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Propiedad Added HtmlSaveOptions.DefaultFontName**
Aspose.Cells for Java 8.9.0 ha expuesto la propiedad DefaultFontName para la clase HtmlSaveOptions que permite especificar el nombre de fuente predeterminado al renderizar hojas de cálculo en formato HTML. La fuente predeterminada se utilizará solo cuando la fuente del estilo no exista. El valor predeterminado de la propiedad HtmlSaveOptions.DefaultFontName es nulo, lo que significa que la  API Aspose.Cells for Java utilizará la fuente universal que tenga la misma familia que la fuente original.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revisa el artículo en [Establecer Fuente Predeterminada para Renderizar Hojas de Cálculo en Formato HTML](/cells/es/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Propiedad Agregada ImageOrPrintOptions.DefaultFont**
Aspose.Cells for Java 8.9.0 permite establecer el nombre de fuente predeterminado para la clase ImageOrPrintOptions al exponer la propiedad DefaultFont. Dicha propiedad se puede utilizar cuando los caracteres Unicode en la hoja de cálculo no están configurados con la fuente correcta en el estilo de celda, por lo que esos caracteres pueden aparecer como bloques en las imágenes resultantes. 

{{% alert color="primary" %}} 

Establezca la propiedad DefaultFont en MingLiu o MS Gothic para mostrar caracteres Unicode. Si dicha propiedad no está establecida, Aspose.Cells utilizará la fuente predeterminada del sistema para mostrar caracteres Unicode. 

{{% /alert %}} {{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revisa el artículo en [Establecer Fuente Predeterminada para Renderizar Hojas de Cálculo en Formatos de Imagen](/cells/es/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **Propiedad Agregada PivotTable.Excel2003Compatible**
La API Aspose.Cells for Java ha expuesto la propiedad Excel2003Compatible de tipo Boolean para la clase PivotTable que permite especificar si la PivotTable es compatible con Excel 2003 para fines de actualización. El valor predeterminado de la propiedad Excel2003Compatible es verdadero, lo que significa que una cadena debe tener menos o igual a 255 caracteres. Si la cadena es mayor a 255 caracteres, será truncada. Si es falsa, no se impondrá la restricción mencionada anteriormente.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revisa el artículo en [Compatibilidad con Excel 2003 para Actualizar Tablas Dinámicas](/cells/es/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
