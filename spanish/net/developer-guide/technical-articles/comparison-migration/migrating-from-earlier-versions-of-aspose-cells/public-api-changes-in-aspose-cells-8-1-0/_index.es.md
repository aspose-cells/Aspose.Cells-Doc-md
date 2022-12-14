---
title: Público API Cambios en Aspose.Cells 8.1.0
type: docs
weight: 40
url: /es/net/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.0.2 a la 8.1.0, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó la propiedad HtmlSaveOptions.ExportHiddenWorksheet**
La clase HtmlSaveOptions ha expuesto la propiedad ExportHiddenWorksheet que se puede usar para especificar si las hojas de trabajo ocultas se exportan a formato HTML. El valor por defecto es verdadero. mientras que si se establece en falso, el Aspose.Cells no exportará el contenido oculto de la hoja de trabajo.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Impedir la exportación de hojas de cálculo ocultas](/cells/es/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Se agregó la propiedad Cell.StringValueWithoutFormat**
La propiedad StringValueWithoutFormat se ha agregado a la clase Cell para facilitar a los desarrolladores la recuperación del valor de la celda sin aplicar ningún formato.

El fragmento de código proporcionado a continuación demuestra el uso de la propiedad Cell.StringValueWithoutFormat en comparación con cell.DisplayStringValue al crear una hoja de cálculo desde cero y aplicar el formato de número a una de las celdas.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

La salida del código anterior es la siguiente

123,456

123456

{{% /alert %}}
## **Propiedades de bytes, caracteres, caracteres con espacios, líneas y párrafos obsoletos**
Muchas propiedades de la clase BuiltInDocumentPropertyCollection se han marcado como obsoletas a partir de Aspose.Cells for .NET 8.1.0. Estas propiedades incluyen bytes, caracteres, caracteres con espacios, líneas y párrafos. La razón es que las propiedades antes mencionadas no sirven para conservar las hojas de cálculo de Excel porque Excel las omite. Donde estas propiedades se escribieron originalmente para documentos de Word y presentaciones PowerPoint.
