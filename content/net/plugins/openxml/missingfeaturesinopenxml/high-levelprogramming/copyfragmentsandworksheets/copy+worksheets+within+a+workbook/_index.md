---
title : "Copy Worksheets within a Workbook" 
description : "" 
weight : 24874 
toc : false
type: docs
url: /net/plugins/openxml/missingfeaturesinopenxml/high-levelprogramming/copyfragmentsandworksheets/copy+worksheets+within+a+workbook/
---

# Aspose.Cells for .NET : Copy Worksheets within a Workbook


**Aspose.Cells** provides an overloaded method, **Aspose.Cells.WorksheetCollection.AddCopy()**, that is used to add a worksheet to the collection and copies data from an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet as the parameter.

The following example shows how to copy an existing worksheet within a workbook.

{{< code lang="cs" >}}
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
{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)

