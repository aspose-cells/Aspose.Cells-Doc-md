---
title: Público API Cambios en Aspose.Cells 8.1.0
type: docs
weight: 50
url: /es/java/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.0.2 a la 8.1.0, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó la propiedad HtmlSaveOptions.ExportHiddenWorksheet**
La clase HtmlSaveOptions ha expuesto la propiedad ExportHiddenWorksheet que se puede usar para especificar si las hojas de trabajo ocultas se exportan al formato HTML. El valor por defecto es verdadero. mientras que si se establece en falso, el Aspose.Cells no exportará el contenido oculto de la hoja de trabajo.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Impedir la exportación de hojas de cálculo ocultas](/cells/es/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Se agregó la propiedad Cell.StringValueWithoutFormat**
 La propiedad StringValueWithoutFormat se ha agregado a la clase Cell para facilitar a los desarrolladores la recuperación del valor de la celda sin aplicar ningún formato.

El fragmento de código proporcionado a continuación demuestra el uso del método Cell.getStringValueWithoutFormat en comparación con el método cell.getDisplayStringValue al crear una hoja de cálculo desde cero y aplicar el formato de número a una de las celdas.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

La salida del código anterior es la siguiente

Valor de cadena con formato: 123,456
Valor de cadena sin formato: 123456

{{% /alert %}}
## **Propiedades de bytes, caracteres, caracteres con espacios, líneas y párrafos obsoletos**
 Muchas propiedades de la clase BuiltInDocumentPropertyCollection se han marcado como obsoletas a partir de Aspose.Cells for .NET 8.1.0. Estas propiedades incluyen bytes, caracteres, caracteres con espacios, líneas y párrafos. La razón es que las propiedades antes mencionadas no sirven para conservar las hojas de cálculo de Excel porque Excel las omite. Donde estas propiedades se escribieron originalmente para documentos de Word y presentaciones PowerPoint.
