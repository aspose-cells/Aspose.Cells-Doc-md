---
title: Imposta collegamenti esterni nelle formule in Aspose.Cells
type: docs
weight: 90
url: /it/net/set-external-links-in-formulas-in-aspose-cells/
---

{{% alert color="primary" %}} 

A volte è necessario includere collegamenti a file esterni nelle formule, ad esempio per valutare un valore di cella o di intervallo rispetto ad essi. Aspose.Cells fornisce questa funzionalità e questo documento spiega come utilizzarla.

{{% /alert %}} 

Il codice di esempio qui sotto mostra come includere file esterni nelle formule.

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **Scarica Esempio in Esecuzione**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
