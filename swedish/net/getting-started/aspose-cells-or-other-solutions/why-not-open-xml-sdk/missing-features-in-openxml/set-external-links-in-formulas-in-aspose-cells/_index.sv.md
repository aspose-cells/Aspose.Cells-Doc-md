---
title: Ställ in externa länkar i formler i Aspose.Cells
type: docs
weight: 90
url: /sv/net/set-external-links-in-formulas-in-aspose-cells/
---
{{% alert color="primary" %}} 

Ibland är det nödvändigt att inkludera länkar till externa filer i formler, till exempel för att utvärdera en cell eller ett områdesvärde mot dem. Aspose.Cells tillhandahåller den här funktionen och det här dokumentet förklarar hur du använder den.

{{% /alert %}} 

Exempelkoden nedan visar hur man inkluderar externa filer i formler.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Set External Links in Formula.xlsx";

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get first Worksheet

Worksheet sheet = workbook.Worksheets[0];

//Get Cells collection

Aspose.Cells.Cells cells = sheet.Cells;

//Set formula with external links

cells["A1"].Formula = "=SUM('[book1.xls]Sheet1'!A2, '[book1.xls]Sheet1'!A4)";

//Set formula with external links

cells["A2"].Formula = "='[book1.xls]Sheet1'!A8";

//Save the workbook

workbook.Save(FileName);

{{< /highlight >}}
## **Ladda ner exempelkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **Ladda ner körningsexempel**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
