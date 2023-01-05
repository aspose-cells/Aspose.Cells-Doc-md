---
title: Copiar hojas de trabajo dentro de un libro de trabajo
type: docs
weight: 20
url: /es/net/copy-worksheets-within-a-workbook/
---
**Aspose.Cells** proporciona un método sobrecargado,**Aspose.Cells.WorksheetCollection.AddCopy()**, que se usa para agregar una hoja de trabajo a la colección y copia datos de una hoja de trabajo existente. Una versión del método toma el índice de la hoja de cálculo de origen como parámetro. La otra versión toma el nombre de la hoja de cálculo de origen como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro de trabajo.

{{< highlight "csharp" >}}

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
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
