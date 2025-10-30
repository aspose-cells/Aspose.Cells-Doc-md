---
title: Cambios en la API pública en Aspose.Cells 8.1.0
type: docs
weight: 50
url: /es/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.0.2 hasta la 8.1.0, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Propiedad HtmlSaveOptions.ExportHiddenWorksheet Agregada**
La clase HtmlSaveOptions ha expuesto la propiedad ExportHiddenWorksheet la cual puede ser utilizada para especificar si las hojas de cálculo ocultas son exportadas al formato HTML. El valor predeterminado es true. mientras que si se establece en false, Aspose.Cells no exportará el contenido de la hoja de cálculo oculta.

{{% alert color="primary" %}} 

Por favor revise el artículo detallado sobre [Prevenir la Exportación de la Hoja de Cálculo Oculta](/cells/es/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Propiedad Cell.StringValueWithoutFormat Agregada**
Se ha agregado la propiedad StringValueWithoutFormat a la Clase Cell, para que los desarrolladores puedan recuperar el valor de la celda sin aplicar ningún formato. 

El fragmento de código proporcionado a continuación demuestra el uso del método Cell.getStringValueWithoutFormat en comparación con cell.getDisplayStringValue creando una hoja de cálculo desde cero y aplicando el formato numérico a una de las celdas. 

**Java**

{{< highlight csharp >}}

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

Valor de Cadena con Formato: 123,456
Valor de Cadena sin Formato: 123456

{{% /alert %}}
## **Propiedades Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs Obsoletas**
Muchas propiedades de la clase BuiltInDocumentPropertyCollection han sido marcadas como obsoletas a partir de Aspose.Cells for Java 8.1.0. Estas propiedades incluyen Bytes, Characters, CharactersWithSpaces, Lines y Paragraphs. La razón es que dichas propiedades no son útiles para preservar hojas de cálculo de Excel porque Excel las omite. Mientras que estas propiedades fueron originalmente diseñadas para documentos de Word y presentaciones de PowerPoint. 
{{< app/cells/assistant language="java" >}}
