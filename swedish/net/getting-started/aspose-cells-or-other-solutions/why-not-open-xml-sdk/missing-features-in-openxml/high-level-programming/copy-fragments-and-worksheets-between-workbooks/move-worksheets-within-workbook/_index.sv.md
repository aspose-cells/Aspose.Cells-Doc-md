---
title: Flytta kalkylblad inom arbetsbok
type: docs
weight: 30
url: /sv/net/move-worksheets-within-workbook/
---

Aspose.Cells tillhandahåller en metod, Aspose.Cells.Worksheet.MoveTo(), som används för att flytta ett kalkylblad till en annan plats i kalkylen. Metoden tar målkalkylbladets index som parameter.

Det följande exemplet visar hur man flyttar ett kalkylblad till en annan plats inom arbetsboken.

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
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)
