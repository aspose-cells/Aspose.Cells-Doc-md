---
title: Arbeitsblätter innerhalb einer Arbeitsmappe kopieren
type: docs
weight: 20
url: /de/net/copy-worksheets-within-a-workbook/
---

**Aspose.Cells** bietet eine überladene Methode, **Aspose.Cells.WorksheetCollection.AddCopy()**, die verwendet wird, um ein Arbeitsblatt zur Sammlung hinzuzufügen und Daten von einem vorhandenen Arbeitsblatt zu kopieren. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter. Die andere Version nimmt den Namen des Quellarbeitsblatts als Parameter.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

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
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
