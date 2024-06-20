---
title: Sposta i fogli all interno del workbook
type: docs
weight: 30
url: /it/net/move-worksheets-within-workbook/
---

Aspose.Cells fornisce un metodo, Aspose.Cells.Worksheet.MoveTo(), utilizzato per spostare un foglio di lavoro in un'altra posizione nel foglio di calcolo. Il metodo prende l'indice del foglio di lavoro di destinazione come parametro.

L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno del libro di lavoro.

{{< highlight csharp >}}

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)
