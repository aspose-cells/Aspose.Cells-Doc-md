---
title: Cambios en la API pública en Aspose.Cells 8.1.0
type: docs
weight: 40
url: /es/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.0.2 hasta la 8.1.0, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Propiedad HtmlSaveOptions.ExportHiddenWorksheet Agregada**
La clase HtmlSaveOptions ha expuesto la propiedad ExportHiddenWorksheet la cual puede ser utilizada para especificar si las hojas de cálculo ocultas son exportadas al formato HTML. El valor predeterminado es true. mientras que si se establece en false, Aspose.Cells no exportará el contenido de la hoja de cálculo oculta.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Prevenir la exportación de hojas de cálculo ocultas](/cells/es/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Propiedad Cell.StringValueWithoutFormat Agregada**
Se ha agregado la propiedad StringValueWithoutFormat a la Clase Cell, para que los desarrolladores puedan recuperar el valor de la celda sin aplicar ningún formato.

El fragmento de código proporcionado a continuación demuestra el uso de la propiedad Cell.StringValueWithoutFormat en comparación con cell.DisplayStringValue al crear una hoja de cálculo desde cero y aplicar el formato numérico a una de las celdas.

**C#**

{{< highlight csharp >}}

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
## **Propiedades Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs Obsoletas**
Muchas propiedades de la clase BuiltInDocumentPropertyCollection han sido marcadas como obsoletas a partir de Aspose.Cells for .NET 8.1.0. Estas propiedades incluyen Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. La razón es que dichas propiedades no son útiles para la preservación de hojas de cálculo de Excel ya que Excel las omite. Estas propiedades fueron originalmente escritas para documentos de Word y presentaciones de PowerPoint.
{{< app/cells/assistant language="csharp" >}}
