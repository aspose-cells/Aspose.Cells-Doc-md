---
title: Arbeitsblätter innerhalb der Arbeitsmappe verschieben
type: docs
weight: 30
url: /de/net/move-worksheets-within-workbook/
---
Aspose.Cells stellt eine Methode bereit, Aspose.Cells.Worksheet.MoveTo(), die verwendet wird, um ein Arbeitsblatt an eine andere Stelle in der Tabelle zu verschieben. Die Methode nimmt den Index des Zielarbeitsblatts als Parameter.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt an eine andere Stelle innerhalb der Arbeitsmappe verschieben.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Move Worksheet.xlsx";

//Open an existing excel file.

Workbook wb = new Workbook(FileName);

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Get the first worksheet.

Worksheet worksheet = sheets[0];

string test = worksheet.Name;

//Move the first sheet to the third position in the workbook.

worksheet.MoveTo(2);

//Save the excel file.

wb.Save(FileName);

{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)
