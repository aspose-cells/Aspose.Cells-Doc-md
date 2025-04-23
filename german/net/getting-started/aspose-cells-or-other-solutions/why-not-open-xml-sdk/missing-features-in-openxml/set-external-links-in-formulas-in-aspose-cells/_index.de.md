---
title: Externe Links in Formeln in Aspose.Cells einrichten
type: docs
weight: 90
url: /de/net/set-external-links-in-formulas-in-aspose-cells/
---

{{% alert color="primary" %}} 

Manchmal ist es notwendig, Links zu externen Dateien in Formeln einzuschließen, zum Beispiel um einen Zellen- oder Bereichswert gegen sie zu evaluieren. Aspose.Cells bietet diese Funktion und dieses Dokument erläutert, wie sie verwendet wird.

{{% /alert %}} 

Der nachfolgende Beispielcode zeigt, wie externe Dateien in Formeln eingebunden werden.

**C#**

{{< highlight csharp >}}

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
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **Laufendes Beispiel herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
