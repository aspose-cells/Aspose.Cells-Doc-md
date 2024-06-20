---
title: Copiar hojas de cálculo dentro de un libro
type: docs
weight: 20
url: /es/net/copy-worksheets-within-a-workbook/
---

**Aspose.Cells** proporciona un método sobrecargado, **Aspose.Cells.WorksheetCollection.AddCopy()**, que se utiliza para agregar una hoja de cálculo a la colección y copiar datos de una hoja de cálculo existente. Una versión del método toma el índice de la hoja de cálculo de origen como parámetro. La otra versión toma el nombre de la hoja de cálculo de origen como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro.

{{< highlight csharp >}}

 //Create a new Workbook.

//Open an existing Excel file.

Workbook wb = new Workbook("ResultedBook.xls");

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing

//sheet within the Workbook.

sheets.AddCopy("MySheet");

//Save the Excel file.

wb.Save("Copy Worksheet.xls");

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
